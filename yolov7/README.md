# Yolov7 with object tracking

[TOC]

## Setup

### Prerequisites

python version <= 3.8.10

### Source

Yolov7 https://github.com/WongKinYiu/yolov7   
Yolo object Tracking https://github.com/haroonshakeel/yolov7-object-tracking

### Install from Gitlab

**Step 1: Clone DTN Main Repo**

```
git clone git@gitlab.informatik.fb2.hs-intern.de:kweronek/dtn.git
```

**Step 2: Setup virtual environment**

```
pip install virtualenv
python -m virtualenv env_yolo7
```

**Step 3: Activate virtual environment**

Windows:

```
env_yolo7/Scripts/activate.bat
```

Linux

```
source env_yolo7/bin/activate
```

**Step 4: Install requirements**

```
pip install -r requirements.txt
```

**Step 5: Installing tk**

Windows:
```
pip install tk
```
Linux:
```
pip install tk
sudo apt-get install python3-tk
```

**Step 6: Download yolov7 model from Yolo7 Repo (https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt) and copy the .pt file into
   yolov7/model/**

   For different models with different performances check: https://github.com/WongKinYiu/yolov7#performance

## Execute

Execute the following command after inserting the video path to use the object detection with tracking.   
Vehicle detection is to be used in this project, which is why we use the object classes 2: car, 5: bus, 6: train, 7: truck.

```
python detect_or_track.py --weights ./models/yolov7.pt --no-trace --view-img --save-txt --classes 1 2 5 6 7 --track --source <video_path>
```

### Relevant Keys

| Key        | Description                                                   | Required |
| ---------- | ------------------------------------------------------------- | -------- |
| weights    | Path to downloaded model (.pt)                                | x        |
| source     | Path to video to analyse                                      | x        |
| device     | For gpu acceleration enter device id                          |          |
| view-img   | Display results while analysing                               |          |  
| save-txt   | Save json (standard path: ../runs/detect/exp/labels/*.json)   |          | 
| save-video | Save analysed video (standard path: ../runs/detect/exp/*.mov) |          | 
| nosave     | Do not save videos / images                                   |          | 
| classes    | Objectclasses to detect (2: car, 5: bus, 6: train, 7: truck)  | x        | 
| no-trace   | Don't trace model                                             |          | 
| track      | Activate object tracking                                      | (x)      |


## Output

The output of the object detection is saved in /yolov7/runs/detect/exp<last detection>/labels/<video_name>.json

Output format:

```
{
   "frame_with_number":{
      "timestamp": "YYYY-mm-ddTHH:MM:SS.fffZ",
      "tracking_id": {
         "type": "detectet_vehicle_type",
         "class": "class_from_coco128_data_set",
         "x1": "top_left_boundingbox_corner_x",
         "y1": "top_left_boundingbox_corner_y",
         "x2": "bottom_right_boundingbox_corner_x",
         "y2": "bottom_right_boundingbox_corner_y",
      },
      "tracking_id": {...}
      ...
   },
   "frame_with_number+1":{...}
   ...
}
```

x1,y1,x2,y2 give the corners (in pixels) of the boundingbox of a detected object. Origin for the pixels is the top left corner of a picture with (0,0)

Output example:

```
{
   "frame1":{
      "timestamp": "2022-11-28T15:33:37.642Z",
      "1": {
         "type": "car",
         "class": "2",
         "x1": "378",
         "y1": "30",
         "x2": "395",
         "y2": "39",
      },
      "2": {...}
      ...
   },
   "frame2":{...}
   ...
}
```

## Known Bugs
### TKinter conflict with matplotlib 
Under Windows there can be a possibility to occure an error in sort.py. This is a known conflict from matplotlib in occurrence with tkinter.   
We fixed this with changing line 6 in sort.py:
``` 
matplotlib.use('TkAgg') 
``` 
to
``` 
matplotlib.use('Agg') 
```
### Timestamp workaround
Opencv2 cannot guarantee to successfully read the timestamp of every frame either because opencv failed or the file does not have a timestamp. In this case the following code segment will result in 0.0 value and thus indicates having the same timestamp as the first frame.   
``` 
cap_diff = vid_cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
``` 
It is necessary to check for this case. As a workaround we have two cases:    
1. The Error happens in the first two frames. In this case the timestamp will be static.
2. The Error happens after 3 or more frames. In this case the estimated timeframe gets calculated out of the diffrence of the last and second last frame.
