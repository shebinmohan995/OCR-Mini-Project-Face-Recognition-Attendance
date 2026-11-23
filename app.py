import streamlit as st
import cv2
import face_recognition as fr
import numpy as np
from datetime import datetime
import os

st.title("OCR Mini Project")
st.subheader("Face Recognition Attendance System")

# Load known image
img_path = r'C:\Users\My Lap\OneDrive\Documents\MLWORK2\DL\ANN\Attendance\Walter white.jpg'

classname = [os.path.basename(img_path).split('.')[0]]

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

known_code = fr.face_encodings(img)[0]

# Camera
picture = st.camera_input("Capture your face")

if picture is not None:

    frame = cv2.imdecode(
        np.frombuffer(picture.getvalue(), np.uint8),
        cv2.IMREAD_COLOR
    )

    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_loc = fr.face_locations(img1)
    face_code = fr.face_encodings(img1, face_loc)

    for loc, encode in zip(face_loc, face_code):

        face_dis = fr.face_distance([known_code], encode)
        match = fr.compare_faces([known_code], encode)

        if match[0] == True and face_dis[0] < 0.45:

            name = classname[0]
            color = (0, 255, 0)

            st.success("Attendance Marked")

            st.write("Name:", name)
            st.write("Date & Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        else:

            name = "Unknown"
            color = (0, 0, 255)

            st.error("Not Recognized")

        y1, x2, y2, x1 = loc

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)

        cv2.putText(
            frame, name, (x1, y1-10),
            cv2.FONT_HERSHEY_COMPLEX, 1, color, 2
        )

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    st.image(frame)