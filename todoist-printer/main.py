#!/usr/bin/env python3
"""
Todoist Thermal Printer

A Python application that retrieves today's tasks from Todoist and prints them on a thermal printer.
"""

import os
import sys
from datetime import datetime, timezone
from typing import List, Optional
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from dotenv import load_dotenv

try:
    from todoist_api_python.api import TodoistAPI
except ImportError:
    print("Error: todoist-api-python not installed. Run: uv add todoist-api-python")
    sys.exit(1)

try:
    from escpos.printer import Usb, Serial, Network, File
    from escpos.exceptions import Error as EscposError
except ImportError:
    print("Warning: python-escpos not installed. Thermal printing will be disabled.")
    print("To enable thermal printing, run: uv add python-escpos")
    print("To list USB printers, also run: uv add pyusb")
    Usb = Serial = Network = File = None
    EscposError = Exception

try:
    import usb.core
    import usb.util
except ImportError:
    usb = None

# Load environment variables
load_dotenv()

console = Console()


def list_usb_printers():
    """List available USB devices that might be printers."""
    if not usb:
        console.print("[red]Error: pyusb not installed. Run: uv add pyusb[/red]")
        return
    
    console.print("[bold blue]Available USB Devices:[/bold blue]")
    console.print("(Potential printers are shown below)\n")
    
    # Create table for USB devices
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Vendor ID", style="cyan")
    table.add_column("Product ID", style="cyan")
    table.add_column("Manufacturer", style="white")
    table.add_column("Product", style="white")
    table.add_column("Likely Printer?", style="green")
    
    devices = usb.core.find(find_all=True)
    printer_keywords = ['printer', 'thermal', 'receipt', 'pos', 'epson', 'star', 'citizen', 'bixolon']
    
    found_devices = False
    for device in devices:
        try:
            # Get device info
            vendor_id = f"0x{device.idVendor:04x}"
            product_id = f"0x{device.idProduct:04x}"
            
            # Try to get manufacturer and product strings
            try:
                manufacturer = usb.util.get_string(device, device.iManufacturer) if device.iManufacturer else "Unknown"
            except:
                manufacturer = "Unknown"
            
            try:
                product = usb.util.get_string(device, device.iProduct) if device.iProduct else "Unknown"
            except:
                product = "Unknown"
            
            # Check if it's likely a printer
            is_likely_printer = any(keyword in (manufacturer + " " + product).lower() 
                                  for keyword in printer_keywords)
            
            # Only show devices that might be printers or have printer-related info
            if is_likely_printer or "printer" in product.lower() or "thermal" in product.lower():
                table.add_row(
                    vendor_id,
                    product_id,
                    manufacturer,
                    product,
                    "[green]Yes[/green]" if is_likely_printer else "[yellow]Maybe[/yellow]"
                )
                found_devices = True
            
        except Exception as e:
            # Skip devices that can't be accessed
            continue
    
    if found_devices:
        console.print(table)
        console.print("\n[bold yellow]Usage:[/bold yellow]")
        console.print("Use the Vendor ID and Product ID with the --printer-config option:")
        console.print("Example: --printer-config vendor_id=0x04b8,product_id=0x0202")
    else:
        console.print("[yellow]No obvious printer devices found.[/yellow]")
        console.print("Your printer might not be connected, or might require different detection methods.")
        console.print("\n[bold]Common thermal printer IDs:[/bold]")
        console.print("• Epson: vendor_id=0x04b8, product_id=0x0202")
        console.print("• Star: vendor_id=0x0519, product_id=0x0001")
        console.print("• Citizen: vendor_id=0x1d57, product_id=0x0001")


class TodoistTaskRetriever:
    """Handles retrieval of tasks from Todoist API."""
    
    def __init__(self, api_token: str):
        """Initialize with Todoist API token."""
        self.api = TodoistAPI(api_token)
    
    def get_todays_tasks(self) -> List[dict]:
        """Retrieve today's tasks from Todoist."""
        try:
            # Get all tasks
            tasks_lists = self.api.get_tasks()
            
            # Get today's date in YYYY-MM-DD format
            today = datetime.now().strftime('%Y-%m-%d')
            
            # Filter for today's and overdue tasks
            todays_tasks = []
            
            for tasks in tasks_lists:
                for task in tasks:
                    # Ensure task is not completed
                    if task.is_completed:
                        continue
                    if task.due:

                        due_date = task.due.date.strftime('%Y-%m-%d')
                        
                        if due_date == today or due_date < today:

                            todays_tasks.append(task)
            
            return todays_tasks
            
        except Exception as e:
            console.print(f"[red]Error retrieving tasks: {e}[/red]")
            return []
    
    def get_projects(self) -> dict:
        """Get all projects to map project IDs to names."""
        try:
            project_lists = self.api.get_projects()
            project_dict = {}
            
            # Handle the projects list
            for projects in project_lists:
                for project in projects:
                    project_dict[project.id] = project.name
                
            return project_dict
        except Exception as e:
            console.print(f"[red]Error retrieving projects: {e}[/red]")
            return {}


class ThermalPrinter:
    """Handles thermal printer operations."""
    
    def __init__(self, printer_type: str = "file", **kwargs):
        """Initialize thermal printer."""
        self.printer = None
        self.printer_type = printer_type
        
        if not any([Usb, Serial, Network, File]):
            console.print("[yellow]Warning: python-escpos not available. Printing to console only.[/yellow]")
            return
        
        try:
            if printer_type == "usb":
                # Common USB thermal printer settings
                vendor_id = kwargs.get('vendor_id', 0x04b8)  # Epson
                product_id = kwargs.get('product_id', 0x0202)
                console.print(f"[blue]Attempting to connect to USB printer: vendor_id={hex(vendor_id)}, product_id={hex(product_id)}[/blue]")
                
                try:
                    self.printer = Usb(vendor_id, product_id)
                    # Test the connection by trying to get printer status
                    console.print("[green]USB printer connected successfully![/green]")
                except Exception as usb_error:
                    console.print(f"[red]Failed to connect to USB printer: {usb_error}[/red]")
                    console.print("[yellow]Troubleshooting tips:[/yellow]")
                    console.print("1. Check if the printer is connected and powered on")
                    console.print("2. Run --list-usb-printers to find the correct vendor/product ID")
                    console.print("3. Make sure you have the correct permissions (try running with sudo on Linux)")
                    console.print("4. Check if the printer driver is installed")
                    raise usb_error
                    
            elif printer_type == "serial":
                port = kwargs.get('port', '/dev/ttyUSB0')
                baudrate = kwargs.get('baudrate', 9600)
                console.print(f"[blue]Connecting to serial printer: port={port}, baudrate={baudrate}[/blue]")
                self.printer = Serial(port, baudrate)
            elif printer_type == "network":
                host = kwargs.get('host', '192.168.1.100')
                port = kwargs.get('port', 9100)
                console.print(f"[blue]Connecting to network printer: {host}:{port}[/blue]")
                self.printer = Network(host, port)
            elif printer_type == "file":
                filename = kwargs.get('filename', 'todoist_tasks.txt')
                console.print(f"[blue]Writing to file: {filename}[/blue]")
                self.printer = File(filename)
            
        except Exception as e:
            console.print(f"[red]Error initializing printer: {e}[/red]")
            self.printer = None
    
    def print_tasks(self, tasks: List[dict], projects: dict):
        """Print tasks to thermal printer."""
        if not self.printer:
            console.print("[yellow]No printer available, falling back to console output[/yellow]")
            self._print_to_console(tasks, projects)
            return
        
        console.print(f"[blue]Printing {len(tasks)} tasks to {self.printer_type} printer...[/blue]")
        
        try:
            # Header
            self.printer.set(align='center', bold=True, double_width=True, double_height=True)
            self.printer.text("TODAY'S TASKS\n")
            self.printer.text("=" * 20 + "\n")
            
            # Current date and time
            self.printer.set(align='center')
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.printer.text(f"Generated: {current_time}\n\n")
            
            if not tasks:
                self.printer.set(align='center')
                self.printer.text("No tasks for today!\n")
                self.printer.text("Great job! 🎉\n")
            else:
                self.printer.set(align='left')
                
                # Group tasks by project
                tasks_by_project = {}
                for task in tasks:
                    project_name = projects.get(task.project_id, "Unknown Project")
                    if project_name not in tasks_by_project:
                        tasks_by_project[project_name] = []
                    tasks_by_project[project_name].append(task)
                
                # Print tasks grouped by project
                for project_name, project_tasks in tasks_by_project.items():
                    # Project header
                    self.printer.set(bold=True)
                    self.printer.text(f"\n{project_name.upper()}\n")
                    self.printer.text("-" * len(project_name) + "\n")
                    
                    # Tasks in project
                    self.printer.set()  # Reset formatting
                    for i, task in enumerate(project_tasks, 1):
                        # Task content
                        self.printer.text(f"{i}. {task.content}\n")
                        
                        # Priority
                        if task.priority > 1:
                            priority_map = {2: "Low", 3: "Medium", 4: "HIGH"}
                            self.printer.text(f"   Priority: {priority_map.get(task.priority, 'Normal')}\n")
                        
                        # Labels
                        if task.labels:
                            labels_str = ", ".join(task.labels)
                            self.printer.text(f"   Labels: {labels_str}\n")
                        
                        self.printer.text("\n")
            
            # Footer
            self.printer.text("\n" + "=" * 15 + "\n")
            self.printer.set(align='center')
            self.printer.text("Have a productive day!\n\n")
            
            # Cut paper (if supported)
            try:
                self.printer.cut()
            except:
                pass
            
            console.print("[green]Tasks successfully printed to thermal printer![/green]")
            
        except Exception as e:
            console.print(f"[red]Error printing: {e}[/red]")
            self._print_to_console(tasks, projects)
    
    def _print_to_console(self, tasks: List[dict], projects: dict):
        """Fallback: print tasks to console with rich formatting."""
        console.print(Panel.fit(
            "[bold blue]TODAY'S TASKS[/bold blue]",
            border_style="blue"
        ))
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        console.print(f"[dim]Generated: {current_time}[/dim]\n")
        
        if not tasks:
            console.print(Panel(
                "[green]No tasks for today!\nGreat job! 🎉[/green]",
                title="Status",
                border_style="green"
            ))
            return
        
        # Group tasks by project
        tasks_by_project = {}
        for task in tasks:
            project_name = projects.get(task.project_id, "Unknown Project")
            if project_name not in tasks_by_project:
                tasks_by_project[project_name] = []
            tasks_by_project[project_name].append(task)
        
        # Create table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Project", style="cyan", no_wrap=True)
        table.add_column("Task", style="white")
        table.add_column("Due", style="yellow")
        table.add_column("Priority", style="red")
        table.add_column("Labels", style="green")
        
        for project_name, project_tasks in tasks_by_project.items():
            for i, task in enumerate(project_tasks):
                # Due date formatting
                due_text = ""
                if task.due:
                    due_text = task.due.date if hasattr(task.due, 'date') else str(task.due.date)
                    if hasattr(task.due, 'datetime') and task.due.datetime:
                        time_part = task.due.datetime.split('T')[1][:5]
                        due_text += f" {time_part}"
                    # Compare date strings properly
                    if isinstance(due_text, str) and due_text[:10] < datetime.now().strftime('%Y-%m-%d'):
                        due_text = f"[red]{due_text} (OVERDUE)[/red]"
                
                # Priority formatting
                priority_text = ""
                if task.priority > 1:
                    priority_map = {2: "Low", 3: "Medium", 4: "[red]HIGH[/red]"}
                    priority_text = priority_map.get(task.priority, "Normal")
                
                # Labels formatting
                labels_text = ", ".join(task.labels) if task.labels else ""
                
                # Only show project name for first task in each project
                project_display = project_name if i == 0 else ""
                
                table.add_row(
                    project_display,
                    task.content,
                    due_text,
                    priority_text,
                    labels_text
                )
        
        console.print(table)


@click.command()
@click.option('--token', envvar='TODOIST_API_TOKEN', 
              help='Todoist API token (or set TODOIST_API_TOKEN environment variable)')
@click.option('--printer-type', envvar='PRINTER_TYPE', default='file', 
              type=click.Choice(['usb', 'serial', 'network', 'file']),
              help='Type of printer to use (or set PRINTER_TYPE environment variable)')
@click.option('--printer-config', default='', 
              help='Printer configuration (format: key=value,key=value)')
@click.option('--output-file', envvar='OUTPUT_FILE', default='todoist_tasks.txt',
              help='Output file for file printer type (or set OUTPUT_FILE environment variable)')
@click.option('--list-usb-printers', 'list_usb_printers_flag', is_flag=True,
              help='List available USB printers and exit')
def main(token: str, printer_type: str, printer_config: str, output_file: str, list_usb_printers_flag: bool):
    """
    Todoist Thermal Printer - Retrieve today's tasks and print them.
    
    Set your Todoist API token using the TODOIST_API_TOKEN environment variable
    or pass it using the --token option.
    
    You can get your API token from: https://todoist.com/prefs/integrations
    """
    
    # Handle list USB printers option
    if list_usb_printers_flag:
        list_usb_printers()
        return
    
    if not token:
        console.print("[red]Error: No Todoist API token provided![/red]")
        console.print("Set the TODOIST_API_TOKEN environment variable or use --token option")
        console.print("Get your token from: https://todoist.com/prefs/integrations")
        sys.exit(1)
    
    console.print("[blue]Todoist Thermal Printer[/blue]")
    console.print("Retrieving today's tasks...")
    
    # Initialize task retriever
    task_retriever = TodoistTaskRetriever(token)
    
    # Get today's tasks and projects
    tasks = task_retriever.get_todays_tasks()
    projects = task_retriever.get_projects()
    
    console.print(f"Found {len(tasks)} task(s) for today")
    
    # Parse printer configuration
    printer_kwargs = {'filename': output_file} if printer_type == 'file' else {}
    
    # Add environment variable support for printer configuration
    if printer_type == 'usb':
        # Try to get USB printer config from environment variables
        vendor_id = os.getenv('PRINTER_VENDOR_ID')
        product_id = os.getenv('PRINTER_PRODUCT_ID')
        if vendor_id:
            try:
                printer_kwargs['vendor_id'] = int(vendor_id, 0)  # Support hex notation
            except ValueError:
                console.print(f"[yellow]Warning: Invalid PRINTER_VENDOR_ID format: {vendor_id}[/yellow]")
        if product_id:
            try:
                printer_kwargs['product_id'] = int(product_id, 0)  # Support hex notation
            except ValueError:
                console.print(f"[yellow]Warning: Invalid PRINTER_PRODUCT_ID format: {product_id}[/yellow]")
    elif printer_type == 'serial':
        port = os.getenv('PRINTER_PORT')
        baudrate = os.getenv('PRINTER_BAUDRATE')
        if port:
            printer_kwargs['port'] = port
        if baudrate:
            try:
                printer_kwargs['baudrate'] = int(baudrate)
            except ValueError:
                console.print(f"[yellow]Warning: Invalid PRINTER_BAUDRATE format: {baudrate}[/yellow]")
    elif printer_type == 'network':
        host = os.getenv('PRINTER_HOST')
        port = os.getenv('PRINTER_PORT')
        if host:
            printer_kwargs['host'] = host
        if port:
            try:
                printer_kwargs['port'] = int(port)
            except ValueError:
                console.print(f"[yellow]Warning: Invalid PRINTER_PORT format: {port}[/yellow]")
    
    # Override with command line printer_config if provided
    if printer_config:
        for pair in printer_config.split(','):
            if '=' in pair:
                key, value = pair.split('=', 1)
                # Try to convert to int if possible
                try:
                    value = int(value, 0)  # Support hex (0x) notation
                except ValueError:
                    pass
                printer_kwargs[key.strip()] = value
    
    # Initialize printer and print tasks
    printer = ThermalPrinter(printer_type, **printer_kwargs)
    printer.print_tasks(tasks, projects)


if __name__ == "__main__":
    main()
