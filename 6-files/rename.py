import os
import sys

def rename_files(folder_path, new_name_addition):
    # Get list of files in the folder
    files = os.listdir(folder_path)
    
    # Iterate through each file
    for file in files:
        # Construct the new filename by adding the new name addition to the end
        new_name = os.path.splitext(file)[0] + new_name_addition + os.path.splitext(file)[1]
        
        # Rename the file
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
        print(f"Renamed '{file}' to '{new_name}'")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py folder_path new_name_addition")
        sys.exit(1)

    # Get the folder path and the new name addition from command-line arguments
    folder_path = sys.argv[1]
    new_name_addition = sys.argv[2]

    # Call the function to rename files in the specified folder
    rename_files(folder_path, new_name_addition)
