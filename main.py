from drift.loader import load_config
from drift.comparator import detect_drift


def main():
    expected = load_config("sample_configs/expected.json")
    actual = load_config("sample_configs/actual.json")
    
    drift = detect_drift(expected, actual)
    
    if not drift:
        print("No config drift detected")
        return
    
    print("Config drift detected:\n")
    for system, differences in drift.items():
        print(f"{system}:")
        for key, values in differences.items():
            print(f" - {key}: expected {values['expected']}, found {values['actual']}")

if __name__ == "__main__":
    main()