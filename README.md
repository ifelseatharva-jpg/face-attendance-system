Face Attendance System
A Python-based face recognition attendance system that works in offline mode (folder images), online mode (laptop webcam), and online mode via Android phone webcam (IP Webcam app).
It automatically detects faces, matches them with known images, and logs attendance in a CSV file.
________________________________________
Features: - Detects and recognizes faces automatically. - Three modes of operation: 1. Offline Mode: Uses images in data/known_faces folder. 2. Laptop Webcam Mode: Uses laptop webcam to capture faces in real-time. 3. Phone Webcam Mode: Uses Android phone via IP Webcam app for live streaming. - Avoids duplicate attendance entries for the same person on the same day. - Attendance is saved in data/attendance.csv in a readable format.
________________________________________
System Requirements: - Python 3.10+ recommended. - Libraries: opencv-python, numpy, pandas, face_recognition, dlib, optionally imutils. - Windows Users: Install CMake and Visual Studio Build Tools for dlib. - Linux Users: Install cmake, boost, and python3-dev for dlib.
________________________________________
Setup Instructions: 1. Clone the repository
git clone <repository_url>
cd face-attendance-system/src
2.	Install dependencies
pip install -r requirements.txt
3.	Prepare known faces
•	Place images of known people in data/known_faces/.
•	Filename (without extension) will be used as the person’s name in attendance.
•	Example:
data/known_faces/John.jpg
data/known_faces/Mehak.png
4.	Ensure attendance CSV exists
•	If data/attendance.csv does not exist, it will be created automatically.
5.	Set up phone webcam (optional)
•	Install IP Webcam on Android.
•	Start server → copy the direct video URL (e.g., http://192.168.1.6:8080/video).
•	Ensure phone and laptop are on the same Wi-Fi network.
________________________________________
Usage: Run the script:
python attendance.py
You will be prompted to choose a mode:
Choose mode:
1 - Offline (folder images)
2 - Laptop webcam
3 - Phone webcam (IP Webcam)
Mode Details: 1. Offline Mode - Scans all images in known_faces. - Marks attendance for faces detected in images. - Automatically avoids duplicates for today.
2.	Laptop Webcam Mode
o	Opens your laptop webcam.
o	Detects faces in real-time.
o	Press q to quit webcam mode.
3.	Phone Webcam Mode
o	Prompts for your phone IP Webcam URL.
o	Connects to live feed.
o	Detects faces from known images and marks attendance.
o	Press q to quit.
________________________________________
Attendance CSV Format: | Name | Date | Time | |——-|———–|———-| | John | 2026-01-14 | 13:30:25 | | Mehak | 2026-01-14 | 13:32:10 |
•	Prevents duplicate entries for the same person on the same day.
•	Automatically updates CSV for every mode.
________________________________________
Tips & Notes: - Use clear frontal images in known_faces for best recognition accuracy. - For IP Webcam: always use direct video URL (/video or /mjpeg), not the webpage URL. - Keep phone and laptop on the same Wi-Fi. - Online webcam attendance will only mark known faces. - For large numbers of images, script may take longer to recognize faces in real-time.
________________________________________
Troubleshooting: 1. Cannot install dlib - Windows: Install CMake and Visual Studio Build Tools. - Linux: Install cmake, boost, and python3-dev.
2.	Phone webcam not connecting
o	Check URL: must be http://<phone_ip>:8080/video
o	Ensure Wi-Fi connection is the same.
3.	Attendance not updating
o	Ensure filenames in known_faces exactly match names to log.
o	Script only marks recognized faces.
________________________________________
License: Open-source and free to use for personal or educational purposes.



