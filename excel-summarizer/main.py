import pandas as pd
import ollama


def create_summary(row):
    """Create a summary text for each row based on available information, excluding specified columns."""
    # Columns to exclude from summary
    excluded_columns = {
        'Título', 'País', 'DOI', 'Idade média', 'Faixa etária', 'Sexo',
        'IMC (baixo peso, peso normal, excesso de peso, obesidade)', 
        'Álcool', 'Tabaco', 'Comorbilidades relevantes',
        'Outros fármacos (concomitant medication use)', 
        'Adesão à tx (padrão de adesão à tx)'
    }
    
    # Create a structured summary from remaining columns
    summary_parts = []
    
    for column_name, value in row.items():
        # Skip excluded columns and empty values
        if column_name in excluded_columns or pd.isna(value) or str(value).strip() == '':
            continue
            
        # Format the column-value pair
        clean_value = str(value).strip()
        if clean_value and clean_value.lower() not in ['nan', 'none', 'null']:
            summary_parts.append(f"{column_name}: {clean_value}")
    
    # Join all parts with "; "
    summary = "; ".join(summary_parts)
    
    # If no meaningful information is available, provide a default summary
    if not summary_parts:
        summary = "Incomplete record with missing information"
    
    return summary


def create_ai_summary(row):
    """Create an AI-generated summary using Ollama."""
    try:
        # Prepare the context for AI summarization
        context = []

        if pd.notna(row.get("Author")):
            context.append(f"Author: {row['Author']}")
        if pd.notna(row.get("Year")):
            context.append(
                f"Year: {int(row['Year']) if isinstance(row['Year'], float) else row['Year']}"
            )
        if pd.notna(row.get("Title")):
            context.append(f"Title: {row['Title']}")
        if pd.notna(row.get("Journal")):
            context.append(f"Journal: {row['Journal']}")
        if pd.notna(row.get("Final Decision")):
            context.append(f"Final Decision: {row['Final Decision']}")
        if pd.notna(row.get("Reason")):
            context.append(f"Reason: {row['Reason']}")

        if not context:
            return "Incomplete record with missing information"

        # Create prompt for AI
        prompt = f"""
        Please create a concise summary (maximum 2 sentences) for this research paper review record:
        
        {"; ".join(context)}
        
        Focus on the key aspects: what the paper is about, the decision made, and why it was made.
        """

        # Generate AI summary using Ollama
        response = ollama.chat(
            model="gemma3",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response["message"]["content"].strip()

    except Exception as e:
        print(f"Error generating AI summary: {e}")
        # Fallback to basic summary
        return create_summary(row)


def main():
    """Main function to process the Excel file and create summaries."""
    input_file = "conflitos.xlsx"
    output_file = "conflitos_with_summaries.xlsx"
    sheet_name = "FT- Review Results"

    try:
        # Read the Excel file
        print(f"Reading Excel file: {input_file}")
        df = pd.read_excel(input_file, sheet_name=sheet_name)
        print(f"Loaded {len(df)} rows and {len(df.columns)} columns")

        # Display basic information about the data
        print(f"\nColumns: {df.columns.tolist()}")
        print(f"Shape: {df.shape}")

        # Create summaries for each row
        print("\nCreating summaries...")

        # Try to use AI summaries first, fallback to basic summaries if Ollama is not available
        try:
            # Test if Ollama is available
            ollama.list()
            print("Using AI-generated summaries with Ollama...")
            df["Summary"] = df.apply(create_ai_summary, axis=1)
        except Exception as e:
            print(f"Ollama not available ({e}), using basic summaries...")
            df["Summary"] = df.apply(create_summary, axis=1)

        # Save to new Excel file
        print(f"\nSaving results to: {output_file}")
        df.to_excel(output_file, sheet_name=sheet_name, index=False)

        print(f"✅ Successfully processed {len(df)} rows and saved to {output_file}")

        # Display sample of results
        print("\nSample summaries:")
        print("-" * 80)
        for i in range(min(3, len(df))):
            row = df.iloc[i]
            print(f"Row {i + 1}:")
            print(f"  Original: {row.get('Title', 'N/A')}")
            print(f"  Summary: {row['Summary']}")
            print()

    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found in the current directory")
    except Exception as e:
        print(f"❌ Error processing file: {e}")


if __name__ == "__main__":
    main()
