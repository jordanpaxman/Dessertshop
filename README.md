# DessertShop

DessertShop is a Python-based application that allows customers to place dessert orders, generate receipts, and manage customer order history. The program supports both a command-line interface (CLI) and a graphical user interface (GUI).

## Features

- Supports ordering different types of desserts:
  - Candy
  - Cookies
  - Ice Cream
  - Sundaes
- Admin module for managing customer order history
- Generates receipts in PDF format using `reportlab`
- Freezer module to temporarily store dessert items
- Supports multiple payment methods: Cash, Card, and Phone
- GUI mode available using `DessertApp`

## Installation

### Prerequisites

Ensure you have Python 3 installed. You also need to install the `reportlab` package for generating receipts:

```bash
pip install reportlab
```

Ensure you have `kivy` package installed for GUI:

```bash
pip3 install kivy
```

### Clone the Repository

```bash
git clone https://github.com/yourusername/DessertShop.git
cd DessertShop
```

## Usage

### Running the CLI Version

To run the application in command-line mode:

```bash
python3 dessertshop.py
```

### Running the GUI Version

To launch the graphical user interface:

```bash
python3 dessertshop.py -g
```

## Order Process

1. The user selects dessert items to add to their order.
2. The program asks for customer details.
3. The user selects a payment method.
4. A receipt is generated and displayed.

## Admin Module

The admin module provides the following functionalities:

1. View the customer list.
2. View customer order history.
3. Find the best customer based on order frequency.
4. Exit the admin module.

## Files and Modules

- `dessertshop.py` - Main application file
- `dessert.py` - Contains classes for different dessert types
- `receipt.py` - Handles receipt generation
- `freeze.py` - Manages temporary storage of desserts
- `dessertshop_gui.py` - GUI implementation

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

## Author

Jordan Paxman
