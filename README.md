Intelligent Class Scheduling System
Project Overview
This project is a web-based intelligent class scheduling system designed to simplify the process of creating and managing academic timetables for different sections. It enables faculty members and administrators to upload CSV data files containing faculty and subject information, which the system then uses to generate a complete weekly schedule based on available time slots and specified teaching hours per subject. The generated schedule is displayed in an organized table format.
Features
File Upload: Upload a CSV file containing subject, faculty, and section information.
Timetable Generation: Automatically generate a timetable based on the uploaded file.
Display: View the generated schedule in a clean, tabular format for easy reference.
User Interface: Simple, intuitive web interface for file uploads and timetable generation.
Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python with Flask
Data Handling: Pandas for CSV data processing
How It Works
Data Upload: The CSV file is uploaded through the client interface and saved on the server.
Timetable Generation:
Data is read and processed using Pandas.
Based on the available time slots and the specified weekly teaching hours, a timetable is generated for each section.
Subjects are allocated in hourly slots between 8:00 AM and 6:00 PM from Monday to Saturday.
Display: The generated timetable is returned to the frontend and displayed in a table format.
Future Improvements
Conflict Management: Detect and handle scheduling conflicts.
Customization: Allow customization of time slots, working days, and hours.
Downloadable Timetable: Enable the timetable to be downloaded as a PDF or CSV file.
Author
Anurag Mandal

