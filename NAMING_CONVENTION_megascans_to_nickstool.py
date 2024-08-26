import os

# Define the path to the directory
directory_path = r'C:\Users\andrew\Desktop\textures_to_rename'

# Define replacement mappings
replacement_dict = {
    "Colour": "color", "colour": "color", "basecolour": "color", 
    "Basecolour": "color", "base_colour": "color", "Base_colour": "color", 
    "base_Colour": "color", "Base_Colour": "color", "Albedo": "color", 
    "diffuse": "color",
    "metallic": "metal", "Metallic": "metal", "metallness": "metal", 
    "Metallness": "metal", "Metal": "metal",
    "roughness": "rough", "Roughness": "rough",
    "Normal": "normal", "Nmap": "normal", "nmap": "normal",
    "Displacement": "height",
    "Emission": "emission",
    "Alpha": "alpha", "mask": "alpha", "Opacity": "alpha",
    "Refraction": "refraction",
    "Translucency": "translucency",
    "Specular": "specular",
    "AO": "AO"
}

def replace_text(text, replacements):
    # Replace each key in the text with its corresponding value
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def ensure_unique_filename(path, base_name, ext):
    counter = 1
    new_file_name = base_name + ext
    while os.path.exists(os.path.join(path, new_file_name)):
        new_file_name = f"{base_name}_{counter}{ext}"
        counter += 1
    return new_file_name

def rename_files_in_directory(path):
    for root, dirs, files in os.walk(path):
        for file_name in files:
            old_file_path = os.path.join(root, file_name)
            # Replace words according to the replacement dictionary
            base_name, ext = os.path.splitext(file_name)
            new_base_name = replace_text(base_name, replacement_dict)
            # Replace spaces and dashes with underscores
            new_base_name = new_base_name.replace(' ', '_').replace('-', '_')
            new_file_name = ensure_unique_filename(root, new_base_name, ext)
            new_file_path = os.path.join(root, new_file_name)
            
            if old_file_path != new_file_path:
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {old_file_path} -> {new_file_path}')

# Run the rename function
rename_files_in_directory(directory_path)





## author='Andrew_Sutherland'
## author_email='afxsutherland@gmail.com'
