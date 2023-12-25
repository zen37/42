# Temperature Converter

This script provides a simple command-line interface for converting temperatures between Fahrenheit and Celsius.

## Usage

### Prerequisites

Make sure you have Python installed on your system.

### Running the script

1. Clone the repository or download the script.

    ```bash
    git clone https://github.com/your-username/temperature-converter.git
    cd temperature-converter
    ```

2. Run the script with the desired temperature and unit flags.

    ```bash
    python temperature_converter.py -f 32
    ```

    or

    ```bash
    python temperature_converter.py -c 0
    ```

## Command-line Options

```bash
usage: temperature_converter.py [-h] (-f | -c) temperature

Convert temperature between Fahrenheit and Celsius.

positional arguments:
  temperature           Temperature value to convert, either Fahrenheit or Celsius.

optional arguments:
  -h, --help            show this help message and exit
  -f, --fahrenheit      Specify temperature in Fahrenheit.
  -c, --celsius         Specify temperature in Celsius.
