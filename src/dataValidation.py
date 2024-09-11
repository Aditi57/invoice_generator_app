
def validate_json_structure(json_data, schema, path=""):
   
    for key, expected_type in schema.items():
        current_path = f"{path}.{key}" if path else key  # Track path for nested keys

        if key not in json_data:
            return False, f"Missing key: {current_path}"

        value = json_data[key]

        # If expected type is dict, recursively validate the nested dictionary
        if isinstance(expected_type, dict):
            if not isinstance(value, dict):
                return False, f"Key {current_path} should be a dict, but got {type(value).__name__}"
            is_valid, error = validate_json_structure(value, expected_type, current_path)
            if not is_valid:
                return False, error

        # If expected type is list, validate the list and each of its items
        elif isinstance(expected_type, list):
            if not isinstance(value, list):
                return False, f"Key {current_path} should be a list, but got {type(value).__name__}"
            for idx, item in enumerate(value):
                item_path = f"{current_path}[{idx}]"
                is_valid, error = validate_json_structure(item, expected_type[0], item_path)
                if not is_valid:
                    return False, error

        # Check if the value matches the expected type
        elif not isinstance(value, expected_type):
            return False, f"Key {current_path} should be of type {expected_type.__name__}, but got {type(value).__name__}"

    return True, "JSON structure is valid"

