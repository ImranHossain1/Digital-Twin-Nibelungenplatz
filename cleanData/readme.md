# JSON Data Cleaning Script

This script cleans and filters JSON data to remove objects with inadequate occurrences from camera feeds. The objective is to remove data points that show up less frequently across a predetermined number of frames. The updated JSON file is then stored with the cleansed data.

## Algorithm Overview

1. **Clean Data Function**: The `clean_data()` method accepts a list of frames and a `consecutive_threshold` as inputs. It determines IDs that do not meet the consecutive threshold by counting the instances of each ID across frames. Then, it deletes these IDs and the associated information from each frame.

2. **Input and Output Files**: The cleaned data is stored to an output file called "output/Camera_1_cut_final_transformed.json," while the input JSON data is fetched from a file named "input/Camera_1_cut_final_transformed.json."

3. **Consecutive Threshold**: The 'consecutive_threshold' is set to various values based on the camera source. The bare minimum of consecutive occurrences necessary for an object ID to be regarded as legitimate is specified by this threshold. This threshold can be changed to suit your needs for each camera feed.

## Usage

1. **Input Data**: Place the input JSON file in the specified directory (`input/`).

2. **Execution**: Open a terminal or command prompt and navigate to the directory containing the script. Run the script using the command:

   ```bash
   python clean_data.py
   ```
