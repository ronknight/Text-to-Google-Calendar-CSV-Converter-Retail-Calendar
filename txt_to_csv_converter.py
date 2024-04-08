import csv

def txt_to_csv(input_file, output_file):
    """
    Convert a text file containing events to the specified CSV format.

    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to save the output CSV file.

    Returns:
        None
    """
    # Read the lines from the input text file
    with open(input_file, 'r') as txt_file:
        # Skip the first line (label)
        next(txt_file)
        lines = txt_file.readlines()

    # Initialize an empty list to store events
    events = []

    # Iterate through each line in the text file
    for line in lines:
        # Skip empty lines
        if line.strip() != '':
            # Split each line by comma
            parts = line.strip().split(',')
            # If the line contains a date range
            if '-' in parts[0]:
                events.append([parts[1].strip(), parts[0].strip(), 'TRUE'])
            else:
                events.append([parts[1].strip(), parts[0].strip(), 'TRUE'])

    # Write the events to the output CSV file
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write the header row
        writer.writerow(['Subject', 'Start Date', 'All Day Event'])
        # Write each event to the CSV file
        for event in events:
            writer.writerow(event)

if __name__ == "__main__":
    # Input and output file paths
    input_file = "events.txt"  # Change this to the path of your input text file if it's not in the same directory
    output_file = "events.csv"  # Change this to the desired path for the output CSV file
    # Convert the text file to CSV
    txt_to_csv(input_file, output_file)
    print("Conversion complete.")
