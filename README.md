Student-Register-System-and-Notification
This mini-project, Student Register System and Notification, is designed to streamline the process of tracking student attendance and sending real-time notifications to parents via WhatsApp. The system allows teachers to mark attendance and automatically send a message to parents if their child is absent from school.

Project Overview
The project is built using Django, a high-level Python web framework, and integrates with the pywhatkit library to send WhatsApp messages. The system maintains a register of students, allows teachers to mark attendance, and generates notifications that are sent directly to the parents' WhatsApp numbers.

Key Features
Attendance Tracking: Teachers can mark students as present or absent.
Automated Notifications: Automatically send a customized message to parents when their child is marked absent.
Session Management: Uses Django’s session management to keep track of absent students and ensure the right messages are sent.
Development Environment
This project was developed using Visual Studio Code as the Integrated Development Environment (IDE).

Libraries and Dependencies
To set up and run this project, the following libraries need to be installed:
Create virtual environment to run the program
Django: The primary web framework used to develop the project.
pip install django
pywhatkit: Used for sending WhatsApp messages programmatically.
pip install pywhatkit
Logging: A Python standard library used for logging messages and errors.
pip install logging
Other dependencies:
pip install pillow  # For image handling (if required)

Clone the Repository:
git clone https://github.com/Amirhamza2003/Student-Register-System-and-Notification.git
Navigate to the Project Directory:
cd Student-Register-System-and-Notification
Install the Required Dependencies:
pip install -r requirements.txt
Run the Development Server:
python manage.py runserver

pip install requests  # For handling HTTP requests (if needed)
