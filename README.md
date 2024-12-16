<h1 align="center">🗓️ <a href="https://github.com/ronknight/Text-to-Google-Calendar-CSV-Converter-Retail-Calendar">Text to Google Calendar CSV/ICS Converter</a></h1>

<h4 align="center">🔧 A Python-based system that converts retail event calendars (tab-delimited text files) into Google Calendar-compatible ICS files with notifications for both major and minor events.</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
<a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/Text-to-Google-Calendar-CSV-Converter-Retail-Calendar/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/Text-to-Google-Calendar-CSV-Converter-Retail-Calendar/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Love-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#project-overview">Project Overview</a> •
  <a href="#files">Files</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#visualization">Visualization</a> •
  <a href="#disclaimer">Disclaimer</a>
</p>

---

## 📋 Project Overview

This project provides tools to convert tab-delimited retail event calendar text files into **Google Calendar ICS files**. It distinguishes between **major events** and **minor events**, categorizing them and generating notifications ahead of event dates.

**Features**:
- Generates separate ICS files for **major** and **minor events**.
- Creates **notification reminders** 1-3 months in advance for major events.
- Handles input files in **tab-delimited text format**.

---

## 📁 Files

| File Name                         | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| `txt_to_ics_converter_internal.py` | Converts text files into **separate ICS files** for major and minor events. |
| `txt_to_ics_converter_external.py` | Creates **ICS files with notifications** for each event.                    |

---

## 🛠️ Installation

To set up this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/ronknight/Text-to-Google-Calendar-CSV-Converter-Retail-Calendar.git
   cd Text-to-Google-Calendar-CSV-Converter-Retail-Calendar
   ```

2. Install dependencies:
   ```bash
   pip install python-dateutil
   ```

---

## 🚀 Usage

### **1. Generating ICS Files for Major and Minor Events**

Use the `txt_to_ics_converter_internal.py` script:

```bash
python txt_to_ics_converter_internal.py
```

- Input file: `retail-calendar-2025-final.txt`
- Outputs:
  - `major_events.ics` (Major events)
  - `minor_events.ics` (Minor events)

### **2. Generating ICS Files with Notifications**

Use the `txt_to_ics_converter_external.py` script:

```bash
python txt_to_ics_converter_external.py
```

- Input file: `retail-calendar-2025-final.txt`
- Output:
  - `events_with_notifications.ics` (ICS file with notifications for events)

---

## 📊 Visualization

### Workflow for `txt_to_ics_converter_internal.py`:

```mermaid
graph TD
A[Input: Retail Calendar Text File] --> B[Read Events and Categorize]
B -->|Major Events| C[Generate Major ICS File]
B -->|Minor Events| D[Generate Minor ICS File]
C --> E[Save as major_events.ics]
D --> F[Save as minor_events.ics]
```

### Workflow for `txt_to_ics_converter_external.py`:

```mermaid
graph TD
A[Input: Retail Calendar Text File] --> B[Parse Event and Notification Dates]
B --> C[Generate Main Event in ICS Format]
B --> D[Generate Notification Event in ICS Format]
C --> E[Save to events_with_notifications.ics]
D --> E
```

---

## ⚠️ Disclaimer

This project processes date-sensitive retail calendars and generates notification files. Ensure that the input text files are correctly formatted. Always validate generated ICS files before importing them into calendar applications.