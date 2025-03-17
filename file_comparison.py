# file_comparison.py
import os

def list_files(directory, output_file):
    with open(output_file, 'w') as file:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                file.write(f"{filename}\n")

def compare_files(media_folder, json_folder, media_output_file, json_output_file, matched_file):
    # List files in /media and /JSON_Files
    list_files(media_folder, media_output_file)
    list_files(json_folder, json_output_file)

    # Read the file names from media.txt and json.txt
    with open(media_output_file, 'r') as file:
        media_files = {line.strip() for line in file.readlines()}

    with open(json_output_file, 'r') as file:
        json_files = {line.strip() for line in file.readlines()}

    # Find matching files based on the name (ignoring extensions)
    matched_files = []
    for json_file in json_files:
        # Remove the '.json' extension to compare with media files
        base_name = json_file.replace('.json', '')

        # Check if there is a corresponding media file with the same base name
        for media_file in media_files:
            if media_file.startswith(base_name):
                matched_files.append(f"{json_file} and {media_file}")

    # Write the matched files to matched.txt
    with open(matched_file, 'w') as file:
        for match in matched_files:
            file.write(f"{match}\n")

    print(f"Matched files have been saved to {matched_file}")
