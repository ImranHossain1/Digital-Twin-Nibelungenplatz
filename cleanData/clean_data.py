import json

def clean_data(frames, consecutive_threshold):
    # Count occurrences of each ID
    id_counts = {}
    for frame in frames:
        ids = frame['id']
        for id in ids:
            id_counts[id] = id_counts.get(id, 0) + 1

    # Find IDs to delete
    ids_to_delete = []
    for id, count in id_counts.items():
        if count < consecutive_threshold:
            ids_to_delete.append(id)

    # Remove IDs and corresponding data from each frame
    for frame in frames:
        ids = frame['id']
        coordinates = frame['coordinates']
        types = frame['type']

        cleaned_ids = []
        cleaned_coordinates = []
        cleaned_types = []

        for id, coord, type in zip(ids, coordinates, types):
            if id not in ids_to_delete:
                cleaned_ids.append(id)
                cleaned_coordinates.append(coord)
                cleaned_types.append(type)

        frame['id'] = cleaned_ids
        frame['coordinates'] = cleaned_coordinates
        frame['type'] = cleaned_types

    return frames

input_file = 'input/Cars/Camera_12345_cut_final_transformed.json'
output_file = 'output/onlyCars/Camera_12345_cut_final_transformed.json'

# Load input data from file
with open(input_file) as f:
    input_data = json.load(f)

consecutive_threshold = 50

#Camera 1 = consecutive_threshold = 50
#Camera 2 = consecutive_threshold = 50
#Camera 3= consecutive_threshold = 50
#Camera 4 = consecutive_threshold = 75
#Camera 5 = consecutive_threshold = 50

cleaned_data = clean_data(input_data, consecutive_threshold)

# Write the cleaned data to the output file
with open(output_file, 'w') as f:
    json.dump(cleaned_data, f, indent=4)
