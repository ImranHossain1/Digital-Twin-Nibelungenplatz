import json

# Load the JSON data from the input file
with open('cam1.json', 'r') as file:
    data = json.load(file)

# Define the types to filter (e.g., 'bicycle' and 'person')
types_to_filter = ['car', 'bicycle']

# Filter out the entries with specified types within each frame
filtered_data = {}
for frame, frame_data in data.items():
    filtered_frame_data = {'timestamp': frame_data['timestamp']}
    for key, value in frame_data.items():
        if key != 'timestamp' and isinstance(value, dict) and value.get('type') in types_to_filter:
            filtered_frame_data[key] = value
    filtered_data[frame] = filtered_frame_data

# Create a new dictionary with the filtered data
output_data = filtered_data

# Write the output data to a new JSON file
with open('cam1_final.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=2)
