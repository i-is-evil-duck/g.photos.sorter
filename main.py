# main.py
import os
from file_formatting import format_json_files
from file_comparison import compare_files
from file_moving import move_files, ensure_directories

def get_directory_input():
    # Prompt the user to specify the root directory
    root_directory = input("Please specify the root directory (e.g., 'C:\\Users\\Ducky\\Pictures\\Saved Pictures\\roblox takeout-20250316T013841Z-001\\Takeout\\Google Photos\\Photos from 2024'): ")

    if not os.path.isdir(root_directory):
        print(f"Error: The specified root directory '{root_directory}' does not exist.")
        exit(1)

    # Assuming the json and media directories are within the root directory
    json_folder = os.path.join(root_directory, 'json')
    media_folder = os.path.join(root_directory, 'media')

    # Check if both subdirectories exist
    if not os.path.isdir(json_folder):
        print(f"Error: 'json' folder not found in {root_directory}")
        exit(1)
    
    if not os.path.isdir(media_folder):
        print(f"Error: 'media' folder not found in {root_directory}")
        exit(1)

    return root_directory, json_folder, media_folder

def main():
    # Step 1: Get user input for the root directory
    root_directory, json_folder, media_folder = get_directory_input()

    # File paths for storing the lists and matched pairs
    media_output_file = 'media.txt'
    json_output_file = 'json.txt'
    matched_file = 'matched.txt'

    # Matched folders (automatically created under the root directory)
    matched_json_folder = os.path.join(root_directory, 'matched', 'json')
    matched_media_folder = os.path.join(root_directory, 'matched', 'media')

    # Step 2: Format JSON files
    print("Formatting JSON files...")
    format_json_files(json_folder)

    # Step 3: Compare files and list matched pairs
    print("Comparing files...")
    compare_files(media_folder, json_folder, media_output_file, json_output_file, matched_file)

    # Step 4: Ensure the matched directories exist
    ensure_directories(matched_json_folder, matched_media_folder)

    # Step 5: Move matched files
    print("Moving matched files...")
    move_files(matched_file, json_folder, media_folder, matched_json_folder, matched_media_folder)

if __name__ == '__main__':
    main()
