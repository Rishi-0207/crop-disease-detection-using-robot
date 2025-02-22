import cv2
import requests
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import model

# Function to fetch and update the frame from the URL

Project_name = "Smart Car"
img_data = 0
def update_frame():
    global img_data
    try:
        # Fetch the image from the URL
        response = requests.get("http://192.168.4.1/capture")
        response.raise_for_status()  # Check if the request was successful
        image_data = response.content

        # Convert the image to a format compatible with OpenCV and Tkinter
        np_array = cv2.imdecode(
            np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR
        )
        # cv2image = cv2.imread(r'Dataset\test\Tomato___Bacterial_spot (1).JPG')
        cv2image = cv2.cvtColor(np_array, cv2.COLOR_BGR2RGB)
        img_data = cv2image
        img = ImageTk.PhotoImage(image=Image.fromarray(cv2image))

        # Update the label with the new image
        video_label.config(image=img)
        video_label.image = img
    except Exception as e:
        print("Error fetching image:", e)
    
    # Schedule the next frame update
    root.after(100, update_frame)

# Function to handle the "Predict" button click
def on_predict():
    global img_data
    # Placeholder for prediction logic
    # Replace this with actual prediction logic from your model
    # model.predict(img_data)
    result_label.config(text=f"Prediction: {model.predict(img_data)}!")  # Example text

# Initialize Tkinter GUI
root = Tk()
root.title(Project_name)
root.geometry("400x500")  # Adjust the size to fit components better

# Add an outer frame for the app border
app_frame = Frame(root, bg="gray", bd=10, relief="ridge")
app_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Add a colorful title inside the app frame
title = Label(app_frame, text=Project_name, font=("Helvetica", 16, "bold"), fg="white", bg="blue")
title.pack(fill=X, pady=5)

# Add an inner frame for the video border
video_frame = Frame(app_frame, bg="black", bd=5, relief="solid")
video_frame.pack(expand=True, padx=10, pady=10)

# Add a label inside the video frame for the video feed with a fixed size
video_label = Label(video_frame, bg="white", width=320, height=240)
video_label.pack()

# Add a label below the video feed to display predictions
result_label = Label(app_frame, text="Prediction: Waiting for input...", font=("Helvetica", 12), fg="blue", bg="white")
result_label.pack(pady=10)

# Add a "Predict" button at the bottom inside the app frame
predict_button = Button(app_frame, text="Predict", font=("Helvetica", 12, "bold"), bg="green", fg="white", command=on_predict)
predict_button.pack(side=BOTTOM, pady=10)

# Start fetching and displaying the video feed
update_frame()
root.mainloop()
