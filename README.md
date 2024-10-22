
# Fake Image Detection Using Linear Regression

This project is a web-based application developed using **Django** and **Python** for detecting tampered (fake) images using **Linear Regression**. The application allows users to upload an image, processes the image, and predicts whether it is tampered or original.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)

## Project Overview

With the widespread availability of photo editing software, fake images are a growing concern. This project aims to provide a simple, user-friendly web application for detecting fake images based on a Linear Regression model that analyzes image features. The system accepts image inputs, processes them to extract features, and classifies them as either **Tampered** or **Original**.

## Features

- **User Registration and Login**: Users can create accounts and log in.
- **Image Upload**: Upload images directly through the web interface.
- **Fake Image Detection**: Linear regression is used to detect whether an image is tampered or original.
- **Result Display**: Shows the result after analysis of the uploaded image.

## Technologies Used

- **Backend**: Django (Python-based web framework)
- **Machine Learning**: Linear Regression (scikit-learn)
- **Frontend**: HTML, Bootstrap, JavaScript
- **Database**: SQLite (default for Django) or MySQL (optional)
- **Image Processing**: OpenCV, NumPy

## Installation

To run the project locally, follow these steps:

### Prerequisites

- Python 3.x
- pip (Python package manager)
- virtualenv (optional but recommended)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Prameeth8817/Fake-Product-Detection-Using-Linear-Regression.git
    cd fake-image-detection
    ```

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv env
    source env/bin/activate  # For Linux/Mac
    env\Scripts\activate  # For Windows
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000/` to use the application.

## Usage

1. **Register or Log in**: Users need to create an account or log in to access the image detection feature.
2. **Upload an Image**: On the home page, upload an image in a `.jpg` or `.png` format.
3. **Get Results**: The system will classify the image as either **Tampered** or **Original**.

### Example

- Go to `/register` to create a new account.
- Once registered, go to `/login` to sign in.
- Upload your image on the home page, and the system will analyze it and provide the result.

## File Structure

```bash
fake-image-detection/
│
├── forgery_app/                # Main Django app for handling views, models, etc.
│   ├── migrations/             # Django database migrations
│   ├── templates/              # HTML files
│   ├── static/                 # CSS, JS, and image files
│   └── views.py                # Django views for handling requests
│
├── media/                      # Uploaded images
│
├── manage.py                   # Django management script
├── README.md                   # Project documentation
├── requirements.txt            # List of required packages
├── trained_model/              # Placeholder for trained ML model files
└── db.sqlite3                  # SQLite database file (default for Django)
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add feature/your-feature-name"
    ```
4. Push the changes to your fork:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Create a pull request and describe your changes.


### Notes:
- Replace `https://github.com/Prameeth8817/Fake-Product-Detection-Using-Linear-Regression.git` with your GitHub repository URL.
- Modify the `File Structure` section based on your actual file structure if necessary.
- You might need to add or update the `requirements.txt` with the necessary packages such as Django, scikit-learn, OpenCV, etc.

Let me know if you need further customization!