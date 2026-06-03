import os
import shutil

current_dir = os.getcwd()

for filename in os.listdir(current_dir):
    if filename == 'organizer.py' or os.path.isdir(filename):
        continue
    
    file_ext = filename.split('.')[-1].lower()

    if file_ext in ['jpg', 'jpeg', 'png', 'gif', 'svg', 'psd']:
        folder_name = 'Images'
    elif file_ext in ['mp4', 'mov', 'avi', 'mp3', 'wav']:
        folder_name = 'Audio_and_Video'
    elif file_ext in ['txt', 'pdf', 'docx']:
        folder_name = 'Documents'
    elif file_ext in ['zip', 'rar', '7z', 'iso']:
        folder_name = 'Archives_and_Data'
    elif file_ext in ['py', 'sh', 'html', 'htm', 'css', 'js', 'php', 'java', 'cpp', 'c', 'json']:
        folder_name = 'Programming_and_Scripts'
    elif file_ext in ['exe', 'dll', 'sys', 'bat', 'cfg', 'ini']:
        folder_name = 'System_and_Executables'
    else:
        folder_name = 'others'

    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Created folder: {folder_name}")

        shutil.move(filename, os.path.join(folder_name, filename))
        print(f"Moved: {filename} -> {folder_name}/")

    except PermissionError:
        print(f"Error: Missing system permissions to move {filename}")
    except FileNotFoundError:
        print(f"Error: {filename} was moved or deletd during execution")
    except Exception as e:
        print(f"Unexpected Error with {filename}: {e}")