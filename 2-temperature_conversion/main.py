import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert temperature between Fahrenheit and Celsius.')

    # Define temperature argument
    parser.add_argument('temperature', type=float, help='Temperature value to convert, either Fahrenheit or Celsius.')

    # Define mutually exclusive group for Fahrenheit and Celsius flags
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--fahrenheit', action='store_true', help='Specify temperature in Fahrenheit.')
    group.add_argument('-c', '--celsius', action='store_true', help='Specify temperature in Celsius.')

    # Parse command-line arguments
    return parser.parse_args()

def convertFahrenheitToCelsius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5 / 9)

def convertCelsiusToFahrenheit(degreesCelsius):
    return  degreesCelsius * (9 / 5) + 32

def convert_temperature(args):
    if args.fahrenheit:
        # Convert Fahrenheit to Celsius
        celsius = convertFahrenheitToCelsius(args.temperature)
        print(f"{args.temperature} Fahrenheit is {celsius:.2f} Celsius.")
    elif args.celsius:
        # Convert Celsius to Fahrenheit
        fahrenheit = convertCelsiusToFahrenheit(args.temperature)
        print(f"{args.temperature} Celsius is {fahrenheit:.2f} Fahrenheit.")
    else:
        print("Please specify either -f or -c flag.")

def main():

    args = parse_arguments()
    convert_temperature(args)

    return

if __name__ == "__main__":
    main()