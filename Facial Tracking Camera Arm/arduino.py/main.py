import cv2
import serial
import time

PORT_SERIAL = 'COM8'  # Set port to 8
BAUD_RATE = 9600

try:
    # Initialize connection
    arduino = serial.Serial(PORT_SERIAL, BAUD_RATE, timeout=1)

    # Wait for Arduino to reset after connection
    time.sleep(2)

    print(f"Successfully connected to {PORT_SERIAL}")
except Exception as e:
    print(f"ERROR: Could not connect to {PORT_SERIAL}.")
    exit()

# Load facial detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

print("Program started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the image
    frame = cv2.flip(frame, 1)

    # Convert image to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    img_h, img_w = frame.shape[:2]
    center_x = img_w // 2
    center_y = img_h // 2

    # Draw the center of the screen
    cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

    for (x, y, w, h) in faces:
        # Calculate the center of the detected face
        face_center_x = x + w // 2
        face_center_y = y + h // 2

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.circle(frame, (face_center_x, face_center_y), 5, (255, 0, 0), -1)

        # Tolerance (pixels)
        tol = 60

        # Command sending logic
        try:
            # Y-Axis - Servo
            if face_center_y < center_y - tol:
                arduino.write(b'U')  # Up
            elif face_center_y > center_y + tol:
                arduino.write(b'D')  # Down

            # X-Axis - Stepper
            if face_center_x < center_x - tol:
                arduino.write(b'L')  # Left
            elif face_center_x > center_x + tol:
                arduino.write(b'R')  # Right

        except Exception as e:
            print(f"Error sending data: {e}")
            break

    # Display the window
    cv2.imshow('Facial Tracking - Arduino COM8', frame)

    # Exit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup resources
cap.release()
cv2.destroyAllWindows()

if 'arduino' in locals():
    arduino.close()
    print("Serial connection closed.")