import json
import numpy as np
import os

# returns alpha the z-axis orientation. Use like this: orientation = [0, 0, alpha]
def orientation(a, b, prevAlpha):
    #Check if difference too small to uvoid unnecessary orientation changing
    x_diff = (abs(a[0] - b[0]))
    y_diff = (abs(a[1] - b[1]))

    if x_diff < 1 and y_diff < 1:
        return prevAlpha

    # special cases
    if a == b:
        return prevAlpha
    if a[0] == b[0]:
        if a[1] < b[1]:
            return np.pi
        else:
            return 0
    if a[1] == b[1]:
        if a[0] > b[0]:
            return np.pi / 2
        else:
            return -1 * (np.pi / 2)

    # regular case
    hyp = np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    side = abs(b[1] - a[1])
    x = side / hyp

    if a[0] < b[0] and a[1] < b[1]:  # q1
        alpha = np.arcsin(x)
        return -1 * (np.pi / 2 + alpha)
    if a[0] < b[0] and a[1] > b[1]:  # q4
        alpha = np.arccos(x)
        return -1 * alpha
    if a[0] > b[0] and a[1] > b[1]:  # q3
        alpha = np.arccos(x)
        return alpha
    if a[0] > b[0] and a[1] < b[1]:  # q2
        alpha = np.arcsin(x)
        return np.pi / 2 + alpha


def getNextCoordinate(index, id):
    index += 1
    while index < len(data):
        j = 0
        while j < len(data[index]["id"]):
            if data[index]["id"][j] == id:
                return data[index]["coordinates"][j]
            j += 1
        index += 1
    return [0, 0, 0]


# Remember to specify the correct file name
filename = "Camera_12345_cut_final_7500_cleaned.json"

# Expect Json like: [{timestamp, id[], coordinates[], type[]}]
with open(os.path.join(os.getcwd(), filename)) as f:
    data = json.load(f)

jsonList = []
prevAlpha = dict()

i = 0
while i < len(data):
    featuresDict = dict()
    geoJsonDict = dict()
    allDict = dict()

    featuresDict["type"] = "MultiPoint"
    featuresDict["coordinates"] = data[i]["coordinates"]

    orients = []
    j = 0
    while j < len(data[i]["coordinates"]):
        id_str = str(data[i]["id"][j])
        x1 = data[i]["coordinates"][j][0]
        y1 = data[i]["coordinates"][j][1]
        p1 = [x1, y1]

        next = getNextCoordinate(i, data[i]["id"][j])
        p2 = [next[0], next[1]]
        if p2 == [0, 0]:
            p2 = p1

        prev = 0
        if id_str in prevAlpha:
            prev = prevAlpha.get(id_str)

        alpha = orientation(p1, p2, prev)

        if id_str not in prevAlpha:
            prevAlpha.update({id_str: alpha})
        else:
            prevAlpha[id_str] = alpha
        o = [0, 0, alpha]

        orients.append(o)
        j += 1

    featuresDict["orientations"] = orients
    featuresDict["feature_id"] = data[i]["id"]
    featuresDict["feature_type"] = data[i]["type"]
    geoJsonDict["feature_type"] = "FeatureCollection"
    geoJsonDict["features"] = [featuresDict]

    allDict["timestamp"] = data[i]["timestamp"]
    allDict["geoJson"] = geoJsonDict

    jsonList.append(allDict)
    i += 1

jsonFile = open(
    os.path.join(os.getcwd(), filename.replace("cleaned", "calculated")), "w"
)
jsonFile.write(json.dumps(jsonList))
jsonFile.close()
