// Handle file upload with confirmation popup
document.getElementById("uploadButton").addEventListener("click", () => {
    const fileInput = document.getElementById("fileInput").files[0];
    if (!fileInput) {
        alert("Please select a file first!");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput);

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("File uploaded successfully!");
        } else {
            alert(data.message || "Upload failed.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while uploading.");
    });
});

// Generate timetable and display in table format
document.getElementById("generateButton").addEventListener("click", () => {
    fetch("/generate-timetable")
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                displayTimetable(data.timetable);
            } else {
                alert(data.message || "Failed to generate timetable.");
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred during timetable generation.");
        });
});

function displayTimetable(timetable) {
    const resultDiv = document.getElementById("timetableResult");
    resultDiv.innerHTML = ""; // Clear any previous results

    timetable.forEach(sectionData => {
        const table = document.createElement("table");
        const header = `<tr><th>Day</th><th>Time</th><th>Subject</th><th>Faculty</th><th>Section</th></tr>`;
        table.innerHTML = header;

        sectionData.schedule.forEach(entry => {
            const row = `<tr>
                <td>${entry.day}</td>
                <td>${entry.time}</td>
                <td>${entry.subject}</td>
                <td>${entry.faculty}</td>
                <td>${entry.section}</td>
            </tr>`;
            table.innerHTML += row;
        });

        resultDiv.appendChild(table);
    });
}
