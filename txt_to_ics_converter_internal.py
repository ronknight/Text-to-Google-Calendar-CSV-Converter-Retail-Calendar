from datetime import datetime
from dateutil.relativedelta import relativedelta

def categorize_event(event_name, minor_events, major_events):
    """
    Categorize the event as major or minor and get its related category.
    """
    if event_name in minor_events:
        return "minor", minor_events[event_name]
    elif event_name in major_events:
        return "major", major_events[event_name]
    else:
        raise ValueError(f"No category found for event: {event_name}")

def create_ical_file(events, output_file):
    """
    Create an iCal (.ics) file from a list of events.

    Args:
        events (list): List of events where each event is a dictionary with event details.
        output_file (str): Path to save the output iCal file.
    """
    ical_header = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n"
    ical_footer = "END:VCALENDAR\n"

    with open(output_file, 'w') as ical_file:
        ical_file.write(ical_header)
        for event in events:
            ical_file.write(
                "BEGIN:VEVENT\n"
                f"SUMMARY:{event['summary']}\n"
                f"DTSTART;VALUE=DATE:{event['start_date']}\n"
                f"DTEND;VALUE=DATE:{event['end_date']}\n"
                f"DESCRIPTION:{event.get('description', '')}\n"
                f"UID:{event['uid']}\n"
                "STATUS:CONFIRMED\n"
                "END:VEVENT\n"
            )
        ical_file.write(ical_footer)

    print(f"iCal file successfully created at {output_file}")

def txt_to_ical_separate(input_file, major_output_file, minor_output_file):
    """
    Convert a tab-delimited text file containing events to separate iCal (.ics) files for major and minor events.

    Args:
        input_file (str): Path to the input text file.
        major_output_file (str): Path to save the output iCal file for major events.
        minor_output_file (str): Path to save the output iCal file for minor events.

    Returns:
        None
    """
    # Define all major events and their related categories
    major_events = {
        "New Year's Day": "Holiday Decorations & Gifts",
        "Valentine's Day": "Seasonal Gifts & Party Supplies",
        "Good Friday": "Religious Observances",
        "Easter Sunday": "Seasonal Celebrations & Gifts",
        "Mother's Day": "Gifts & Home Decor",
        "Memorial Day": "Patriotic Items & Outdoor Goods",
        "Father's Day": "Gifts & Tools",
        "Independence Day": "Patriotic Items & Decorations",
        "Halloween": "Costumes & Party Supplies",
        "Thanksgiving (US)": "Kitchenware & Seasonal Goods",
        "Christmas Day": "Holiday Decorations & Gifts",
        "New Year's Eve": "Party Supplies & Gifts",
        "First Day of Spring": "Seasonal Items",
        "First Day of Summer": "Seasonal Items",
        "Black Friday": "Sales & Promotions",
        "First Day of Winter": "Seasonal Items",
        "Labor Day": "Home Goods & Tools",
        "International Youth Day": "Toys & Educational Items",
        "First Day of Autumn": "Seasonal Items",
        "World AIDS Day": "Social Awareness Events",
    }

    # Define all minor events and their related categories
    minor_events = {
        "Back to School": "Stationery & Educational Items",
        "Last Day of Summer": "Seasonal Items",
        "President's Day": "Social Awareness Events",
        "National Pet Day": "Pet Supplies",
        "Star Wars Day": "Licensed Toys",
        "National Wellness Month": "Health & Wellness",
        "National Coloring Book Day": "Toys & Educational Items",
        "International Coffee Day": "Kitchenware & Beverage Supplies",
        "International Waffle Day": "Kitchenware & Bakeware",
        "National Apple Pie Day": "Kitchenware & Seasonal Baking",
        "World Fair Trade Day": "Eco-Friendly Products",
        "April Fool's Day": "Party Supplies & Fun Items",
        "National Biscuit Day": "Party Supplies & Seasonal Goods",
        "National Pizza Day": "Party Supplies & Fun Items",
        "National Cheese Day": "Kitchenware & Dairy Products",
        "World Chocolate Day": "Party Supplies & Gifts",
        "International Beer Day": "Party Supplies",
        "International Cat Day": "Pet Supplies",
        "Women's Equality Day": "Home Goods & Gifts",
        "National Eat Outside Day": "Outdoor & Seasonal Items",
        "International Day of Charity": "Home Goods & Gift Items",
        "Read a Book Day": "Toys & Educational Items",
        "International Day of Peace": "Social Awareness Events",
        "World Photography Day": "Electronics & Photography Items",
        "World Heart Day": "Health & Wellness",
        "World Animal Day": "Pet Supplies & Outdoor Items",
        "World Mental Health Day": "Social Awareness Events",
        "World Food Day": "Kitchenware & Seasonal Baking",
        "All Saints' Day": "Religious Observances",
        "Remembrance Day": "Patriotic Items",
        "Human Rights Day": "Social Awareness & Charity",
    }

    # Read the lines from the input text file
    with open(input_file, 'r') as txt_file:
        lines = txt_file.readlines()[1:]  # Skip the header row

    major_events_list = []
    minor_events_list = []

    for line in lines:
        if line.strip():
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                event_date = parts[1].strip()
                event_name = parts[2].strip()

                try:
                    event_date_parsed = datetime.strptime(event_date, "%d-%b-%Y")
                except ValueError as e:
                    print(f"Error parsing date for {event_name}: {e}")
                    continue

                # Categorize the event
                category_type, category_name = categorize_event(event_name, minor_events, major_events)
                event_list = minor_events_list if category_type == "minor" else major_events_list

                # Add main event without description
                event_list.append({
                    "summary": event_name,
                    "start_date": event_date_parsed.strftime("%Y%m%d"),
                    "end_date": event_date_parsed.strftime("%Y%m%d"),
                    "uid": f"{event_name.replace(' ', '_')}_{event_date_parsed.strftime('%Y%m%d')}@4sgm.com"
                })

                # Add notifications with descriptions
                notification_offsets = [-3, -2, -1] if category_type == "major" else [-2, -1]
                for idx, offset in enumerate(notification_offsets, start=1):
                    notification_date = event_date_parsed + relativedelta(months=offset)
                    notification_number = len(notification_offsets) - idx + 1  # Reverse order (3 -> 1)

                    description = (
                        f"Reminder for event: {event_name} on {event_date} - Category: {category_name}"
                    )

                    event_list.append({
                        "summary": f"Notification {notification_number} for {event_name}",
                        "start_date": notification_date.strftime("%Y%m%d"),
                        "end_date": notification_date.strftime("%Y%m%d"),
                        "description": description,
                        "uid": f"Notification_{notification_number}_{event_name.replace(' ', '_')}_{notification_date.strftime('%Y%m%d')}@4sgm.com"
                    })

    # Create separate iCal files
    create_ical_file(major_events_list, major_output_file)
    create_ical_file(minor_events_list, minor_output_file)

if __name__ == "__main__":
    input_file = "retail-calendar-2025-final.txt"
    major_output_file = "major_events.ics"
    minor_output_file = "minor_events.ics"

    txt_to_ical_separate(input_file, major_output_file, minor_output_file)
