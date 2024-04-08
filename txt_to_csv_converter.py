import csv

def txt_to_csv(input_file, output_file):
    """
    Convert a text file containing events to a Google Calendar compatible CSV format.

    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to save the output CSV file.

    Returns:
        None
    """
    # Read the lines from the input text file
    with open(input_file, 'r') as txt_file:
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
                dates = parts[0].split('-')
                # Split the date range and add individual dates to the events list
                for date in dates:
                    events.append([date.strip(), parts[1]])
            else:
                # If the line doesn't contain a date range, add the date and event to the events list
                events.append([parts[0], parts[1]])

    # Write the events to the output CSV file
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write the header row
        writer.writerow(['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'Description'])
        # Iterate through each event and write it to the CSV file
        for event in events:
            start_date = event[0]
            end_date = event[0]
            start_time = ''
            end_time = ''
            # Check for special cases and adjust start and end dates accordingly
            if ' - ' in start_date:
                start_date, end_date = start_date.split(' - ')
            if 'Starts (' in start_date:
                start_date = start_date.split('(')[0].strip()
            if ' (ends' in end_date:
                end_date = end_date.split('(')[0].strip()
            if 'Wimbledon' in start_date:
                start_date = '2024-07-03'
                end_date = '2024-07-16'
            # Write the event to the CSV file
            writer.writerow([event[1], start_date, start_time, end_date, end_time, ''])

if __name__ == "__main__":
    # Input and output file paths
    input_file = "event.txt"  # Change this to the path of your input text file if it's not in the same directory
    output_file = "events.csv"  # Change this to the desired path for the output CSV file
    # Convert the text file to CSV
    txt_to_csv(input_file, output_file)
    print("Conversion complete.")
