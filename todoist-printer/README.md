# Todoist Thermal Printer

A Python application that retrieves today's tasks from Todoist and prints them on a thermal printer or displays them in a beautiful console format.

## Features

- 🔗 **Todoist Integration**: Uses the official Todoist API to fetch tasks
- 📅 **Today's Tasks**: Automatically filters for today's tasks and overdue items
- 🎫 **Two Print Modes**: 
  - **Separate Mode** (Default): Each task prints as an individual ticket that can be cut and placed on a board
  - **Grouped Mode**: All tasks printed together in a single document
- 🖨️ **Multiple Printer Support**: USB, Serial, Network, and file output
- 📊 **Rich Console Display**: Beautiful table format when printer is not available
- 🏷️ **Project Organization**: Groups tasks by project for better organization
- ⚡ **Priority & Labels**: Shows task priorities and labels
- 📱 **Cross-platform**: Works on Windows, macOS, and Linux

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd todoist-printer
```

2. Install dependencies:
```bash
pip install -e .
```

Or install manually:
```bash
pip install todoist-api-python python-escpos pillow python-dotenv click rich
```

## Configuration

1. Get your Todoist API token:
   - Go to [Todoist Integrations Settings](https://todoist.com/prefs/integrations)
   - Copy your API token

2. Set up environment variables:
```bash
cp .env.example .env
```

3. Edit `.env` file and add your API token:
```
TODOIST_API_TOKEN=your_api_token_here
```

## Usage

### Basic Usage (Console Output)

#### Separate Tickets Mode (Default)
```bash
uv run python main.py
```

#### Grouped Tasks Mode
```bash
uv run python main.py --print-mode grouped
```

### Thermal Printer Usage

#### USB Printer (Separate Tickets)
```bash
uv run python main.py --printer-type usb --printer-config "vendor_id=0x04b8,product_id=0x0202"
```

#### USB Printer (Grouped Tasks)
```bash
uv run python main.py --printer-type usb --printer-config "vendor_id=0x04b8,product_id=0x0202" --print-mode grouped
```

#### Serial Printer
```bash
uv run python main.py --printer-type serial --printer-config "port=/dev/ttyUSB0,baudrate=9600"
```

#### Network Printer
```bash
uv run python main.py --printer-type network --printer-config "host=192.168.1.100,port=9100"
```

#### File Output
```bash
uv run python main.py --printer-type file --output-file tasks.txt
```

## Print Modes

### Separate Tickets Mode (Default)
- Each task is printed as an individual ticket
- Perfect for cutting and placing on a kanban board or task board
- Includes task details, priority, due date, and a completion checkbox
- Automatically cuts paper between tickets (if supported by printer)

### Grouped Tasks Mode
- All tasks are printed together in a single document
- Tasks are grouped by project
- More compact format for overview purposes
- Traditional single-document output

### Environment Variables

You can also set configuration via environment variables:

```bash
export TODOIST_API_TOKEN="your_token_here"
export PRINT_MODE="separate"  # or "grouped"
export PRINTER_TYPE="file"
export OUTPUT_FILE="my_tasks.txt"
uv run python main.py
```

## Printer Setup

### USB Thermal Printers

For USB thermal printers, you'll need to find the vendor and product IDs:

```bash
# On Linux/macOS
lsusb

# Look for your printer and note the vendor:product IDs
# Example: Bus 001 Device 004: ID 04b8:0202 Seiko Epson Corp.
```

Common USB thermal printer IDs:
- **Epson TM series**: `vendor_id=0x04b8, product_id=0x0202`
- **Star TSP series**: `vendor_id=0x0519, product_id=0x0001`
- **Citizen CT series**: `vendor_id=0x1CB0, product_id=0x0003`

### Serial Printers

For serial printers, you'll need:
- Port (e.g., `/dev/ttyUSB0` on Linux, `COM1` on Windows)
- Baud rate (usually 9600, 19200, or 38400)

### Network Printers

For network printers, you'll need:
- IP address of the printer
- Port (usually 9100 for raw printing)

## Sample Output

### Console Output
```
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Project            ┃ Task                        ┃ Due              ┃ Priority ┃ Labels       ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ Work               │ Finish quarterly report     │ 2024-01-15 09:00 │ HIGH     │ urgent       │
│                    │ Team meeting preparation    │ 2024-01-15       │          │              │
│ Personal           │ Buy groceries               │ 2024-01-15       │          │ shopping     │
│                    │ Call dentist                │ 2024-01-14       │ Medium   │ health       │
└────────────────────┴─────────────────────────────┴──────────────────┴──────────┴──────────────┘
```

### Thermal Printer Output
```
     TODAY'S TASKS
====================
Generated: 2024-01-15 08:30

WORK
----
1. Finish quarterly report
   Priority: HIGH
   Labels: urgent

2. Team meeting preparation

PERSONAL
--------
1. Buy groceries
   Labels: shopping

2. Call dentist
   Priority: Medium
   Labels: health

====================
Have a productive day!
```

## Troubleshooting

### Permission Issues (Linux/macOS)
```bash
# Add user to dialout group for serial printers
sudo usermod -a -G dialout $USER

# Set USB permissions
sudo chmod 666 /dev/ttyUSB0
```

### Printer Not Found
- Check USB connection and try `lsusb` (Linux/macOS) or Device Manager (Windows)
- Verify printer drivers are installed
- Try different vendor/product ID combinations

### API Issues
- Verify your Todoist API token is correct
- Check internet connection
- Ensure you haven't exceeded API rate limits (1000 requests per 15 minutes)

## Dependencies

- **todoist-api-python**: Official Todoist API client
- **python-escpos**: Thermal printer control library
- **rich**: Beautiful console output
- **click**: Command-line interface
- **python-dotenv**: Environment variable management
- **pillow**: Image processing (required by escpos)

## License

This project is open source. Feel free to modify and distribute as needed.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For issues related to:
- **Todoist API**: Check the [official documentation](https://developer.todoist.com/rest/v2/)
- **Thermal printing**: Refer to [python-escpos documentation](https://python-escpos.readthedocs.io/)
- **This application**: Open an issue in this repository