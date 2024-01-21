'''Sample code to connect arduino to a secondary device via bluetooth and classify images

import torch
from torchvision import transforms
from PIL import Image
import cv2
import serial
import time
import pickle
import io
import fastai

def is_fire(f): return f[0] == 'f'

class CPU_Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == 'torch.storage' and name == '_load_from_bytes':
            return lambda b: torch.load(io.BytesIO(b), map_location='cpu')
        else: return super().find_class(module, name)
        
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model =  CPU_Unpickler(open("/Users/parthivvarma/Projects/forest_fire_detection/forest_fire.pth","rb")).load()

model.eval()



# OpenCV setup for capturing images from the camera
cap = cv2.VideoCapture(0)

# PyTorch transformation for image processing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Bluetooth setup
arduino_port = '/dev/tty.YOUR-ARDUINO-SERIAL-PORT'  # Change this to your Arduino's serial port
baud_rate = 9600

try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    print("Connected to Arduino")

    while True:
        # Capture an image from the camera
        ret, frame = cap.read()

        # Convert the OpenCV image to PIL format
        pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Preprocess the image
        input_tensor = transform(pil_image)
        input_batch = input_tensor.unsqueeze(0)

        # Perform inference
        with torch.no_grad():
            output = model(input_batch)

        # Get the predicted class
        _, predicted_class = torch.max(output, 1)

        # Send a message to Arduino based on the prediction
        if predicted_class.item() == 1:  # Assuming class 1 represents fire (adjust based on your model)
            ser.write(b'1')  # Send '1' to Arduino
            print("Fire detected! Sending message to Arduino.")
        else:
            ser.write(b'0')  # Send '0' to Arduino
            print("No fire detected.")

        # Display the captured frame (optional)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except serial.SerialException:
    print("Error: Could not open serial port. Ensure that the port is correct.")
finally:
    # Release the camera and close the serial connection
    cap.release()
    ser.close()
    cv2.destroyAllWindows()'''
