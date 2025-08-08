# Tkinter Digital Clock

A simple digital clock GUI application built using Python's **Tkinter** and **time** modules.  
It shows the current time, day, and a relevant greeting (Good Morning/Afternoon/Evening/Night) based on the time of day.

---

## Features
- **Live Time Display:** Shows the current hour, minute, and second.  
- **Day Indicator:** Displays the current day (Mon, Tue, etc.).  
- **Greeting Message:** Automatically updates with a suitable greeting according to the current time.  
- **Stylish UI:** Custom fonts and colors for better visual appeal.

---

## How It Works
- Uses Tkinter for the GUI.  
- Fetches the current time and day using the `time` module.  
- Updates the display every second.

---

## Usage
1. Clone or copy the code.  
2. Make sure you have Python installed.  
3. Run the file:
   ```bash
   python clock.py
4. The clock window will open, showing time, day, and greeting.

## Code Highlights
- The my_clock() function updates the time and day labels every second.
- The what_to_say() function sets the greeting message based on the current hour.

## Requirements
- Python 3.x
- Uses only standard library modules (tkinter, time)