
from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Intelligent Class Scheduling System", ln=True, align="C")

# Adding content to PDF
pdf.set_font("Arial", "", 12)
pdf.ln(10)
pdf.cell(0, 10, "Project Overview", ln=True)
pdf.multi_cell(0, 10, (
    "This project is a web-based intelligent class scheduling system designed to simplify the process of creating "
    "and managing academic timetables for different sections. It enables faculty members and administrators to upload "
    "CSV data files containing faculty and subject information, which the system then uses to generate a complete "
    "weekly schedule based on available time slots and specified teaching hours per subject. The generated schedule is "
    "displayed in an organized table format."
))

# Features
pdf.ln(10)
pdf.cell(0, 10, "Features", ln=True)
features = [
    "File Upload: Upload a CSV file containing subject, faculty, and section information.",
    "Timetable Generation: Automatically generate a timetable based on the uploaded file.",
    "Display: View the generated schedule in a clean, tabular format for easy reference.",
    "User Interface: Simple, intuitive web interface for file uploads and timetable generation."
]
for feature in features:
    pdf.cell(10, 10, "- " + feature, ln=True)

# Technologies Used
pdf.ln(10)
pdf.cell(0, 10, "Technologies Used", ln=True)
technologies = [
    "Frontend: HTML, CSS, JavaScript",
    "Backend: Python with Flask",
    "Data Handling: Pandas for CSV data processing",
    "Other: AJAX for client-server interaction"
]
for tech in technologies:
    pdf.cell(10, 10, "- " + tech, ln=True)

# Folder Structure
pdf.ln(10)
pdf.cell(0, 10, "Folder Structure", ln=True)
structure = (
    "project-root/\n"
    "├── uploads/                    # Directory to store uploaded CSV files\n"
    "├── templates/\n"
    "│   └── index.html              # HTML for the main interface\n"
    "├── static/\n"
    "│   └── script.js               # JavaScript for frontend interaction\n"
    "├── app.py                      # Main Flask application\n"
    "└── README.md                   # Project documentation (this file)"
)
pdf.multi_cell(0, 10, structure)

# Installation and Setup
pdf.ln(10)
pdf.cell(0, 10, "Installation and Setup", ln=True)
installation = [
    "1. Clone the repository: git clone <repository_url>",
    "2. Set up a virtual environment (optional but recommended):",
    "   python3 -m venv env",
    "   source env/bin/activate  # For Linux/macOS",
    "   env\\Scripts\\activate   # For Windows",
    "3. Install dependencies: pip install Flask pandas",
    "

