from cv2 import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the data 
X = np.load('image.npz')['arr_0']
y = pd.read_csv("labels.csv")["labels"]

# Splitting the data to train and test the model
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=9, train_size=3500, test_size=500)

# Fitting the data 
clf = LogisticRegression(solver='saga', multi_class='multinomial').fit(x_train_scaled, y_train)

# Calculating the accuracy of the model
y_pred = clf.predict(x_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("The accuracy is :- ",accuracy)

# Open the camera 
cam = cv2.VideoCapture(0)

while(True):
    try:
        ret, frame = cap.read()
        print("Inside the loop")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Drawing a box in the center of the video
        height, width = gray.shape
        bottom_right = (int(w/2 + 56), int(h/2 + 56))
        upper_left = (int(width / 2 - 56), int(height / 2 - 56))
        cv2.rectangle(gray, upper_left, bottom_right, (0, 255, 0), 2)
        # To only consider the area inside the box
        roi = gray[upper_left[1]:bottom_right[1], upper_left[0]:bottom_right[0]]
        # Converting the image to PIL format
        im_pil = Image.fromarray(roi)
        # Convert the image to grayscale
        image_bw = im_pil.convert('L')
        image_bw_resized = image_bw.resize((28,28), Image.ANTIALIAS)
        # Inverting the image
        image_bw_resized_inverted = PIL.ImageOps.invert(image_bw_resized)
        pixel_filter = 20
        # Converting to scaler quantity
        min_pixel = np.percentile(image_bw_resized_inverted, pixel_filter)
        image_bw_resized_inverted_scaled = np.clip(image_bw_resized_inverted-min_pixel, 0, 255)
        max_pixel = np.max(image_bw_resized_inverted)
        #converting into an array
        image_bw_resized_inverted_scaled = np.asarray(image_bw_resized_inverted_scaled)/max_pixel
        #creating a test sample and making a prediction
        test_sample = np.array(image_bw_resized_inverted_scaled).reshape(1,784)
        test_pred = clf.predict(test_sample)
        print("Predicted class is: ", test_pred)
        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break        
    except Exception as e:
            pass

cam.release()
cv2.destroyAllWindows()


    
