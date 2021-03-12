from utils.config import BOX_COLOR, LINE_THICKNESS, WIDTH
from utils.FPS import FPS
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser() # parse args
ap.add_argument("-v", "--video", required=True, help="path to video file")
args = vars(ap.parse_args())

if args["video"].isdigit(): # check int for peripheral cam
    args["video"] = int(args["video"])
    print(args["video"])

try:
    tracker = cv2.TrackerKCF_create()
except:
    print("OpenCV isn't properly loading the tracker...\n\
    make sure you installed the opencv-contrib-python version...")
    exit(1)

print("[INFO]Everything was properly loaded you are ready for the workshop...")
print("[INFO]Feel free to mess around with OpenCV...")

# Initialize fps, bbox, and capture

# Begin infinte loop

# capture frame and check for errors

# resize window and grab shape

# Initialize bbox tracking DO LAST

# display frame and grab key input

# Check For keys

# Release
