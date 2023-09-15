
import pyproj
import json
from datetime import datetime

def transform_coordinates(input_data):
    epsg3857 = pyproj.CRS("EPSG:3857")
    wgs84 = pyproj.CRS("EPSG:4326")
    transformer = pyproj.Transformer.from_crs(epsg3857, wgs84, always_xy=True)
    
    output_data = {
        "timestamp": input_data["timestamp"],
        "geoJson": {
            "feature_type": "FeatureCollection",
            "features": [
                {
                    "type": "MultiPoint",
                    "coordinates": input_data["coordinates"],
                    "orientations": [],
                    "feature_id": input_data["id"],
                    "feature_type": input_data["type"],
                }
            ]
        }
    }
    
    transformed_coordinates = []
    for coord in input_data["coordinates"]:
        lon, lat = transformer.transform(coord[0], coord[1])
        transformed_coordinates.append([lon, lat, coord[2]])
    
    output_data["geoJson"]["features"][0]["coordinates"] = transformed_coordinates
    
    return output_data

def process_json_file(input_filename, output_filename):
    with open(input_filename, "r") as f:
        input_data = json.load(f)
    
    transformed_data = transform_coordinates(input_data)
    
    with open(output_filename, "w") as f:
        json.dump(transformed_data, f, indent=4)

# Configure input and output filenames
input_filename = "input.json"  # Change this to your input JSON file
output_filename = "output_transformed.json"  # Change this to the desired output filename

# Process the JSON file and save the transformed data
process_json_file(input_filename, output_filename)

