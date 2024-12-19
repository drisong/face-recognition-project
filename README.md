# Face Recognition Project
#### Video Demo:  <URL HERE>
#### Description: The project compares a given face with pictures in a folder and copies the images that match the reference face.

# Face Recognition Project

Welcome to the Face Recognition Project! This repository contains a basic Python-based implementation for face recognition. The project compares a given face with images in a folder and creates an output folder containing copies of the images that match the given face.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)

---

## Introduction

Face recognition technology is widely used in various domains, including security and surveillance systems, user authentication, airport and border control, and image tagging. This project demonstrates how to use computer vision libraries in Python to compare a given face with images in a folder. When a match is found, the project copies the matched images into a specified output directory.

This repository is ideal for:
- Beginners interested in exploring computer vision and machine learning.
- Developers building face recognition systems for their projects.
- Students working on academic or personal projects involving facial recognition.

---

## Features

- **Face Comparison**: Compare a given face against images in a folder.
- **Match Detection**: Identify matching images based on facial similarity.
- **File Organization**: Automatically copy matched images to a designated folder.
- **Cross-Platform**: Compatible with Linux, macOS, and Windows.

---

## Technologies Used

The project leverages the following technologies:

- **Python**: The programming language used for development.
- **OpenCV**: A library for real-time computer vision tasks.
- **dlib**: A machine learning library for face detection and recognition.
- **NumPy**: For numerical computations.
- **shutil module**: To handle file operations.

---

## Installation

Follow these steps to set up the project on your local machine:

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/drisong/face-recognition-project.git
cd face-recognition-project
```

### Prerequisites

1. Install Python (version 3.12.3 or higher).
2. Ensure `pip` is installed.
3. Create a virtual environment `python -m venv [folder]` and activate it.
3. Install the following libraries in the requirements file:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Prepare Your Dataset

- Create a folder named `images` and add the JPEG or PNG images you want to compare against.
- Place the reference face image in the project root directory or create a folder for it and name it `face.jpg` (or specify a different name using the script arguments).

### 2. Run the Script

Execute the script with the following command:

```bash
python project.py
--face /path of face.jpg
--source /path of images folder
--output /path of output folder (if it doesn't exist, the program will create one)
```

If you would like to know the usage, you can execute the following command:

```bash
python project.py -h
```

Inside the folder, I've put some images for testing. You can execute the command using the reference file and folder given.

### 3. Script Arguments

- `--face`: Path to the reference face image (.jpeg or .png).
- `--source`: Path to the folder containing input images.
- `--output`: Path to the folder where matched images will be saved.

### 4. Tolerance

After execution, the program will ask you for a tolerance value. The default value is 0.6 and lower numbers make face comparisons more strict.
If you are getting multiple matches for the same person, it might be that the people in your photos look very similar and a lower tolerance value is needed.

### 5. Output

The matched images will be copied to the `output` folder, maintaining their original names.

---

## Folder Structure

```plaintext
face-recognition-project/
├── images/
│   └── ...test_images.jpg
├── known-face/
│   └── face.jpg
├── project.py
├── README.md
└── requirements.txt
```

---

Thank you for using the Face Recognition Project!