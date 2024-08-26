import os
import re

# Path to the parent directory containing all the subfolders
base_dir = r'C:\Users\andrew\Desktop\textures_to_rename'

# Function to extract the number from the folder name
def extract_number_from_folder_name(folder_name):
    match = re.search(r'\d+', folder_name)
    return match.group() if match else None

# Iterate over each subfolder in the base directory
for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    
    # Check if it's a directory
    if os.path.isdir(folder_path):
        folder_number = extract_number_from_folder_name(folder_name)
        
        # Continue only if folder_number is found
        if folder_number:
            files_to_keep = None
            
            # List all files in the folder
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.fbx'):
                    # Check if the file name contains the folder number
                    if folder_number in file_name:
                        files_to_keep = file_name
            
            # Delete all files except the one to keep
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if file_name.endswith('.fbx') and file_name != files_to_keep:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")

print("Operation completed.")



## author='Andrew_Sutherland'
## author_email='afxsutherland@gmail.com'