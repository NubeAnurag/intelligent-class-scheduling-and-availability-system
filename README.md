# Intelligent Class Scheduling System

## Project Overview
This project is a web-based intelligent class scheduling system designed to simplify the process of creating and managing academic timetables. Users upload CSV files with faculty and subject information, which are then processed to generate a weekly timetable displayed in an organized table format.

## Features
- **File Upload**: Upload a CSV file containing subject, faculty, and section information.
- **Timetable Generation**: Automatically generate a timetable based on the uploaded file.
- **Display**: View the generated schedule in a table format.
- **User Interface**: Simple, intuitive interface for file uploads and timetable generation.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python with Flask
- **Data Processing**: Pandas for CSV data handling
- **AJAX**: For client-server interaction

## Folder Structure
```plaintext
project-root/
├── uploads/                    # Directory to store uploaded CSV files
├── templates/
│   └── index.html              # HTML for the main interface
├── static/
│   └── script.js               # JavaScript for frontend interaction
├── app.py                      # Main Flask application
└── README.md                   # Project documentation (this file)



