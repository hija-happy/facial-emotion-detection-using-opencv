# Facial Emotion Detection 

This project is a Python-based application that captures video from the webcam and detects facial emotions using a pre-trained model from the `fer` package. Detected emotions are displayed on the video feed with bounding boxes and confidence scores. Additionally, the video frames are shown using the Pillow library.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)

## Features

- Real-time facial emotion detection using a webcam.
- Displays bounding boxes around detected faces with the dominant emotion and confidence score.
- Converts frames to PIL images and displays them.

## Prerequisites

- Python 3.7+
- OpenCV
- `fer` package (Facial Expression Recognition)
- Pillow

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/hija-happy/facial-emotion-detection-using-opencv.git
    cd facial-emotion-detection-using-opencv
    ```

2. Create a virtual environment (optional):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required libraries:
    ```bash
    pip install opencv-python-headless numpy fer pillow
    ```

## Running the Application

1. Ensure your webcam is connected and working.
2. Run the application:
    ```bash
    python emotion_detection.py
    ```

## Usage

- The application will open a video feed window from your webcam.
- It will detect faces in real-time and draw bounding boxes around them.
- The detected emotion and its confidence score will be displayed above each face.
- Additionally, the frames will be converted to PIL images and displayed.
- Press the 'q' key to exit the application.

## Notes

- Ensure that your webcam is properly connected and configured.
- The Pillow image display (`pil_image.show()`) may open a new window for each frame. This can be modified or disabled based on your requirements.
- The `fer` library handles emotion detection using pre-trained models, and it may internally use TensorFlow or other frameworks.

