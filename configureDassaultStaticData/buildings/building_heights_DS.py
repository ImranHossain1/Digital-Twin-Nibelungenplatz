# This script helps in configuring the height of the buildings
# since most of the buildings are missing the height parameter under their properties tag in the existing dataset.

import math
import json
import os

cwd = os.getcwd()
data = json.load(open(os.path.join(cwd, "buildings.geojson")))

# Define and initialize two variables DEFAULT_HEIGHT and DEFAULT_LEVELS as 3, meaning 3 meters and 3 stocks, respectively

# If the building ID doesn't have building:levels under properties,
# then set the building height as the product of DEFAULT_HEIGHT and DEFAULT_LEVELS.

# If it does have some value defined under building:levels,
# then set the building height as the product of DEFAULT_HEIGHT and the value of building:levels.

DEFAULT_HEIGHT = 3
DEFAULT_LEVELS = 3
for feature in data["features"]:
    ot = str(feature["properties"]["other_tags"]).replace('"', "")
    if ot is not None and "building:levels" in ot:
        dict_ot = {
            pair.split("=>")[0]: pair.split("=>")[1]
            for pair in ot.split(sep=",")
            if "=>" in pair
        }
        feature["properties"]["building_height"] = DEFAULT_HEIGHT * int(
            dict_ot["building:levels"]
        )
    else:
        feature["properties"]["building_height"] = DEFAULT_HEIGHT * DEFAULT_LEVELS

with open("cleaned_buildings.geojson", "w") as f:
    json.dump(data, f)
