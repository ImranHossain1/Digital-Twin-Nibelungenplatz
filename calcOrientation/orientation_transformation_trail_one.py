
import json
import numpy as np
import os
from datetime import datetime

def calculate_velocity(a, b, time_diff):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    vx = dx / time_diff
    vy = dy / time_diff
    return [vx, vy]

def calculate_orientation(velocity):
    return np.arctan2(velocity[1], velocity[0])

def timestamp_to_seconds(timestamp_str):
    timestamp_obj = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
    return timestamp_obj.timestamp()

# Remember to specify the correct file name
filename = "Camera_4_cut_final_cleaned.json"

# Expect Json like: [{timestamp, id[], coordinates[], type[]}]
with open(os.path.join(os.getcwd(), filename)) as f:
    data = json.load(f)

jsonList = []
prev_positions = {}

for i in range(len(data)):
    featuresDict = {
        "type": "MultiPoint",
        "coordinates": data[i]["coordinates"],
    }

    orients = []
    timestamp = timestamp_to_seconds(data[i]["timestamp"])  # Convert the timestamp to seconds
    for j, coord in enumerate(data[i]["coordinates"]):
        id_str = str(data[i]["id"][j])

        if id_str in prev_positions:
            prev_pos, prev_time = prev_positions[id_str]
            time_diff = timestamp - prev_time
            velocity = calculate_velocity(prev_pos, coord, time_diff)
            alpha = calculate_orientation(velocity)
            prev_positions[id_str] = (coord, timestamp)
        else:
            # Initialize for the first time
            prev_positions[id_str] = (coord, timestamp)
            alpha = 0.0

        o = [0, 0, alpha]
        orients.append(o)

    featuresDict["orientations"] = orients
    featuresDict["feature_id"] = data[i]["id"]
    featuresDict["feature_type"] = data[i]["type"]

    geoJsonDict = {
        "feature_type": "FeatureCollection",
        "features": [featuresDict],
    }

    allDict = {
        "timestamp": data[i]["timestamp"],
        "geoJson": geoJsonDict,
    }

    jsonList.append(allDict)

jsonFile = open(
    os.path.join(os.getcwd(), filename.replace("cleaned", "calculated")), "w"
)
jsonFile.write(json.dumps(jsonList))
jsonFile.close()
