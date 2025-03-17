# file_moving.py
import os
import shutil

def ensure_directories(matched_json_folder, matched_media_folder):
    os.makedirs(matched_json_folder, exist_ok=True)
    os.makedirs(matched_media_folder, exist_ok=True)

def move_files(matched_file, json_source_folder, media_source_folder, matched_json_folder, matched_media_folder):
    with open(matched_file, 'r') as file:
        matches = file.readlines()

    # Process each match and move the files
    for match in matches:
        # Extract the JSON file and media file from the matched pair
        json_file, media_file = match.strip().split(' and ')

        # Define the source paths for both files
        json_source = os.path.join(json_source_folder, json_file)
        media_source = os.path.join(media_source_folder, media_file)

        # Define the destination paths
        json_dest = os.path.join(matched_json_folder, json_file)
        media_dest = os.path.join(matched_media_folder, media_file)

        # Move the files if they exist
        if os.path.exists(json_source):
            shutil.move(json_source, json_dest)
            print(f"Moved {json_file} to {matched_json_folder}")
        else:
            print(f"Warning: {json_file} not found in {json_source}!")

        if os.path.exists(media_source):
            shutil.move(media_source, media_dest)
            print(f"Moved {media_file} to {matched_media_folder}")
        else:
            print(f"Warning: {media_file} not found in {media_source}!")
