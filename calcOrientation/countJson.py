import json

def count_json_objects(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    if isinstance(data, list):
        return len(data)
    else:
        return 0

file_path = 'Camera_12345_cut_final_7500_transformed.json'
json_object_count = count_json_objects(file_path)
print(f"The number of JSON objects in '{file_path}' is: {json_object_count}")
