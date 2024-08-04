# facial-emotion-detection-using-opencv

This project is a Python-based application that captures images using the device's webcam and detects facial emotions using a pre-trained model from the `fer` package.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)

## Features

- Real-time facial emotion detection using a webcam.
- Displays bounding boxes around faces with the detected emotion and confidence score.

## Prerequisites

- Python 3.7+
- OpenCV
- TensorFlow
- `fer` package (Facial Expression Recognition)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/hija-happy/facial-emotion-detection-using-opencv.git
    cd facial-emotion-detection-using-opencv
    ```

2. Install the required libraries:
    ```bash
     pip install opencv-python-headless numpy tensorflow fer
    ```

## Running the Application

1. Ensure your webcam is connected and working.
2. Run the application:
    ```bash
    python emotion_detection.py
    ```

## Usage

- The application will open a window displaying the webcam feed.
- It will detect faces in real-time and draw bounding boxes around them.
- The detected emotion and its confidence score will be displayed above each face.
- Press the 'q' key to exit the application.

