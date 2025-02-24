#!/usr/bin/env python
import phonenumbers
from phonenumbers import timezone, carrier, geocoder

def track_phone_number():
    try:
        number = input("Enter phone number with country code (e.g., +91XXXXXXXXXX): ").strip()
        phone = phonenumbers.parse(number)

        if not phonenumbers.is_valid_number(phone):
            print("❌ Invalid phone number. Please check the input.")
            return
        
        time_zones = timezone.time_zones_for_number(phone)
        carrier_name = carrier.name_for_number(phone, 'en')
        region = geocoder.description_for_number(phone, 'en')

        print("\n📞 Phone Number Information:")
        print(f"✔ Country Code: {phone.country_code}")
        print(f"✔ National Number: {phone.national_number}")
        print(f"✔ Time Zone(s): {', '.join(time_zones) if time_zones else 'Unknown'}")
        print(f"✔ Carrier: {carrier_name if carrier_name else 'Unknown'}")
        print(f"✔ Country/Region: {region if region else 'Unknown'}")

    except Exception as e:
        print(f"⚠ Error: {e}")

if __name__ == "__main__":
    track_phone_number()
