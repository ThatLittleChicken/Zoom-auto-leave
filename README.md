# Zoom-auto-leave
To exit online class automatically while away from keyboard without being noticed that you went AFK. Auto leaves zoom call when class ends based on the amount of participants.

## Instructions
- Open Zoom in maximize-windowed (not full screen)
- Show particpants tab in zoom
- Run "Zoom auto leave"

Tested and made on 1920x1080 screen, find and edit location of "Participants (x)" if using different screen size

## Prerequisite
- Python 3.x installed
- Necessary libraries installed
  - pyautogui
  - numpy
  - pytesseract
  - opencv-python

Will abort if cant read participant number. Ensure all images are in the same folder as the program.
