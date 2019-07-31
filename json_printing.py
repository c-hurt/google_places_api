import json

def json_pprint(json_values):
    return json.dumps(json_values, indent=4, sort_keys=True)