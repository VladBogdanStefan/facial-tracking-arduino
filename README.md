# Facial Tracking Camera Arm

A hardware-software system designed to automatically detect and track human faces in real-time using a webcam, Python scripts, and an Arduino microcontroller. The project mechanically adjusts the camera's position across two axes (X and Y) to keep the user's face centered in the frame.

## 🚀 Key Features

* **Computer Vision:** Fast and accurate facial detection using **OpenCV** and a pre-trained Haar Cascade classifier.
* **2-Axis Control (Pan & Tilt):** 
  * The X-axis (Left/Right) is controlled by a **Stepper motor** for smooth rotational movement.
  * The Y-axis (Up/Down) is controlled by a **Servo motor** for angle adjustment (tilt).
* **Serial Communication (UART):** Efficient transmission of directional commands ('U', 'D', 'L', 'R') from the Python script to the Arduino microcontroller via USB using **PySerial**.
* **Tolerance Filter (Deadzone):** Implementation of a central deadzone to prevent continuous mechanical jittering and stabilize the camera arm.

## 🛠️ Technologies & Hardware

* **Software:** Python 3, OpenCV (`cv2`), PySerial.
* **Hardware:** Arduino Board, Webcam, Servo Motor, Stepper Motor.
* **Algorithms:** `haarcascade_frontalface_default.xml` for pattern recognition.

## ⚙️ How it Works

1. The Python script captures the video feed from the webcam, flips the image horizontally for natural movement, and converts it to grayscale to optimize detection performance.
2. The `detectMultiScale` function finds the face coordinates and calculates its center.
3. The face's center is compared to the absolute center of the video frame. 
4. If the face moves outside a predefined tolerance box (e.g., a 60-pixel radius), Python sends a command byte over the serial port to the Arduino.
5. The Arduino reads the command and actuates the motors to correct the physical angle of the camera.

## 💻 How to Run (Installation)

1. **Hardware Setup:**
   * Connect the Arduino board to your PC.
   * Open the Arduino IDE, compile, and upload the `.ino` source code to the board.
   * Note the port your Arduino is connected to (e.g., `COM8`). *Make sure to close the Serial Monitor window in the Arduino IDE!*

2. **Software Setup (Python):**
   * Install the required dependencies by running the following command in your terminal:
     ```bash
     pip install opencv-python pyserial
     ```
   * Open the Python script and update the `PORT_SERIAL` variable with your specific port (e.g., `'COM8'`).
   * Run the script. To stop the program, press the **'q'** key while the video window is active.
