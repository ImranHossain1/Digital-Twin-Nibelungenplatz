import os
import cv2
import json

# Specify the paths for input video, JSON file, and output video
input_video_path = 'input_folder/Cam3.mp4'
json_file_path = 'input_folder/cam3_7500.json'
output_video_path = 'output_folder/Cam3.mp4'

# Create the output folder if it doesn't exist
output_folder = os.path.dirname(output_video_path)
os.makedirs(output_folder, exist_ok=True)

# Read the JSON file containing object detection results
with open(json_file_path, 'r') as file:
    detection_data = json.load(file)

# Load the input video
cap = cv2.VideoCapture(input_video_path)

# Get the video's properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create an output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Define colors for specific classes
class_colors = {
    'person': (0, 255, 0),    # Green
    'car': (0, 255, 255),     # Yellow
    'truck': (255, 0, 0),     # Blue
    'motorcycle': (0, 165, 255),  # Orange
    'bicycle': (0, 0, 255),     # Red
    'train': (0, 0, 0),       # Black
    'bus': (128, 0, 128)      # Purple
}

# Iterate over each frame in the video
for frame_name, frame_data in detection_data.items():
    # Extract the object detection results for the current frame
    timestamp = frame_data['timestamp']
    objects = frame_data.copy()
    del objects['timestamp']

    # Read the frame from the input video
    ret, frame = cap.read()

    if not ret:
        break

    # Draw bounding boxes and labels on the frame to visualize the detected objects
    for obj_id, obj_data in objects.items():
        label = obj_data['type']
        x1 = int(obj_data['x1'])
        y1 = int(obj_data['y1'])
        x2 = int(obj_data['x2'])
        y2 = int(obj_data['y2'])

        # Assign color based on the class label
        color = class_colors.get(label, (0, 0, 0))  # Default color: Black

        # Draw the bounding box with the assigned color
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        # Add label text
        label_text = f'{label} (ID: {obj_id})'
        cv2.putText(frame, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # Write the modified frame to the output video
    out.write(frame)

# Release resources
cap.release()
out.release()

# Print a message indicating the completion of the video creation
print('Video creation complete!')
