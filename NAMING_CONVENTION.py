

#i want to replace "Color", "Colour", "colour", "basecolour", "Basecolour", "base_colour", "Base_colour", "base_Colour", "Base_Colour", "basecolor", "Basecolor", "base_color", "Base_color", "base_Color", "Base_Color", "Albedo", "diffuse", "dif" to the word "color"
#i want to replace "metallic", "Metallic", "metallness", "Metallness", "Metal" to the word "metal".
#i want to replace  "roughness", "Roughness", "spec", "Specular" to to the word "rough".
#i want to replace "Normal", "Nmap", "nmap" to the word "normal".
#i want to replace to "Displacement" to the word "height".
#i want to replace to "Emission", to the word "emission".
#i want to replace to "Alpha", "mask", "Opacity",  to the word "alpha".
#i want to replace to "Refraction" to the word "refraction".


import os

# Define the path to the directory
directory_path = r'C:\Users\andrew\Desktop\textures_to_rename'

# Define replacement mappings
replacement_dict = {
    "Color": "color", "Colour": "color", "colour": "color",
    "basecolour": "color", "Basecolour": "color", "base_colour": "color", 
    "Base_colour": "color", "base_Colour": "color", "Base_Colour": "color",
    "basecolor": "color", "Basecolor": "color", "base_color": "color",
    "Base_color": "color", "base_Color": "color", "Base_Color": "color",
    "Albedo": "color", "diffuse": "color", "dif": "color",
    "metallic": "metal", "Metallic": "metal", "metallness": "metal",
    "Metallness": "metal", "Metal": "metal",
    "roughness": "rough", "Roughness": "rough", "spec": "rough",
    "Specular": "rough",
    "Normal": "normal", "Nmap": "normal", "nmap": "normal",
    "Displacement": "height",
    "Emission": "emission",
    "Alpha": "alpha", "mask": "alpha", "Opacity": "alpha",
    "Refraction": "refraction"
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
            new_file_name = ensure_unique_filename(root, new_base_name, ext)
            new_file_path = os.path.join(root, new_file_name)
            
            if old_file_path != new_file_path:
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {old_file_path} -> {new_file_path}')

# Run the rename function
rename_files_in_directory(directory_path)




## author='Andrew_Sutherland'
## author_email='afxsutherland@gmail.com'