# Phone Number Tracker 📞

A simple Python script to track phone numbers using the `phonenumbers` library. It provides details such as the time zone, carrier, and geographical region of a given phone number.

## Features 🚀
- Retrieves **country code** and **national number**.
- Identifies the **carrier** of the phone number.
- Fetches **time zone(s)** associated with the number.
- Displays **geographical region** (country or state).
- Includes **error handling** for invalid inputs.

## Installation 🛠️
Make sure you have Python installed on your system. Then, install the required library:

```bash
pip install phonenumbers
Usage 📌
Run the script and enter a phone number with the country code:

python phone_tracker.py
Example input:

typescript
Enter phone number with country code (e.g., +91XXXXXXXXXX): +14155552671
Example output:

📞 Phone Number Information:
✔ Country Code: 1
✔ National Number: 4155552671
✔ Time Zone(s): America/Los_Angeles
✔ Carrier: AT&T
✔ Country/Region: United States
Requirements 📋
Python 3.x
phonenumbers library
License 📜
This project is licensed under the MIT License.
