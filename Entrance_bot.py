import cv2
import numpy as np
from pyzbar.pyzbar import decode
from gtts import gTTS 
from playsound import playsound
import os

cap = cv2.VideoCapture(1)

name = ""
def convert_to_audio(text):
    audio = gTTS(f"Hello, {name}!, Welcome to ISA's Symposium event, converge", lang='en', tld='co.in', slow=False)
    audio.save("textaudio.mp3")
while True:
    success, img = cap.read()
    for QRCode in decode(img):
        qrcode = QRCode.data.decode('utf-8')
        name = qrcode
        pts = np.array([QRCode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        
        if name:
            convert_to_audio(name)
            playsound('textaudio.mp3')
            os.remove("textaudio.mp3")
            name= ""
        
    cv2.imshow("Result",img)
    cv2.waitKey(1)
    
    





