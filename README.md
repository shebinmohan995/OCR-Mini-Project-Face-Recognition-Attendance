Face Recognition Attendance System

A Python-based mini project that uses real-time face recognition through a webcam to identify a person and automatically mark their attendance with the date and time.

Features

- Real-time face detection using webcam
- Face recognition using "face_recognition"
- Green rectangle when a known face is recognized
- Displays the recognized person's name
- Displays Attendance Marked when recognition is successful
- Automatically records date and time
- Saves attendance in a CSV file

Technologies Used

- Python
- OpenCV
- face_recognition
- NumPy
- CSV
- Datetime

How It Works

1. Loads a reference image of a known person.
2. Extracts the face encoding from the reference image.
3. Captures live frames from the webcam.
4. Detects faces in the webcam frame.
5. Extracts face encodings from detected faces.
6. Compares the live face with the reference face.
7. If a match is found, displays the name and marks attendance with date and time.

Requirements

Install the required libraries:

pip install opencv-python
pip install face-recognition
pip install numpy

Project Output

When a known face is recognized, the system displays the person's name, a green bounding box and an attendance confirmation. The attendance is recorded with the date and time in a CSV file.

Project Type

Deep Learning / Computer Vision Mini Project
