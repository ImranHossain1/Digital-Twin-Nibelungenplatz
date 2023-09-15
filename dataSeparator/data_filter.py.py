import json

# Load the JSON data from the input file
with open('input/cam1_7500.json', 'r') as file:
    data = json.load(file)

# Filter out the entries with "type" equal to "bicycle" within each frame
filtered_data = {}
for frame, frame_data in data.items():
    filtered_frame_data = {'timestamp': frame_data['timestamp']}
    for key, value in frame_data.items():
        if key != 'timestamp' and isinstance(value, dict) and (value.get('type') == 'bicycle'):
            filtered_frame_data[key] = value
    filtered_data[frame] = filtered_frame_data

# Create a new dictionary with the filtered data
output_data = filtered_data

# Write the output data to a new JSON file
with open('output/Camera_1_cut_final.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=2)
