from flask import Flask, request, jsonify, render_template
import pandas as pd
import os
from datetime import datetime, timedelta

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home route to serve the HTML
@app.route('/')
def index():
    return render_template('index.html')

# Route for uploading CSV file
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "message": "No file selected"})
    
    if file and file.filename.endswith('.csv'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv')
        file.save(file_path)
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Invalid file type"})

# Route to generate the timetable
@app.route('/generate-timetable', methods=['GET'])
def generate_timetable():
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv')
    if not os.path.exists(file_path):
        return jsonify({"success": False, "message": "No file uploaded"})
    
    data = pd.read_csv(file_path)
    timetable = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    start_time = datetime.strptime("08:00", "%H:%M")
    end_time = datetime.strptime("18:00", "%H:%M")
    time_increment = timedelta(hours=1)

    sections = data["SECTION"].unique()
    for section in sections:
        section_schedule = {"section": section, "schedule": []}
        section_data = data[data["SECTION"] == section]

        day_index = 0
        current_time = start_time
        for _, row in section_data.iterrows():
            subject_time = int(row["SUBJECT TIME PER WEEK"]) // 4

            for _ in range(subject_time):
                if current_time + time_increment > end_time:
                    day_index += 1
                    current_time = start_time
                    if day_index >= len(days):
                        break
                
                end_time_str = (current_time + time_increment).strftime("%H:%M")
                section_schedule["schedule"].append({
                    "day": days[day_index],
                    "time": f"{current_time.strftime('%H:%M')} - {end_time_str}",
                    "subject": row["SUBJECT"],
                    "faculty": row["FACULTY"],
                    "section": section
                })
                
                current_time += time_increment
            
            if day_index >= len(days):
                break
        
        timetable.append(section_schedule)

    return jsonify({"success": True, "timetable": timetable})

if __name__ == '__main__':
    app.run(debug=True)
