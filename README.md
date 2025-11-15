# Crypiva: Simple Password Generator

Crypiva is a simple Python script for generating strong, random passwords. It's designed to be straightforward and easy to use from the command line.

## Features

*   Generates strong passwords with a customizable length.
*   Optionally include or exclude digits and symbols.
*   Simple command-line interface.

## Getting Started

### 1. Installation

First, clone the repository to your local machine and navigate into the directory:
```bash
git clone https://github.com/YOUR_USERNAME/Crypiva.git
cd Crypiva
```

Next, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Usage

Run the script from your terminal to generate a password.

**Generate a default password (12 characters, with digits and symbols):**
```bash
python script.py
```
> Example output: `s&aP7!k#tE9b`

By default, the script generates a password with a length of 12 characters, including letters, digits, and symbols. You can customize this behavior using command-line arguments.

**Generate a password with a specific length:**
```bash
# Generates a 20-character password
python script.py --length 20
```

**Generate a password without symbols:**
```bash
# Generates a 16-character password with only letters and numbers
python script.py --length 16 --no-symbols
```

## Contributing

Contributions are always welcome! Please feel free to open an issue or submit a pull request.