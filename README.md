# Entrance_BOT

The Entrance bot python project is a program designed to automate the process of taking attendance at an event. The project involves the use of several Python libraries, including OpenCV, gtts, playsound, numpy, pyzbar, and os.

The program begins by requiring the participants to fill out a Google form to indicate their interest in the event. Once they have completed the form, they receive a unique QR code that they can use to check in at the event.

At the event, participants are required to scan their QR code using a camera. The program uses OpenCV, a computer vision library, to detect and decode the QR code. Once the code is decoded, the program adds the participant's name to a Google Sheet that serves as the attendance record for the event.

In addition to keeping track of attendance, the program has a unique feature that uses the gtts library to generate a greeting for the participant when their QR code is scanned. The program uses the participant's name to create a personalized greeting that is played using the playsound library.

The program also uses the numpy library to perform various image processing tasks, such as thresholding and image resizing. The pyzbar library is used to decode the QR code once it has been detected, and the os library is used to access and manipulate files and directories on the system.

Overall, the Entrance bot python project is an efficient and effective way to automate the attendance-taking process at events, while also providing a personalized and engaging experience for participants.

for this the python library are use:
--> OpenCV      
--> numpy      
--> playsound  (for play text file)
--> pyzbar     (for qrcode decode)
--> gtts       (google text to speech)
