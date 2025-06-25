# Citizen Safety using Face Recognition

A real-time face recognition system designed to enhance citizen safety by identifying known individuals and logging detected faces. Built with Python, OpenCV, and face-recognition for live analysis.

---

## 🚀 Features

- **Real-time Face Detection & Recognition**  
  Utilizes live webcam feed to detect faces and recognize known individuals from a pre-registered dataset.

- **Face Dataset Management**  
  Organize and manage registered user images in the `dataset/` folder (one subfolder per individual).

- **Face Encodings**  
  Encodes known faces once and caches them for faster performance in repeated runs.

- **Detection Logging**  
  Logs detection events with timestamped CSV entries, aiding in audit trails and safety tracking.

---

## 🛠️ Tech Stack

- **Python 3.x**  
- **OpenCV** – For image processing and face detection (`haarcascade_frontalface_default.xml`).  
- **face-recognition** – For face encoding and recognition.  
- **NumPy, PIL** – Supporting libraries for image handling.

---

## 📂 Project Structure

