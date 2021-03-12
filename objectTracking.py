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

tracker = cv2.TrackerKCF_create() # Creating KCF tracker instance
fps = FPS()
bbox = None

cap = cv2.VideoCapture(args["video"])

while True:
    _, frame = cap.read()
    if frame is None:
        print("No more frames detected, ending video...")
        break

    frame = imutils.resize(frame, width=WIDTH) #resize frame for faster processing
    HEIGHT, WIDTH, CHANNEL = frame.shape

    if bbox is not None: # checking for bounding box
        (ret, box) = tracker.update(frame)

        fps.update()
        fps.stop()

        if ret:
            (x, y, w, h) = [int(num) for num in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), BOX_COLOR, LINE_THICKNESS)
            frame = fps.fps_print(frame) # prints fps on screen

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s') and not bbox:
        bbox = cv2.selectROI("Frame", frame)
        tracker.init(frame, bbox)
        fps = FPS()
        fps.start()

    if key == ord('c'):
        tracker = cv2.TrackerKCF_create()
        bbox = None

    if key == ord('q'):
        print("Exiting video...")
        break


cap.release()
cv2.destroyAllWindows()