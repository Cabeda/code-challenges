import pandas as pd
import ollama
import datetime
import swifter


def create_summary(row):
    """Create a summary text for each row based on available information, excluding specified columns."""

    # Join all parts with "; "
    summary = f"{row.get("Autor", "Unknown Author")} ({row.get("Ano", "Unknown Year")}) conducted a ({row.get("Tipo de estudo", "Unknown Type")}), in ({row.get("País", "Unknown Country")}), where they investigated the use of LZD in ({row.get("Número de participantes", "Unknown Nº")}) patients with ({row.get("Indicação para uso de LZD", "Unknown indication")}). The main outcomes on Lzd adverse effects were {row.get("Tipo de efeito", "Unknown AE")} with a frequency of {row.get("Frequência", "Unknown Frequency")}."

    return summary


def create_ai_summary(row):
    """Create an AI-generated summary using Ollama, excluding specified columns."""
    try:
        # Columns to exclude from summary
        excluded_columns = {
            "Título",
            "DOI",
            "Idade média",
            "Faixa etária",
            "Sexo",
            "IMC (baixo peso, peso normal, excesso de peso, obesidade)",
            "Álcool",
            "Tabaco",
            "Comorbilidades relevantes",
            "Outros fármacos (concomitant medication use)",
            "Adesão à tx (padrão de adesão à tx)",
        }

        # Prepare the context for AI summarization
        context = []

        for column_name, value in row.items():
            # Skip excluded columns and empty values
            if (
                column_name in excluded_columns
                or pd.isna(value)
                or str(value).strip() == ""
            ):
                continue

            # Format the column-value pair
            clean_value = str(value).strip()
            if clean_value and clean_value.lower() not in ["nan", "none", "null"]:
                context.append(f"{column_name}: {clean_value}")

        if not context:
            return "Incomplete record with missing information"

        # Create prompt for AI
        prompt = f"""
        Please create a concise summary (maximum 2 sentences) for this research data record:
        
        {"; ".join(context)}

        The text should have the following structure:

        {row.get("Autor", "Unknown Author")} ({row.get("Ano", "Unknown Year")}) conducted a ({row.get("Tipo de estudo", "Unknown Type")}), in ({row.get("País", "Unknown Country")}), where they investigated the use of LZD in ({row.get("Número de participantes", "Unknown Nº")}) patients with ({row.get("Indicação para uso de LZD", "Unknown indication")}). The main outcomes on Lzd adverse effects were {row.get("Tipo de efeito", "Unknown AE")} with a frequency of {row.get("Frequência", "Unknown Frequency")}.
        """

        # Generate AI summary using Ollama
        response = ollama.chat(
            model="gemma3n",
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
    output_file = f"conflitos_with_summaries_{datetime.datetime.today().strftime('%Y_%m_%d')}.xlsx"
    sheet_name = "Tabela de extração"

    try:
        # Read the Excel file with proper header handling
        print(f"Reading Excel file: {input_file}")
        # Read without header first to get the structure
        df_raw = pd.read_excel(input_file, sheet_name=sheet_name, header=None)

        # Use row 1 as column headers and start data from row 2
        headers = df_raw.iloc[1].tolist()
        df = df_raw.iloc[2:].copy()
        df.columns = headers
        df = df.reset_index(drop=True)
        # Temporarily limit the number of rows for testing
        # df = df.head(3)

        print(f"Loaded {len(df)} rows and {len(df.columns)} columns")

        # Display basic information about the data
        print(f"\nColumns: {df.columns.tolist()}")
        print(f"Shape: {df.shape}")

        # Create summaries for each row using basic summary (faster)
        print("\nCreating summaries...")
        print("Using basic summaries...")
        df["Summary"] = df.apply(create_summary, axis=1)

        print("\nCreating AI-generated summaries...")
        print("Using AI summaries...")
        # df["Summary_AI"] = df.apply(create_ai_summary, axis=1)
        df["Summary_AI"] = df.swifter.apply(create_ai_summary, axis=1)


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
            print(f"  Summary: {row['Summary_AI']}")
            print()

    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found in the current directory")
    except Exception as e:
        print(f"❌ Error processing file: {e}")


if __name__ == "__main__":
    main()
