#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import os

def convert_json_to_csv():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Input and output file paths
    json_file = os.path.join(current_dir, 'idiom-4-char.json')
    csv_file = os.path.join(current_dir, 'idiom-4-char.csv')
    
    try:
        # Read JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Write to CSV file
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            # Define CSV writer
            writer = csv.DictWriter(f, fieldnames=['word', 'pinyin', 'derivation', 
                                                 'explanation', 'example', 'abbreviation'])
            
            # Write header
            writer.writeheader()
            
            # Write data rows
            writer.writerows(data)
            
        print(f"Successfully converted {json_file} to {csv_file}")
        print(f"Total four-character idioms processed: {len(data)}")
        
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    convert_json_to_csv() 