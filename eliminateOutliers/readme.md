# GeoJSON Data Filtering

This script processes a GeoJSON file containing location data from a camera feed. It filters out data points that fall outside a specified bounding box. The filtered data is then saved to a new GeoJSON file.

## How It Works

The script performs the following steps:

1. **Bounding Box Definition**: A bounding box is defined with four boundary values: `xmin`, `xmax`, `ymin`, and `ymax`. This box represents a geographical region of interest.

Our boundary box:
`xmin`: 967596.583700508
`xmax`: 967803.7492728742
`ymin`: 6468558.8948148275
`ymax`: 6468728.366299554

2. **Loading Input Data**: The script reads GeoJSON data from the file 'input/Camera_1_cut_final_transformed.json' using the `json.load()` function.

3. **Filtering Coordinates**: The script determines if the coordinates of each object in the input data are within the specified bounding box for each object. The filtered coordinates list also includes the associated ID and type values for each coordinate that satisfies the box bounds.

4. **Creating Filtered Objects**: A new object is created with the original timestamp, filtered ID, filtered coordinates, and filtered type if an object has correct filtered coordinates. The list of the filtered data now includes this additional object.

5. **Saving Filtered Data**: Using the 'json.dump()' function with an indentation of 4 spaces, the filtered data, which contains both filtered and preserved objects, is written to a new GeoJSON file called 'output/Camera_1_cut_final_transformed.json'.

## How to Run

1. **Prerequisites**: Ensure you have Python installed on your system.

2. **Data Preparation**: The `Camera_1_cut_final_transformed.json` file should be put in the `input` directory of the script's directory. Make a `output` directory to store the filtered data.

3. **Execution**: Locate the directory containing the script by opening a terminal or command prompt. Use this command to run the script:

   ```bash
   python eliminate-outliers.py
   ```
