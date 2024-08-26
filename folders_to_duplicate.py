import os
import shutil

def duplicate_folders(base_path):
    # Iterate over each item in the base directory
    for subfolder_name in os.listdir(base_path):
        subfolder_path = os.path.join(base_path, subfolder_name)
        
        # Check if it's a directory
        if os.path.isdir(subfolder_path):
            # Count the number of .fbx files in the subfolder
            fbx_files = [f for f in os.listdir(subfolder_path) if f.endswith('.fbx')]
            num_fbx_files = len(fbx_files)
            
            # Duplicate the subfolder based on the number of .fbx files
            for i in range(1, num_fbx_files + 1):
                new_folder_name = f"{subfolder_name}_{i}"
                new_folder_path = os.path.join(base_path, new_folder_name)
                
                # Copy the directory to the new location
                shutil.copytree(subfolder_path, new_folder_path)
                print(f"Created: {new_folder_path}")

# Define the base path to your folder
base_path = r"C:\Users\andrew\Desktop\folders_to_duplicate"

# Run the function
duplicate_folders(base_path)



## author='Andrew_Sutherland'
## author_email='afxsutherland@gmail.com'