import json
import yaml

# Load the JSON data
with open("example.json", "r") as json_file:
    json_data = json.load(json_file)

# Write the JSON data to a YAML file
with open("example.yml", "w") as yaml_file:
    yaml.dump(json_data, yaml_file, default_flow_style=False)
