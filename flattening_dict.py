def flatten_dict(nested_dict, parent_key=''):
    flat_dict = {}
    
    for key, value in nested_dict.items():
        # Build the new key with a dot separator
        new_key = f"{parent_key}.{key}" if parent_key else key
        
        if isinstance(value, dict):
            # If value is a dict, recurse
            flat_dict.update(flatten_dict(value, new_key))
        else:
            # If value is a primitive, add to result
            flat_dict[new_key] = value
            
    return flat_dict

data = {"a": {"b": 1, "c": {"d": 2}}, "e": 3}
print(f"The single level dictionary is : {flatten_dict(data)}")