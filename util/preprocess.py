import os
import sys
import shutil
import re
import subprocess

def extract_strings(input_folder_path, output_folder_path):
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder_path):
        # Check if the file is a regular file
        if os.path.isfile(os.path.join(input_folder_path, filename)):
            # Run the strings command on the file and capture the output
            output = subprocess.check_output(['strings', os.path.join(input_folder_path, filename)])

            # Decode the output to a string and save it to a .txt file with the same name in the output folder
            with open(os.path.join(output_folder_path, os.path.splitext(filename)[0] + '.txt'), 'w') as f:
                f.write(output.decode('utf-8'))


if __name__ == "__main__":
    # Get the directory containing the library files from command-line argument
    if len(sys.argv) > 1:
        source_directory = sys.argv[1]
    else:
        print("Please provide the directory containing the library files as a command-line argument.")
        sys.exit(1)

    destination_directory = '../data/dataset_txt'
    
    extract_strings(source_directory, destination_directory)
    print("Strings extracted.")
