import csv

def txt_to_csv(input_file, output_file, year):
    """
    Convert a text file containing events to the specified CSV format.

    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to save the output CSV file.
        year (str): Year to be appended to the dates.

    Returns:
        None
    """
    # Dictionary to map month names to their corresponding numbers
    month_map = {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12"
    }

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
                # Split the date range by hyphen
                date_range = parts[0].split(' - ')
                if len(date_range) == 2:
                    start_date, end_date = date_range[0], date_range[1]
                    start_month, start_day = start_date.split()
                    end_date_parts = end_date.split()
                    if len(end_date_parts) == 2:
                        end_month, end_day = end_date_parts
                        # Convert month names to numbers
                        start_month_num = month_map.get(start_month)
                        end_month_num = month_map.get(end_month)
                        if start_month_num and end_month_num:
                            events.append([parts[1].strip(), f"{start_month_num}/{start_day}/{year} - {end_month_num}/{end_day}/{year}", 'TRUE'])
                        else:
                            print(f"Error: Invalid month name in date range: {parts[0]}")
                    else:
                        print(f"Error: Invalid end date format in date range: {parts[0]}")
                else:
                    print(f"Error: Invalid date range format: {parts[0]}")
            else:
                # Split the date by space
                date_parts = parts[0].split()
                # Ensure that date_parts contain enough elements
                if len(date_parts) == 2:
                    month, day = date_parts[0], date_parts[1]
                    # Convert month name to number
                    month_num = month_map.get(month)
                    if month_num:
                        events.append([parts[1].strip(), f"{month_num}/{day}/{year}", 'TRUE'])
                    else:
                        print(f"Error: Invalid month name in date: {parts[0]}")
                else:
                    print(f"Error: Invalid date format: {parts[0]}")

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
    year = "2024"  # Specify the year
    # Convert the text file to CSV
    txt_to_csv(input_file, output_file, year)
    print("Conversion complete.")
