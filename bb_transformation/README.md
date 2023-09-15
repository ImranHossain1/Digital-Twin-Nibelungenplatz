# Pixel to Coordinate Transformation

Transformation of pixel coordinates to real-world coordinates using a reference dataset. The reference dataset contains the corresponding pixel and real-world coordinates for a specific camera. The output is another JSON file containing the transformed coordinates in a format that is compatible with Dassault Systemes software.

## Dependencies

  - pandas
  - OpenCV(cv2)
  -  NumPy


## Input and Output Formats

### Input Format
The input JSON file should have the following format:

```
"frame1": {
    "timestamp": "2022-01-20T20:09:55.000Z",
    "1": {
      "type": "car",
      "class": "2",
      "x1": "26",
      "y1": "138",
      "x2": "70",
      "y2": "167"
    },
}
```
### Output Format
The output JSON file has the following format:

```
[
    {
        "timestamp": "2022-01-20T20:09:55.000Z",
        "id": [
            1,
            2,
            3,
            ...
        ],
        "coordinates": [
            [
                967764.1987389801,
                6468677.19386809,
                1.0
            ],
            [
                967763.8077150271,
                6468694.298630416,
                1.0
            ],
            [
                967733.9523218535,
                6468696.157381911,
                1.0
            ],
           
        ],
        "type": [
            "car",
            "bus",
            "car",
        ]
    }

]
```

## Setup and Execution

1. Clone DTN Main Repo

```
git clone git@gitlab.informatik.fb2.hs-intern.de:kweronek/dtn.git
```
2. Install the required packages:
```
pip install -r requirements.txt
```
3. Place your input files in the 'input' directory. The input files should be in JSON format. In order for the program to process each camera with a unique id, the input file must follow a specific naming convention of ‘Camera_ID_cut_final’. This convention allows the program to distinguish between input files belonging to different cameras.

4. Place your reference points CSV file in the 'ref_points' directory. The CSV file should contain the reference points for each camera, with columns for camera ID, pixel X coordinate, pixel Y coordinate, EPSG3857 X coordinate, and EPSG3857 Y coordinate.

5. Run the bb_transformation.py script to transform the bounding box coordinates from pixel coordinates to EPSG3857 coordinates. The transformed output files will be saved in the 'output' directory.You can run the script for a single input file like this:
```
python bb_transformation.py 
```

- Please refer to the [code documentation](../bb_transformation/pixel_to_coord.py) for more information.
 
## Known Bugs

- Thus far, no bugs have been reported.