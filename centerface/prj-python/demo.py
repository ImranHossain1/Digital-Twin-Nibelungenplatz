import cv2
import os
from centerface import CenterFace


def test_stream(output_path: str):
    """
    Test CenterFace model on input from streaming camera
    """

    # Create a VideoCapture object and read from input file
    # Since the input is to be taken from the camera, pass 0
    cap = cv2.VideoCapture(0)
    # Check if streaming camera opened successfully
    if cap.isOpened() == False:
        print("Error getting input from streaming camera")
    # Read a frame of the input video to find the video height and width
    _, frame = cap.read()
    h, w = frame.shape[:2]
    # Initialize model
    centerface = CenterFace()

    # Create VideoWriter object to save the output video
    out = cv2.VideoWriter(
        os.path.join(output_path, "output_stream.mp4"),
        cv2.VideoWriter_fourcc(*"mp4v"),
        24,  # FPS
        (w, h),
    )

    # Read until streaming camera is manually stopped
    while cap.isOpened():
        # Read frame-by-frame
        _, frame = cap.read()
        # Model generates detections
        dets, lms = centerface(frame, h, w, threshold=0.35)
        # Draw detections on the input frame
        # draw_det(frame, dets)
        # Blur each detection on the frame
        for det in dets:
            blur_det(frame, det)
        # Write/Save the frame to the output
        out.write(frame)
        # Display the resulting frame
        cv2.imshow("stream_output", frame)
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # When everything done, release the video capture object
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()


def test_image(input_path: str, output_path: str):
    """
    Test CenterFace model on image input
    """

    # Read image input
    frame = cv2.imread(input_path)
    # Find the height and width of image input
    h, w = frame.shape[:2]
    # Initialize model
    centerface = CenterFace()
    # Model generates detections
    dets, lms = centerface(frame, h, w, threshold=0.35)
    # Draw detections on image input
    # draw_det(frame, dets)
    # Blur each detection on the frame
    for det in dets:
        blur_det(frame, det)
    # Get file name of video input
    _, filename = os.path.split(input_path)
    # Save the resulting frame
    cv2.imwrite(
        os.path.join(output_path, filename),
        frame,
    )
    # Display the resulting frame
    cv2.imshow(input_path, frame)
    # Show the resulting frame until a key is pressed
    cv2.waitKey(0)


def test_video(input_path: str, output_path: str):
    """
    Test CenterFace model on video input
    """

    # Create a VideoCapture object and read from input file
    # Since the input is a video, pass the video path
    cap = cv2.VideoCapture(input_path)
    # Check if the video input is read successfully
    if cap.isOpened() == False:
        print("Error getting video input")
    # Read a frame of the input video to find the video height and width
    _, frame = cap.read()
    h, w = frame.shape[:2]
    # Initialize model
    centerface = CenterFace()

    # Get file name of video input
    _, filename = os.path.split(input_path)
    # Create VideoWriter object to save the output video
    out = cv2.VideoWriter(
        os.path.join(output_path, filename),
        cv2.VideoWriter_fourcc(*"mp4v"),
        24,  # FPS
        (w, h),
    )

    # Read until video input ends
    while cap.isOpened():
        # Read frame-by-frame
        _, frame = cap.read()
        # Model generates detections
        dets, _ = centerface(frame, h, w, threshold=0.35)
        # Draw detections on the input frame
        # draw_det(frame, dets)
        # Blur each detection on the frame
        for det in dets:
            blur_det(frame, det)
        # Write/Save the frame to the output
        out.write(frame)
        # Display the resulting frame
        cv2.imshow(input_path, frame)
        # Press Q on keyboard to stop playing the video
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # When everything done, release the video capture object and the video write object
    cap.release()
    out.release()
    # Closes all the frames
    cv2.destroyAllWindows()


def draw_det(frame, dets):
    """
    Draw the detections on the frame using rectangles
    """

    for det in dets:
        boxes, score = det[:4], det[4]
        cv2.rectangle(
            frame,
            (int(boxes[0]), int(boxes[1])),
            (int(boxes[2]), int(boxes[3])),
            (2, 255, 0),
            1,
        )


def blur_det(frame, det, blur_amount=51):
    """
    Blur detections on the frame by the given amount
    More specifically, get the detection, blur it, and stick it back on the frame
    """

    boxes = det[:4]
    top_left_x, top_left_y, bottom_right_x, bottom_right_y = (
        int(boxes[0]),
        int(boxes[1]),
        int(boxes[2]),
        int(boxes[3]),
    )
    det = frame[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
    blur = cv2.GaussianBlur(det, (blur_amount, blur_amount), 0)
    frame[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = blur


if __name__ == "__main__":

    # For execution, run the following methods one at a time.
    # Remember to put data in the input folder and specify the output folder.

    output_path = os.path.join(os.getcwd(), "output")
    image_input_path = os.path.join(os.getcwd(), "input", "images", "000388.jpg")

    # The test video can be found in MagentaCloud/video_recordings/WS_22
    video_input_path = os.path.join(
        os.getcwd(), "input", "videos", "1_SD_test_video_for_centerface.mp4"
    )

    # test_stream(output_path)
    # test_image(image_input_path, output_path)
    #test_video(video_input_path, output_path)
