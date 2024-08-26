import os
import shutil

# Define the path to the parent directory
parent_directory = r'C:\Users\andrew\Desktop\textures_to_rename'

def move_fbx_files(source_dir, target_dir):
    for root, dirs, files in os.walk(source_dir):
        for file_name in files:
            if file_name.lower().endswith('.fbx'):
                old_file_path = os.path.join(root, file_name)
                new_file_path = os.path.join(target_dir, file_name)
                
                # Move file to the target directory
                if not os.path.exists(new_file_path):
                    shutil.move(old_file_path, new_file_path)
                    print(f'Moved: {old_file_path} -> {new_file_path}')
                else:
                    print(f'Skipped (file already exists): {new_file_path}')

# Run the move function
move_fbx_files(parent_directory, parent_directory)





## author='Andrew_Sutherland'
## author_email='afxsutherland@gmail.com'