import math
import json
from shapely.geometry import Point, Polygon


def calculate_distance(coord1, coord2):
    x1, y1, _ = coord1
    x2, y2, _ = coord2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def merge_json_data(json_data1, json_data2, threshold_distance, adjust_ID):
    merged_data = {
        "timestamp": json_data1["timestamp"],
        "id": [],
        "coordinates": [],
        "type": []
    }
    unmatched_indices = set(range(len(json_data2["coordinates"])))
    print(f"\n\nWorking with json_data1 timestamp: {json_data1['timestamp']}")
    print(f"Working with json_data2 timestamp: {json_data2['timestamp']}")
    for i, coord1 in enumerate(json_data1["coordinates"]):
        matched_index = None
        for j, coord2 in enumerate(json_data2["coordinates"]):
            if j in unmatched_indices and json_data1["type"][i] == json_data2["type"][j]:
                distance = calculate_distance(coord1, coord2)
                if distance <= threshold_distance:
                    matched_index = j
                    break

        if matched_index is not None:
            unmatched_indices.remove(matched_index)
            merged_data["id"].append(json_data1["id"][i])
            merged_data["coordinates"].append([
                coord1[0],
                coord1[1],
                coord1[2]
            ])
            merged_data["type"].append(json_data1["type"][i])
            print(
                f'Matched data from json_data1 id={json_data1["id"][i]} with json_data2 id={json_data2["id"][matched_index]}')
        else:
            merged_data["id"].append(json_data1["id"][i])
            merged_data["coordinates"].append(coord1)
            merged_data["type"].append(json_data1["type"][i])
            print(f'Unmatched data from json_data1 id={json_data1["id"][i]}')

    for j in unmatched_indices:
        json_data2["id"][j] += adjust_ID
        merged_data["id"].append(json_data2["id"][j])
        merged_data["coordinates"].append(json_data2["coordinates"][j])
        merged_data["type"].append(json_data2["type"][j])
        print(
            f'Added unmatched data from json_data2 with new id={json_data2["id"][j]}')

    return merged_data


def merge_and_save_json(json_file1, json_file2, threshold_distance, output_file, adjust_ID):
    with open(json_file1, 'r') as file1, open(json_file2, 'r') as file2:
        json_data1 = json.load(file1)
        json_data2 = json.load(file2)

    merged_data = []
    for data1, data2 in zip(json_data1, json_data2):
        merged_data.append(merge_json_data(
            data1, data2, threshold_distance, adjust_ID))

    with open(output_file, 'w') as file:
        json.dump(merged_data, file)


# Example usage
json_file1 = 'input/Cam1.json'
json_file2 = 'input/Cam2.json'
threshold_distance = 20.0  # Adjust this value based on your requirements
output_file = 'output/Cam12.json'
adjust_ID = 10000
# Adjust cam2 ID by adding 10000
# Adjust cam3 ID by adding 20000
# Adjust cam4 ID by adding 30000
# Adjust cam5 ID by adding 40000
merge_and_save_json(json_file1, json_file2,
                    threshold_distance, output_file, adjust_ID)
