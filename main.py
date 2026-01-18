from drift.loader import load_config
from drift.comparer import compare_configs


def main():
    expected = load_config("sample_configs/expected.json")
    actual = load_config("sample_configs/actual.json")
    
    drift = compare_configs(expected, actual)
    print("\n=== CONFIG DRIFT REPORT ===")
    
    if drift["changed"]:
        print("\nChanged Values:")
        for key, values in drift["changed"].items():
            print(f"- {key}: expected={values['expected']} actual={values['actual']}")
    
        if drift["missing"]:
            print("\nMissing keys:")
            for key in drift["missing"]:
                print(f"- {key}")

    if drift["extra"]:
        print("\nExtra keys:")
        for key in drift["extra"]:
            print(f"- {key}")

    if not any(drift.values()):
        print("\nNo drift detected.")

if __name__ == "__main__":
    main()