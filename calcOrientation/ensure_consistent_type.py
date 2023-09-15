import json
import os

# Remember to specify the correct file name
filename = "Camera_12345_cut_final_7500_transformed.json"

with open(os.path.join(os.getcwd(), filename)) as f:
    data = json.load(f)

vehicles = dict()
jsonList = []
i = 0
while i < len(data):
    frame = dict()
    # Timestamp: ok
    frame["timestamp"] = data[i]["timestamp"]
    # Id: ok
    frame["id"] = data[i]["id"]
    # Coordinates: ok
    frame["coordinates"] = data[i]["coordinates"]
    # Fix type
    j = 0
    types = []
    while j < len(data[i]["id"]):
        if str(data[i]["id"][j]) not in vehicles:
            vehicles[str(data[i]["id"][j])] = data[i]["type"][j]
        types.append(vehicles.get(str(data[i]["id"][j])))
        j += 1

    frame["type"] = types
    jsonList.append(frame)
    i += 1

jsonFile = open(
    os.path.join(os.getcwd(), filename.replace("transformed", "cleaned")), "w"
)
jsonFile.write(json.dumps(jsonList))
jsonFile.close()
