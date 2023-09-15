import json

# Define the box boundaries
box = {'xmin': 967596.583700508, 'xmax': 967803.7492728742, 'ymin': 6468558.8948148275, 'ymax': 6468728.366299554}

# Load the input JSON data
with open('input/Camera_1_cut_final_transformed.json') as file:
    data = json.load(file)

# Filter out the coordinates based on the box boundaries
filtered_data = []
for obj in data:
    coordinates = obj['coordinates']
    filtered_coordinates = []
    filtered_id = []
    filtered_type = []
    for coord, id_value, type_value in zip(coordinates, obj['id'], obj['type']):
        x, y, _ = coord
        if (
                box['xmin'] <= x <= box['xmax'] and
                box['ymin'] <= y <= box['ymax']):
            filtered_coordinates.append(coord)
            filtered_id.append(id_value)
            filtered_type.append(type_value)
    if filtered_coordinates:
        filtered_obj = {
            'timestamp': obj['timestamp'],
            'id': filtered_id,
            'coordinates': filtered_coordinates,
            'type': filtered_type
        }
        filtered_data.append(filtered_obj)
    else:
        # If the object has no valid coordinates, keep the original object in the filtered data
        filtered_data.append(obj)

# Save the filtered data to a new JSON file
with open('output/Camera_1_cut_final_transformed.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)
