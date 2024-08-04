import cv2
import numpy as np
from fer import FER

# Initialize the emotion detector
detector = FER(mtcnn=True)

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotions in the frame
    results = detector.detect_emotions(frame)

    for result in results:
        # Get bounding box coordinates
        x, y, w, h = result["box"]

        # Get the dominant emotion and its score
        emotion, score = max(result["emotions"].items(), key=lambda item: item[1])

        # Draw the bounding box and label on the frame
        cv2.putText(frame, f"{emotion} ({score:.2f})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Facial Emotion Detection', frame)

    # Check if the 'q' key is pressed or the window is closed
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Facial Emotion Detection', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()