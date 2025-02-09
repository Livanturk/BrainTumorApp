# Brain Tumor Detection App

A Django-based web application that predicts the presence of a brain tumor from MRI images using a trained deep learning model.

## Features

- Upload MRI images to predict brain tumor types: Glioma, Meningioma, Pituitary, or No Tumor.
- Display the predicted class, confidence score, and uploaded image.
- User-friendly UI for smooth interaction.

## Dataset

The model was trained using the [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset). 

## Requirements

- Python 3.10+
- Django 5.1.6
- TensorFlow 2.18.0
- PIL (Pillow) 9.0+
- Bootstrap for UI

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Livanturk/BrainTumorApp.git
   cd BrainTumorApp

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependecies:
    ```bash
    pip install -r requirements.txt

4. Apply migrations:
    ```bash
    python manage.py migrate

5. Run the server:
    ```bash
    python manage.py runserver

6. Visit http://127.0.0.1:8000/ in your browser.