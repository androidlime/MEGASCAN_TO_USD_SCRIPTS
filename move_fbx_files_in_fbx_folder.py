import os
import shutil

# Define the path to the parent directory
parent_directory = r'C:\Users\andrew\Desktop\textures_to_rename'
# Define the path to the FBX_FILES directory
fbx_files_directory = os.path.join(parent_directory, '_FBX_FILES')

def move_fbx_files(source_dir, target_dir):
    # Create the FBX_FILES directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f'Created directory: {target_dir}')
    
    # Traverse through the source directory and its subdirectories
    for root, dirs, files in os.walk(source_dir):
        for file_name in files:
            if file_name.lower().endswith('.fbx'):
                old_file_path = os.path.join(root, file_name)
                new_file_path = os.path.join(target_dir, file_name)
                
                # Move the .fbx file to the FBX_FILES directory
                if not os.path.exists(new_file_path):
                    shutil.move(old_file_path, new_file_path)
                    print(f'Moved: {old_file_path} -> {new_file_path}')
                else:
                    print(f'Skipped (file already exists): {new_file_path}')

# Run the move function
move_fbx_files(parent_directory, fbx_files_directory)



## author='Andrew_Sutherland'
## author_email='afxsutherland@gmail.com'