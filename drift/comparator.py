def detect_drift(expected, actual):
    drift = {}
    
    for system, expected_values in expected.items():
        actual_values = actual.get(system)
        
        if actual_values is None:
            drift[system] = {"missing": "System not found"}
            continue
        
        differences = {}
        
        for key, expected_value in expected_values.items():
            actual_value = actual_values.get(key)
            
            if actual_value != expected_value:
                differences[key] = {
                    "expected": expected_value,
                    "actual": actual_value
                   }
            
        if differences:
            drift[system] = differences
    
    return drift