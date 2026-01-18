def compare_configs(expected: dict, actual: dict) -> dict:
    """
    Compare expected vs actual config dictionaries.
    Returns a dictionary describing drift.
    """
    drift = {
    "changed" : {},
    "missing" : [],
    "extra": []
    }
    
    #changed values
    for key in expected:
        if key in actual and expected[key] != actual[key]:
            drift["changed"][key] = {
            "expected": expected[key],
            "actual": actual[key]
            }
            
    
    #missing keys
    for key in expected:
        if key not in actual:
            drift["missing"].append(key)
        
    #Extra keys
    for key in actual:
        if key not in expected:
            drift["extra"].append(key)
    
    return drift