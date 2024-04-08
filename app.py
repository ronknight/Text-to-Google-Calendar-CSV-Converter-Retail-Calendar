import csv

def txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as txt_file:
        lines = txt_file.readlines()

    events = []
    for line in lines:
        if line.strip() != '':
            parts = line.strip().split(',')
            if '-' in parts[0]:
                dates = parts[0].split('-')
                for date in dates:
                    events.append([date.strip(), parts[1]])
            else:
                events.append([parts[0], parts[1]])

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'Description'])
        for event in events:
            start_date = event[0]
            end_date = event[0]
            start_time = ''
            end_time = ''
            if ' - ' in start_date:
                start_date, end_date = start_date.split(' - ')
            if 'Starts (' in start_date:
                start_date = start_date.split('(')[0].strip()
            if ' (ends' in end_date:
                end_date = end_date.split('(')[0].strip()
            if 'Wimbledon' in start_date:
                start_date = '2024-07-03'
                end_date = '2024-07-16'
            writer.writerow([event[1], start_date, start_time, end_date, end_time, ''])

if __name__ == "__main__":
    input_file = "events.txt"  # Change this to the path of your input text file if it's not in the same directory
    output_file = "events.csv"  # Change this to the desired path for the output CSV file
    txt_to_csv(input_file, output_file)
    print("Conversion complete.")
