import json

input_file = 'AllCameraMergedWithPerson.json'
output_file = 'onlyPersonsMarged.json'

# Read the JSON data from the input file
with open(input_file, 'r') as infile:
    data = json.load(infile)

# Filter out objects without required fields
filtered_data = [obj for obj in data if any(obj['geoJson']['features'][0][key] for key in ['coordinates', 'orientations', 'feature_id', 'feature_type'])]

# Write the filtered data to the output file
with open(output_file, 'w') as outfile:
    json.dump(filtered_data, outfile, indent=4)
