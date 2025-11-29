# Golden Ratio Face Analyzer ✨👤

## Introduction

*Golden Ratio Face Analyzer* is a Python-based application that detects faces, extracts **68 facial landmarks**, and analyzes facial proportions against the **Golden Ratio**. It provides a symmetry score, highlights key ratios, and visualizes results with annotated landmarks on the face image.

---

## 📸 Screenshots

### 1. Upload & Detection
Shows how users can upload an image and the system detects facial landmarks.

![Upload Screenshot](/examples/sample.jpg)

---

### 2. Landmark Visualization
Displays the face with **68 green landmark points** plotted.

![Landmark Screenshot](/map/landmarks.jpg)

---

### 3. Golden Ratio Analysis
Illustrates the console output with ratio comparisons and overall symmetry score.

![Analysis Screenshot](/map/analysis.jpg)

---

## 🔧 Tech Stack

- *Language*: Python 3.7+
- *Libraries*: OpenCV, dlib, NumPy, Matplotlib
- *Model*: `shape_predictor_68_face_landmarks.dat` (dlib pretrained model)

---

## ✨ Features

- 📷 Upload and analyze any face image  
- 🔍 Detect **68 facial landmarks**  
- 📏 Compute ratios:  
  - Face Length / Width  
  - Mouth Width / Nose Width  
  - Eye Distance / Nose Width  
- ✅ Compare ratios against the Golden Ratio (≈ 1.618)  
- 🧮 Generate an **Overall Symmetry Score**  
- 🗺 Visualize results with annotated landmarks  

---

## 🚀 Getting Started

### Installation

Clone the repository:

```bash
git clone https://github.com/shreeramparab/face-recognition-project.git
cd face-recognition-project