def create(template, id, order):
    # Open input.txt for reading and output.txt for writing
    with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
        # Read lines from input.txt
        records = input_file.readlines()

        # Process each record and write to output.txt
        for record in records:
            # Remove newline character from the end of the record
            record = record.strip()
            line = template.format(id=id, record=record, order=order)
            # Write the processed record to output.txt
            output_file.write(line + "\n")
            print(line)
            # Increment id and order for the next record
            id      += 1
            order   += 1

def get_template():
    with open("template.txt", "r") as f:
        return f.readline().strip()


if __name__ == "__main__":
    t = get_template()
    create(t, 1, 41)
