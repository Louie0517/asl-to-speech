# ASL to Speech 🤟🎙️

A Computer Vision project that converts **American Sign Language (ASL)** hand gestures captured via webcam into **text** and **spoken words** using YOLO, OpenCV, and Text-to-Speech (TTS) technology.

---

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Features
- Detects ASL hand gestures in real-time using a webcam.
- Converts detected gestures into **text**.
- Speaks the detected text aloud using **Text-to-Speech**.
- Flip camera for mirror view.
- Add spaces and delete characters from sentence buffer.
- Press **Shift (`S`)** to confirm a detected letter into the buffer.
- Press **Enter** to read the sentence aloud.

---

## Demo

<p align="center">
  <img src="assets/demo.gif" alt="ASL to Speech Demo">
</p>

> Note: Short demo video displayed as GIF. For longer demos, link to external video.

---

## Requirements

- Python 3.8+
- OpenCV (`opencv-python`)
- Ultralytics YOLO (`ultralytics`)
- gTTS (`gtts`)
- Playsound (`playsound`)
- Matplotlib (`matplotlib`) *(optional if using plt display)*

Install dependencies using:

```bash
pip install -r requirements.txt
