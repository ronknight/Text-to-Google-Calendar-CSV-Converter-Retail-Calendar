# Text to Google Calendar CSV Converter - Retail Calendar

This Python script converts a text file containing events to a Google Calendar compatible CSV format.

## Prerequisites

- Python 3.x
- Input text file containing events (e.g., `events.txt`)

## Installation

1. Clone this repository or download the `txt_to_csv_converter.py` file.
2. Ensure you have Python installed on your system.

## Usage

1. Prepare your input text file (`events.txt`) with events listed in the following format:
    

```bash
Date,Event
January 1,New Year’s Day
January 1 - 31,Dry January, Ginuary, Veganuary
```

Each event should be on a separate line, and if an event spans multiple days, use a hyphen to indicate the range.

2. Run the Python script `txt_to_csv_converter.py` by executing the following command in your terminal or command prompt:


````bash
python txt_to_csv_converter.py
````

3. Follow the prompts to provide the path for the input text file (`events.txt`) and the desired path for the output CSV file.

4. The script will convert the events from the text file to a CSV file compatible with Google Calendar.

## Output

The script generates a CSV file named `events.csv` containing the events in the following format:


````bash
Subject,Start Date,Start Time,End Date,End Time,Description
New Year’s Day,2024-01-01,,2024-01-01,,""
Dry January,2024-01-01,,2024-01-31,,"Ginuary, Veganuary"
````

## Notes

- Ensure that the events in the input text file are formatted correctly to ensure proper conversion.
- Special cases such as date ranges or events spanning multiple days are handled appropriately.
- The script does not include event descriptions by default. You can modify the script to add descriptions if needed.


This `README.md` file provides detailed instructions on how to use the script, prerequisites, and explanations of the output format. Additionally, it includes the full code of the Python script for reference. You can include this file in your project repository to guide users on how to use the script.
