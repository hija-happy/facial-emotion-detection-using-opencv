# Facial Emotion Detection 

This project is a Python-based application that captures video from the webcam and detects facial emotions using a pre-trained model from the `fer` package. Detected emotions are displayed on the video feed with bounding boxes and confidence scores.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Notes](#notes)

## Features

- Real-time facial emotion detection using a webcam.
- Displays bounding boxes around detected faces with the dominant emotion and confidence score.

## Prerequisites

- Python 3.7+
- OpenCV
- `fer` package (Facial Expression Recognition)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/hija-happy/facial-emotion-detection-using-opencv.git
    cd facial-emotion-detection-using-opencv
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required libraries:
    ```bash
    pip install opencv-python-headless numpy fer
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
- Press the 'q' key to exit the application.

## Notes

- Ensure that your webcam is properly connected and configured.
- The application uses the `fer` package for emotion detection and OpenCV for video capture and processing.
- TensorFlow is a dependency of the `fer` package, even though it is not directly used in this application. It is required for the emotion detection functionality.
