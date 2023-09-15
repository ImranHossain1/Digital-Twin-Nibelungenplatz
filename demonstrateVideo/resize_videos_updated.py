import cv2
import os

def resize_video(input_path, output_path, target_width=360, target_height=360):
    # Load the video
    cap = cv2.VideoCapture(input_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Unable to open the video. Please check if the file exists and the codec is supported.")
        return

    # Get the original video's frame dimensions
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("Original Width:", original_width, "Original Height:", original_height)

    # Calculate the scaling factor
    scale_x = target_width / original_width
    scale_y = target_height / original_height

    # Create the output directory if it does not exist
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a video writer to save the resized video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 30, (target_width, target_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame
        resized_frame = cv2.resize(frame, (target_width, target_height))

        # Write the resized frame to the output video
        out.write(resized_frame)

        cv2.imshow('Resized Frame', resized_frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    # Release video capture and writer
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    input_video_path = 'output_folder/Cam5.mp4'
    output_video_path = 'final_output/Cam5.mp4'
    resize_video(input_video_path, output_video_path, target_width=360, target_height=360)
