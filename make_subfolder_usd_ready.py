import os

# Define the path to the directory
directory_path = r'C:\Users\andrew\Desktop\textures_to_rename'

# Function to replace spaces and dashes in folder names with underscores
def rename_folders(path):
    for folder_name in os.listdir(path):
        old_folder_path = os.path.join(path, folder_name)
        if os.path.isdir(old_folder_path):
            # Replace spaces and dashes with underscores
            new_folder_name = folder_name.replace(' ', '_').replace('-', '_')
            new_folder_path = os.path.join(path, new_folder_name)
            
            if old_folder_path != new_folder_path:
                os.rename(old_folder_path, new_folder_path)
                print(f'Renamed: {old_folder_path} -> {new_folder_path}')

# Run the rename function
rename_folders(directory_path)




## author='Andrew_Sutherland'
## author_email='afxsutherland@gmail.com'