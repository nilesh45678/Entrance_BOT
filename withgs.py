import cv2
import numpy as np
from pyzbar.pyzbar import decode
from gtts import gTTS 
from playsound import playsound
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#pip install google-api-python-client

# Define the scope and credentials of the Google Sheets API
scope = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"]
creds = ServiceAccountCredentials.from_json_keyfile_name("D:\entrance_bot\GS.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("EntranceBOT").sheet1

# Display welcome message on the 16x2 LCD screen
# ...

cap = cv2.VideoCapture(0)

name = ""

while True:
    success, img = cap.read()
    for QRCode in decode(img):
        qrcode = QRCode.data.decode('utf-8')
        name = qrcode
        pts = np.array([QRCode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)

    cv2.imshow("Result",img)
    cv2.waitKey(1)
    
    if name:
        # Add the QR code data to the Google Sheet
        row = [name]
        sheet.append_row(row)
        break

def convert_to_audio(text):
    audio = gTTS(f"Hello, {name}!, Welcome to ISA Event", lang='en', tld='co.in', slow=False)
    audio.save("textaudio.mp3")

convert_to_audio(name)

playsound('textaudio.mp3')
