import csv

file_path = "uk.csv"
count = 0
city = 'cambridge'

try:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        csv_reader = csv.reader(file)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Convert row elements to lowercase for case-insensitive comparison
            row_lower = [element.lower() for element in row]

            if any('specialist' in element for element in row_lower) and city in row_lower:
                count += 1  # Increment the counter for each matching row
                print(row)

    print(f"Total rows found with 'Skilled Worker' and {city}: {count}")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
