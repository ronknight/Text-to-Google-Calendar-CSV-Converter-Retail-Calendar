from datetime import datetime

def txt_to_ical_with_notifications(input_file, output_file):
    """
    Convert a tab-delimited text file containing events to iCal (.ics) format,
    creating separate events for the actual event date and notification date.

    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to save the output iCal file.

    Returns:
        None
    """
    # Read the lines from the input text file
    with open(input_file, 'r') as txt_file:
        # Read the file as tab-delimited
        lines = txt_file.readlines()
        # Skip the header row
        lines = lines[1:]

    # Initialize a list for iCal events
    ical_events = []

    # Define the iCal header and footer
    ical_header = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n"
    ical_footer = "END:VCALENDAR\n"

    # Process each line and create events
    for line in lines:
        if line.strip():
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                notification_date = parts[0].strip()
                event_date = parts[1].strip()
                event_name = parts[2].strip()

                try:
                    # Parse notification date
                    notification_date_parsed = datetime.strptime(notification_date, "%d-%b-%Y").strftime("%Y%m%d")
                    # Parse event date
                    event_date_parsed = datetime.strptime(event_date, "%d-%b-%Y").strftime("%Y%m%d")
                except ValueError as e:
                    print(f"Error parsing dates: {e}")
                    continue

                # Create the main event
                main_event_uid = f"{event_name.replace(' ', '_')}_{event_date_parsed}@example.com"
                main_event = (
                    "BEGIN:VEVENT\n"
                    f"SUMMARY:{event_name}\n"
                    f"DTSTART;VALUE=DATE:{event_date_parsed}\n"
                    f"DTEND;VALUE=DATE:{event_date_parsed}\n"
                    f"DESCRIPTION:Event Date: {event_date}\n"
                    f"UID:{main_event_uid}\n"
                    "STATUS:CONFIRMED\n"
                    "END:VEVENT\n"
                )
                ical_events.append(main_event)

                # Create the notification event
                notification_event_uid = f"Notification_{event_name.replace(' ', '_')}_{notification_date_parsed}@example.com"
                notification_event = (
                    "BEGIN:VEVENT\n"
                    f"SUMMARY:Notification for {event_name}\n"
                    f"DTSTART;VALUE=DATE:{notification_date_parsed}\n"
                    f"DTEND;VALUE=DATE:{notification_date_parsed}\n"
                    f"DESCRIPTION:Reminder for event: {event_name} on {event_date}\n"
                    f"UID:{notification_event_uid}\n"
                    "STATUS:CONFIRMED\n"
                    "END:VEVENT\n"
                )
                ical_events.append(notification_event)

    # Write the iCal file
    with open(output_file, 'w') as ical_file:
        ical_file.write(ical_header)
        ical_file.writelines(ical_events)
        ical_file.write(ical_footer)

    print(f"iCal file successfully created at {output_file}")


if __name__ == "__main__":
    # Input and output file paths
    input_file = "retail-calendar-2025-final.txt"  # Path to the input text file
    output_file = "events_with_notifications.ics"  # Path to the output iCal file

    # Convert the text file to iCal format
    txt_to_ical_with_notifications(input_file, output_file)
