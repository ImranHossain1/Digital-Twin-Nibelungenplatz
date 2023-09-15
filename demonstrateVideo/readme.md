# Object Detection Visualization in Video using OpenCV

## Introduction

In order to illustrate the results of object detection, this Python script draws bounding boxes and labels on the frames of an input video after reading the findings from a JSON file. The visualization-modified video is saved as an output video.

## Requirements

To run this code, you need the following:

1. **Python:** Make sure Python is set up on your computer. On the official Python website, you may get the most recent version: [Python Downloads](https://www.python.org/downloads/)

2. **OpenCV:** For the purposes of processing and visualizing video, this code uses the OpenCV library. OpenCV may be set up utilizing `pip`:

```
    pip install -r requirements.txt
```

3. **JSON File:** Prepare a JSON file containing object detection results for each frame of the input video. The JSON file should be in the following format:

```
    {
    "frame_name1.jpg": {
        "timestamp": "2023-07-31 12:34:56",
        "object_id_1": {
            "type": "person",
            "x1": 100,
            "y1": 200,
            "x2": 300,
            "y2": 400
        },
        "object_id_2": {
            "type": "car",
            "x1": 350,
            "y1": 100,
            "x2": 500,
            "y2": 300
        },
        ...
    },
    "frame_name2.jpg": {
        ...
    },
    ...
}
```

The JSON file should include object detection results for each frame, where type denotes the class label (e.g., "person," "car," etc.) and x1, y1, x2, and y2 denote the bounding box coordinates of the discovered object.

## How to Use

1. **Clone the Repository:** Use Git to clone this repository to your machine, or download the code as a ZIP archive.

2. **Install Dependencies:** Install the Python and OpenCV dependencies as described in the "Requirements" section.

3. **Prepare Input Video and JSON File:** Make sure you have the input video, Cam1.mp4, as well as the accompanying JSON file, Camera_1_cut_final.json, which contains the results of the object detection. The input_folder should contain both files.

4. **Adjust File Paths (Optional):** Change the file paths in the script if your input video or JSON file is in a different folder or has a different name.

5. **Run the Script:** Navigate to the project directory where the script (object_detection_visualization.py) is located in a terminal or command prompt. Put the Python script into action:

```
    python object_detection_visualization.py
```

6 **Check Output:** After the script has been run, Cam1.mp4 will be used to store the edited video in the output_folder. Bounding boxes and labels will be included in the video in order to visualize the recognized objects.

## Important Notes

1. **File Paths:** The script expects that the input video and JSON file are in the `input_folder` and that the output video will be saved in the `output_folder`. Be remember to adjust the file paths in the script if your files are kept in a different directory structure. The variables `input_video_path`, `json_file_path`, and `output_video_path` in the script can be changed to point to the appropriate places.

2. **Custom Colors:** The code draws bounding boxes and labels on the video frames using predetermined colors for various class labels (such as `person,` `car` etc.). You can edit the script's `class_colors` dictionary to assign unique colors to various classes. To represent the desired colors, simply alter the class labels as keys and supply the RGB values (0–255) as values.

3. **Integration with Other Projects:** The script uses the OpenCV VideoWriter and VideoCapture APIs to process and display video. To view the results of object detection in films, you can incorporate the object detection visualization code into your own Python projects. This enables you to modify the visualization process according to your particular needs.

---

# Video Resize using OpenCV

## Introduction

A Python script that uses OpenCV to resize a video is available in this repository. The script loads an existing video, resizes every frame, and then creates a new video from the resized frames. The 'final_output' directory houses the resized video.

## Requirements

To run this code, you need the following:

1. **OpenCV:** The OpenCV library is used by this code to process video. OpenCV may be set up utilizing `pip`:

2. **FFmpeg (Optional):** You can transcode the video using FFmpeg if OpenCV has trouble opening the input video. Make sure FFmpeg is set up on your computer. Visit the official website to get FFmpeg.: [FFmpeg Downloads](https://www.ffmpeg.org/download.html)

## How to Use

1. **Clone the Repository:** Use Git to clone this repository to your machine, or download the code as a ZIP archive.

2. **Install Dependencies:** Install the Python and OpenCV dependencies as described in the "Requirements" section.

3. **Prepare Input Video:** Make sure the video you wish to resize is the input video. The `output_folder` should contain the video in a supported format. The `Video Format Conversion for OpenCV` section of the README explains how to use FFmpeg to convert a video if it is not in a format that is supported.

4. **Adjust Parameters (Optional):** In the script, you can modify the target width and height to acquire the resizing dimensions you want. The script automatically resizes to `360x360` pixels.

5. **Run the Script:** Go to the project directory where the script (resize_video.py) is located by opening a terminal or command prompt. Use Python to run the script:

```
    python resize_video.py
```

6. **Check Output:** The resized video will be saved as `Building9Final.mp4` in the `final_output` directory when the script has finished running. The video will be scaled to the desired size (for example, `360x360` pixels).
