import cv2
import numpy as np
from pyzbar.pyzbar import decode
from gtts import gTTS
from playsound import playsound
import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BOARD)
ir_pin = 12
GPIO.setup(ir_pin, GPIO.IN)

# Camera setup
cap = cv2.VideoCapture(0)

# QR Code detection and greeting function
def detect_and_greet():
    success, img = cap.read()
    for QRCode in decode(img):
        name = QRCode.data.decode('utf-8')
        print(f"Detected QR Code with data: {name}")
        pts = np.array([QRCode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)

        # Greeting with user name using gTTS and playsound
        audio = gTTS(f"Hello, {name}!, Welcome to ISA Event", lang='en', tld='co.in', slow=False)
        audio.save("textaudio.mp3")
        playsound('textaudio.mp3')

    cv2.imshow("Result", img)
    cv2.waitKey(1)

# Main loop
while True:
    if GPIO.input(ir_pin):
        detect_and_greet()
        time.sleep(1)
