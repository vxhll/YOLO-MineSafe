# 🚨 YOLO-MineSafe

> **AI-powered vision-based abnormal fall detection and emergency alert framework for isolated mining workers using YOLO, Flask, and OpenCV.**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![YOLO](https://img.shields.io/badge/YOLOv8-Computer_Vision-red)
![Research](https://img.shields.io/badge/Research-Published-success)

---

# 📖 Overview

YOLO-MineSafe is an AI-powered computer vision system developed to detect abnormal fall events involving isolated mining workers in real time. The application processes live video streams using a YOLO-based detection model and automatically generates emergency alerts when a fall is detected.

The primary objective of this project is to improve worker safety, reduce emergency response time, and provide continuous monitoring without requiring wearable devices.

---

# ✨ Features

* 🎯 Real-time AI-powered fall detection
* 📹 Vision-based monitoring without wearable devices
* 🚨 Automated emergency alert generation
* 📧 Email notification with captured evidence
* 🌐 Flask-based web application
* 🖼️ Automatic image capture on detection
* 🔊 Audio alert support
* 👤 Admin and user management modules
* ⛏️ Designed for mining safety applications

---

# 🛠️ Technology Stack

* Python
* Flask
* OpenCV
* YOLO
* PyTorch
* HTML
* CSS
* JavaScript
* SQLite

---

# 🏗️ System Architecture

The following diagram illustrates the complete workflow of the YOLO-MineSafe system.

![System Architecture](docs/architecture.png)

---

# 📸 Application Screenshots

## 🏠 Home Page

Landing page of the YOLO-MineSafe web application.

![Home Page](docs/Home%20page%20.png)

---

## 🔐 Admin Login

Administrator authentication interface for secure system access.

![Admin Login](docs/Admin%20Login.png)

---

## 👤 New User Registration

Registration page for adding new users to the platform.

![New User Registration](docs/New%20User%20Login.png)

---

## 🎯 Real-Time Fall Detection

Live YOLO inference demonstrating fall detection in real time.

![Real-Time Detection](docs/Real%20time%20detection%20and%20interence%20output.png)

---

## 📧 Automated Email Alert

Automatic email notification generated immediately after a fall event is detected.

![Email Alert](docs/Automated%20Email%20alert%20and%20documentation.png)

---

# 📂 Project Structure

```text
YOLO-MineSafe/
│
├── app.py
├── Fall.py
├── NewTra.py
├── templates/
├── static/
├── docs/
├── requirements.txt
└── .gitignore
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/vxhll/YOLO-MineSafe.git
cd YOLO-MineSafe
```

Create and activate a virtual environment:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

# 📄 Research Publication

**Title:**
**YOLO-MineSafe: A Vision-Based Abnormal Fall Detection and Emergency Alert Framework for Isolated Mining Workers**

* 📚 Published in **IJSART (International Journal for Science and Advance Research in Technology)**
* 📅 Volume 12, Issue 4
* 🗓️ April 2026

This repository contains the implementation corresponding to the published research work.

---

# 🏆 Key Highlights

* ✅ AI-powered real-time fall detection
* ✅ Mining worker safety monitoring
* ✅ Automated emergency email notifications
* ✅ Flask-based web dashboard
* ✅ Image capture and event logging
* ✅ Computer vision–driven surveillance solution

---

# 🔮 Future Enhancements

* 📱 Mobile application integration
* ☁️ Cloud deployment
* 📡 Multi-camera monitoring
* 📍 GPS-based emergency response
* 📊 Analytics dashboard
* 📲 SMS and push notifications

---

# 👨‍💻 Author

**Vishal J**

AI & Data Science Student | Computer Vision Enthusiast | Full-Stack Developer

GitHub: https://github.com/vxhll

---

## 📚 Citation

If you use this project in research or academic work, please cite:

**YOLO-MineSafe: A Vision-Based Abnormal Fall Detection and Emergency Alert Framework for Isolated Mining Workers**

Published in **IJSART**, Volume 12, Issue 4 (April 2026).


## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
