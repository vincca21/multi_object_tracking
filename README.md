# multi_object_track
 
## Overview

This project is a simple multi-object tracker using OpenCV. It allows you to track multiple objects in a video stream or a video file.

## Features

- Track multiple objects simultaneously
- Supports various OpenCV trackers (KCF, CSRT, MIL, etc.)
- Works with both webcam and video files

## Requirements

- Python 3.x
- OpenCV
- imutils

## Usage

1. Clone the repo:
    ```sh
    git clone https://github.com/yourusername/multi_object_track.git
    cd multi_object_track
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the tracker:
    ```sh
    python multi_obj_track.py --video path/to/video --tracker kcf
    ```

4. Press `s` to select objects to track, `q` to quit.

## Notes

- Default tracker is KCF. Change with `--tracker` flag.
- If no video path is provided, webcam is used.

