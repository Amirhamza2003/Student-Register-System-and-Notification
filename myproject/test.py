import json
import time
import pywhatkit
import os

# Path to the JSON file
json_file_path = os.path.join('data', 'contacts.json')

# Load contacts from the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)
    contacts = data.get('contacts', [])

# Delay to ensure messages are sent one after the other
delay = 20  # seconds

# Iterate over each contact and send the message
for contact in contacts:
    phone_number = contact.get('phone_number')
    message = contact.get('message')
    
    try:
        # Send message
        pywhatkit.sendwhatmsg_instantly(
            phone_number, 
            message, 
            wait_time=15,  # Adjust as necessary
            tab_close=True, 
            close_time=3
        )
        print(f"Message sent to {phone_number}")
        
        # Wait before sending the next message
        time.sleep(delay)
    
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")
