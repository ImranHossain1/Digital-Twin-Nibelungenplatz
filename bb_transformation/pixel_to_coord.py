import pandas as pd
import os
import cv2
import numpy as np
import json


def pixel_to_coord(input_path: str, reference_path: str, output_path: str):
    """
    The purpose of the function is to transform pixel coordinates from an input image to geographic coordinates, using a reference file.
    """
    # Split file path into two parts: the directory path and the file name.
    _, input_filename = os.path.split(input_path)
    input_camera_id = int(input_filename.split("_")[1])

    # The input file must follow a specific naming convention of ‘Camera_ID_cut_final’, to process each camera with a unique id
    pixel_input = read_input(input_path)
    reference = get_reference(input_camera_id, reference_path)

    # Geographic coordinates are formatted into a specific JSON format
    coord_output = transform(pixel_input, reference)
    formatted_output = generate_dassault_format(coord_output)
    write_output(
        json.dumps(formatted_output, indent=4),
        os.path.join(output_path, input_filename.split(".")[0] + "_transformed.json"),
    )


def get_reference(camera_id: int, reference_path: str) -> dict:
    """
    The function reads a CSV file containing reference points with their pixel and real-world coordinates, specified in EPSG3857 format. It returns a dictionary containing pixel
    coordinates and their corresponding real-world coordinates in EPSG 3857 format.
    """
    # Use https://epsg.io/ to check the accuracy of reference points

    reference_df = pd.read_csv(reference_path)
    relevant_ref = reference_df[reference_df["camera"] == camera_id]
    return {
        "pixel_coords": np.array(relevant_ref[["pixel_x", "pixel_y"]]).astype(
            np.float32
        ),
        "real_coords": np.array(relevant_ref[["epsg3857_x", "epsg3857_y"]]).astype(
            np.float32
        ),
    }


def read_input(input_path: str) -> dict:
    # This function reads a JSON file from a given input path and returns its contents as a dictionary object.

    with open(input_path) as input_file:
        input = json.load(input_file)
    return input


def write_output(output: str, output_path: str):
    with open(output_path, "w") as output_file:
        output_file.write(output)


def transform(pixel_input: dict, reference: dict) -> dict:
    """
    This function takes the pixel coordinates from the input data and applies a perspective transformation using a reference dictionary of pixel and
    real-world coordinates. The output of this function is a dictionary of transformed real-world centroid coordinates for each object detected in the input frames.
    """
    # Use OpenCV's ‘getPerspectiveTransform()’ function to obtain the transformation matrix
    TRANSFORMATION_MATRIX = cv2.getPerspectiveTransform(
        reference["pixel_coords"], reference["real_coords"]
    )
    # Transform pixel coordinates into real-world coordinates for each frame in the input data
    for _, frame_value in pixel_input.items():
        for frame_dict_key, frame_dict_value in frame_value.items():
            if frame_dict_key.strip() != "timestamp":
                x1 = float(frame_dict_value["x1"])
                x2 = float(frame_dict_value["x2"])
                y1 = float(frame_dict_value["y1"])
                y2 = float(frame_dict_value["y2"])

                # Calculate the centroid of each object detected in the frame using the transformed coordinates and stores it in the output dictionary
                x_centroid, y_centroid = (x1 + x2) / 2, (y1 + y2) / 2

                centroid_real_coords = cv2.perspectiveTransform(
                    np.array([(x_centroid, y_centroid)]).reshape(1, -1, 2),
                    TRANSFORMATION_MATRIX,
                ).reshape(-1, 2)
                frame_dict_value["x_centroid"] = str(centroid_real_coords[0, 0])
                frame_dict_value["y_centroid"] = str(centroid_real_coords[0, 1])

                # Vehicle type must be in capital (requirement from Dassault)
                # Vehicle type "train" is unavailable in Dassault, replace with "BUS"
                if frame_dict_value["type"] == "train":
                    frame_dict_value["type"] = "BUS"
                else:
                    frame_dict_value["type"] = frame_dict_value["type"].upper()

                # removes the original pixel coordinates, leaving only the transformed real-world centroid coordinates and the type of each object detected
                for k in ["x1", "x2", "y1", "y2", "class"]:
                    frame_dict_value.pop(k)

    return pixel_input


def generate_dassault_format(coord_output: dict) -> list:
    # This function takes the output of the transform function, and generates a list of data in a specific format expected by Dassault Systèmes software.

    formatted_output = []
    # creates a dictionary containing four keys
    for _, frame_value in coord_output.items():
        single_frame_data = {
            "timestamp": "",
            "id": [],
            "coordinates": [],
            "type": [],
        }
        # Processes a dictionary of raw object tracking data and stores the processed data in a list of dictionaries with one dictionary per frame
        for frame_dict_key, frame_dict_value in frame_value.items():
            if frame_dict_key == "timestamp":
                single_frame_data["timestamp"] = frame_dict_value
            else:
                single_frame_data["id"].append(int(frame_dict_key))
                single_frame_data["type"].append(frame_dict_value["type"])
                single_frame_data["coordinates"].append(
                    [
                        float(frame_dict_value["x_centroid"]),
                        float(frame_dict_value["y_centroid"]),
                        1.0,
                    ]
                )

        formatted_output.append(single_frame_data)

    return formatted_output
