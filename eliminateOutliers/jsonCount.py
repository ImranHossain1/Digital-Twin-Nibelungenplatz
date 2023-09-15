import json


def count_json_objects(json_array):
    try:
        data = json.loads(json_array)
        if isinstance(data, list):
            return len(data)
        else:
            return 0
    except json.JSONDecodeError:
        return 0


# Read JSON data from file
with open('input/Camera_5_cut_final_transformed.json') as file:
    json_data = file.read()

# Count JSON objects
count = count_json_objects(json_data)
print(f"Number of JSON objects: {count}")
