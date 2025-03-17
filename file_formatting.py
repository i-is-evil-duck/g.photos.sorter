# file_formatting.py
import os

def format_json_files(json_folder):
    for filename in os.listdir(json_folder):
        if filename.endswith('.json'):
            base_name = filename.split('.')[0]  # Extract base name (e.g., 0001)
            formatted_name = f"{base_name}.json"  # Format to 0001.json
            original_path = os.path.join(json_folder, filename)
            formatted_path = os.path.join(json_folder, formatted_name)
            
            if original_path != formatted_path:
                os.rename(original_path, formatted_path)
                print(f"Renamed {filename} to {formatted_name}")
