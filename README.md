#Config Drift Detector (Python)

A Python tool that detects configuration drift by comparing expected and actual system configuration files.

## Overview

Configuration drift occurs when a system's actual configuration deviates from its intended or expected state. This tool helps identify drift by analyzing two configuration files and reporting:

- Changed values
- Missing config keys
- Extra config keys 

The project is inspired by real world infrastructure and systems engineering workflows where config consistency is critical.

## Features

- Loads config data from JSON files
- Compares expected vs actual configuration
- Detects:
	- Changed values
	- Missing keys
	- Extra keys 
- Clear, readable outputs
- Modular Python design

## Project Structure
config-drift-detector/
│
├── main.py 
├── drift/
│ ├── loader.py 
│ ├── comparer.py 
│ └── init.py
│
└── sample_configs/
├── expected.json 
└── actual.json 

## How It Works

1. Load the expected and actual config files
2. Compare config keys and values
3. Report:
   - Values that changed
   - Keys missing from the actual config
   - Extra keys present in the actual config

## Example Output
=== CONFIG DRIFT REPORT ===

Changed Values:
- PLC_1: expected={'ip': '192.168.1.10', 'firmware': 'v2.1', 'timeout': 500} actual={'ip': '192.168.1.11', 'firmware': 'v2.0', 'timeout': 500}

## Why This Project

This project was built to strengthen Python fundamentals while solving a realistic engineering problem related to system reliability.

## Possible Improvements

- Support nested configuration structures
- Add CLI arguments for custom file paths
- Export results as JSON
- Add unit tests for drift comparison logic

## Technologies Used

- Python 3
- JSON
- Git / GitHub