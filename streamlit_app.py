import streamlit as st
import cv2
from src.main import detector, tracker, pose_estimator, recorder
import time

st.title("📘 Exam Cheating Detection – Streamlit Version")
st.write("This application detects cheating behaviors like looking around or using a phone.")

run = st.checkbox("Start Detection")

FRAME_WINDOW = st.image([])

cap = None

if run:
    cap = cv2.VideoCapture(0)
    st.write("Camera started.")
else:
    st.write("Click the checkbox above to start.")
    
while run:
    ret, frame = cap.read()
    if not ret:
        st.write("Camera not detected.")
        break
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # ---- Insert your detection pipeline here ----
    # You can call your functions from main.py or write a shorter pipeline.

    FRAME_WINDOW.image(frame)
