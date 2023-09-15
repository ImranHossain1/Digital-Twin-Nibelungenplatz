import json

def count_consecutive_appearances(json_data, target_id):
    consecutive_count = 0
    start_object = None

    for entry in json_data:
        ids = entry["id"]

        if target_id in ids:
            if consecutive_count == 0:
                start_object = entry["timestamp"]
            consecutive_count += 1
        else:
            if consecutive_count > 0:
                end_object = entry["timestamp"]
                print(
                    f"ID {target_id} appears from {start_object} to {end_object} consecutively {consecutive_count} times.")
            consecutive_count = 0

    if consecutive_count > 0:
        end_object = json_data[-1]["timestamp"]
        print(
            f"ID {target_id} appears from {start_object} to {end_object} consecutively {consecutive_count} times.")


def main():
    input_file = "input/Cars/Cam1_demo.json"
    with open(input_file, "r") as file:
        json_data = json.load(file)

    unique_ids = set()
    for entry in json_data:
        unique_ids.update(entry["id"])

    for target_id in unique_ids:
        count_consecutive_appearances(json_data, target_id)

if __name__ == "__main__":
    main()
