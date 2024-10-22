# Installing packages
import numpy as np
import cv2
from sklearn.linear_model import LinearRegression
from os import getcwd


# Placeholder for feature extraction
def extract_image_features(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image_resized = cv2.resize(image, (64, 64))  # Resize for uniformity
    features = np.array(image_resized).flatten()  # Convert image to a 1D array of pixel values
    return features


def process():
    # Load the image
    image_path = getcwd() + "\\media\\input.tif"
    features = extract_image_features(image_path)

    # Dummy Linear Regression model
    classifier = LinearRegression()

    result = classifier.predict([features])

    if result >= 0.5:
        prediction = 'Tampered'
    else:
        prediction = 'Original'

    print("Result : " + prediction)
    return prediction
