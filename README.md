<p><a target="_blank" href="https://app.eraser.io/workspace/anYrqassWvwDxK5i8Thm" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# Text to Google Calendar CSV Converter - Retail Calendar
This Python script converts a text file containing events to a Google Calendar compatible CSV format.

## Prerequisites
- Python 3.x
- Input text file containing events (e.g., `events.txt` )
## Installation
1. Clone this repository or download the `txt_to_csv_converter.py`  file.
2. Ensure you have Python installed on your system.
## Usage
1. Prepare your input text file (`events.txt` ) with events listed in the following format:
```bash
Date,Event
January 1,New Year’s Day
January 1 - 31,Dry January, Ginuary, Veganuary
```
Each event should be on a separate line, and if an event spans multiple days, use a hyphen to indicate the range.

1. Run the Python script `txt_to_csv_converter.py`  by executing the following command in your terminal or command prompt:
```bash
python txt_to_csv_converter.py
```
1. Follow the prompts to provide the path for the input text file (`events.txt` ) and the desired path for the output CSV file.
2. The script will convert the events from the text file to a CSV file compatible with Google Calendar.
## Output
The script generates a CSV file named `events.csv` containing the events in the following format:

```bash
Subject,Start Date,Start Time,End Date,End Time,Description
New Year’s Day,2024-01-01,,2024-01-01,,""
Dry January,2024-01-01,,2024-01-31,,"Ginuary, Veganuary"
```
## Notes
- Ensure that the events in the input text file are formatted correctly to ensure proper conversion.
- Special cases such as date ranges or events spanning multiple days are handled appropriately.
- The script does not include event descriptions by default. You can modify the script to add descriptions if needed.
This `README.md` file provides detailed instructions on how to use the script, prerequisites, and explanations of the output format. Additionally, it includes the full code of the Python script for reference. You can include this file in your project repository to guide users on how to use the script.


<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Text to Google Calendar CSV Converter Architecture-1.eraserdiagram" data-element-id="iItwQoNKVJlFR_1o7Nad9"><img src="/.eraser/anYrqassWvwDxK5i8Thm___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----8d29172fed82262b0b3702582912298b-Text-to-Google-Calendar-CSV-Converter-Architecture.png" alt="" data-element-id="iItwQoNKVJlFR_1o7Nad9" /></a>
<a href="/README-Text to Google Calendar CSV Converter Retail Calendar-2.eraserdiagram" data-element-id="QYRYHAQHyjTnHqE6RZsnl"><img src="/.eraser/anYrqassWvwDxK5i8Thm___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----b6bfff32a7a3405c1d75cbd371cb057c-Text-to-Google-Calendar-CSV-Converter-Retail-Calendar.png" alt="" data-element-id="QYRYHAQHyjTnHqE6RZsnl" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/anYrqassWvwDxK5i8Thm --->