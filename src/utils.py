import json, os

# Json read and write functions
# Read
def load_from_json(filename):
    with open(filename, 'r') as json_file:
        item_list = json.load(json_file)
    return item_list


# Write
def write_to_json(data, filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            json.dump('', file)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

