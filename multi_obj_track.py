# multi_obj_track.py
"""Functions for tracking multiple objects in a video."""
import argparse
import time

import cv2
import imutils
from imutils.video import VideoStream

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str, help="path to input video file")
ap.add_argument("-t", "--tracker", type=str, default="kcf", help="OpenCV object tracker type")
args = vars(ap.parse_args())

# Initialize directory to map tracker names to Opencv funcs
OPENCV_OBJECT_TRACKERS = {
    "csrt": cv2.legacy.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
    "mil": cv2.legacy.TrackerMIL_create,
    "tld": cv2.legacy.TrackerTLD_create,
    "medianflow": cv2.legacy.TrackerMedianFlow_create,
    "mosse": cv2.legacy.TrackerMOSSE_create
}

# Initialize the multi-object tracker
trackers = cv2.legacy.MultiTracker_create()

# If a video path was not supplied, grab the reference to the webcam
if not args.get("video", False):
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    time.sleep(1.0)
# Otherwise, grab a reference to the video file
else:
    vs = cv2.VideoCapture(args["video"])
    
# Loop over frames from the video stream
while True:
    # Read the next frame from the video stream
    frame = vs.read()
    frame = frame[1] if args.get("video", False) else frame
    
    # If we are viewing a video and we did not grab a frame, then we have reached the end of the video
    if frame is None:
        break
    
    # resize the frame
    frame = imutils.resize(frame, width=600)
    
    # update trackers & draw box
    (success, boxes) = trackers.update(frame)
    for box in boxes:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    # Show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    # If the 's' key is selected, we are going to "select" a bounding box to track
    if key == ord("s"):
        # select the bounding box of the object we want to track
        box = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
        
        # create a new object tracker for the bounding box and add it to our multi-object tracker
        tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]()
        trackers.add(tracker, frame, box)
        
    # If the 'q' key is selected, break from the loop
    elif key == ord("q"):
        break
    
# If we are using a webcam, release the pointer
if not args.get("video", False):
    vs.stop()
# Otherwise, release the file pointer
else:
    vs.release()
    
# Close all windows
cv2.destroyAllWindows()
