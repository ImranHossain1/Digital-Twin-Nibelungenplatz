import os
from pixel_to_coord import pixel_to_coord


def bb_transformation(input_path: str, reference_path: str, output_path: str):
    pixel_to_coord(input_path, reference_path, output_path)


if __name__ == "__main__":
    # Remember to put yolo output (json files) in the input folder
    input_path = os.path.join(os.getcwd(), "input")
    output_path = os.path.join(os.getcwd(), "output")
    reference_path = os.path.join(os.getcwd(), "ref_points", "ref_points.csv")

    for file in os.listdir(input_path):
        if file.split(".")[-1] == "json":
            bb_transformation(
                os.path.join(input_path, file), reference_path, output_path
            )
