import json

def update_person_orientations(json_data):
    for entry in json_data:
        features = entry['geoJson']['features'][0]

        for i in range(len(features['feature_type'])):
            if features['feature_type'][i] == 'PERSON' or  features['feature_type'][i] == 'BICYCLE':
                features['orientations'][i] = [-1.5, 0, 0]

    return json_data

# Read the JSON data from 'Cam1.json'
with open('Camera_12345_cut_final_7500_calculated.json', 'r') as file:
    json_data = json.load(file)

# Update the JSON data
updated_json_data = update_person_orientations(json_data)

# Save the updated JSON data to 'Cam1_Person_Output.json'
with open('AllCameraMergedWithPerson.json', 'w') as file:
    json.dump(updated_json_data, file, indent=4)

print("Updated JSON data has been saved.")
