import os
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import shutil

def resize_and_align_faces(input_folder, output_folder, target_size=(640, 360)):
    aligned_images = []
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jfif") :
            # Load the image
            image_path = os.path.join(input_folder, filename)
            img = cv2.imread(image_path, cv2.IMREAD_COLOR)

            # Convert to grayscale for face detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(30, 30))

            for (x, y, w, h) in faces:
                # Crop and resize each detected face to the target size
                face = cv2.resize(img[y:y+h, x:x+w], target_size)

                # Save the aligned face to the output folder with a unique filename
                output_filename = os.path.splitext(filename)[0] + f"_face_{len(aligned_images)}.png"
                output_path = os.path.join(output_folder, output_filename)
                cv2.imwrite(output_path, face)
                aligned_images.append(output_path)

    return aligned_images
a = 'input source'
b = 'output source'
resize_and_align_faces(a,b)