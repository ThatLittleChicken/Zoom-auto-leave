import pyautogui 
import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab
import re

print('Ensure Zoom is in maximized mode (not fullscreen) and Participants tab is toggled, this is coded for 1080p screen so do change capture location if youre on a different screen. Also relocate tesseract location before using, usally just replace user file name\n')

print('Enter minimum participants to leave:')
inpt = input()
while True:
        if re.match('\D',inpt) != None:
                print('Enter a NUMBER')
                inpt = input()
        else: break
participants = int(inpt)
#print(participants)

print('Press Ctrl-C to abort.')
def imToString():
        try:
           # Path of tesseract executable
           pytesseract.pytesseract.tesseract_cmd = r"C:\Users\yongg\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
           while(True):
                
                num = 0
                # imageGrab to capture the screen image in a loop. 
                # bbox used to capture a specific area.
                cap = ImageGrab.grab(bbox =(1680, 40, 1820, 60))
                # converted the image to mono for it to be easily 
                # read by the OCR and obtained the output String.
                tesstr = pytesseract.image_to_string(
                        cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
                        lang ='eng')
                '''print(tesstr)'''

                # somehow covert input to int
                no = [int(s) for s in re.findall(r'\d+',tesstr)]
                no1 = [str(no) for no in no]
                no2= "".join(no1)
                num = int(no2)
                print('Participants:',num , end='')
                print('\b' * 20, end='', flush=True)
                
                # check for minimum particpants
                # move mouse into window, locate and click leave button
                if num <= participants :
                        pyautogui.moveTo(700, 700)
                        x,y = pyautogui.locateCenterOnScreen('End.png')
                        pyautogui.click(x,y)
                        x,y = pyautogui.locateCenterOnScreen('Leave.png')
                        pyautogui.click(x,y)
                        print('\nLeft Class')
                        input("\nPress Enter to continue...")
                        break
        except KeyboardInterrupt:
                print('\nTerminated')
                input("\nPress Enter to continue...")

imToString()

# no idea what im doing lol.
