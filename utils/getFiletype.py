import magic
import os
import shutil
import errno
import zipfile
source_directory = r"C:\Users\Mikael\AppData\Local\Overwolf\BrowserCache\Cache\Cache_Data"
directory = r"C:\Users\Mikael\AppData\Local\Overwolf\BrowserCache\Cache\Cache_Data_temp"
temp_directory = r"h:\dev\temp"

# Delete all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(f'Failed to delete {file_path}. Reason: {e}')

# Function to ignore 'Permission denied' errors while copying
def ignore_errors(src, names):
    errors = []
    for name in names:
        try:
            os.lstat(os.path.join(src, name))  # lstat to not follow symlinks
        except OSError as err:
            if err.errno == errno.EACCES:
                continue
            errors.append(name)
    return errors

# Copy all files from source_directory to directory
shutil.copytree(source_directory, directory, dirs_exist_ok=True, ignore=ignore_errors)

# Get list of all files in the directory
files = os.listdir(directory)

# Iterate over the list of files
for file in files:
    # Construct full path
    full_path = os.path.join(directory, file)
    # Feed the full path to magic.from_file()
    file_type = magic.from_file(full_path)

    if "Zip archive data, at least v1.0 to extract" in file_type:

        # Open the gzip file
        try:    
            with zipfile.ZipFile(full_path) as f:
               file_list = f.namelist()
               for file in file_list:
                     if file == "replay.xml":
                        print(f"File: {file}, Type: {file_type}")
                        # Rename the file to have the extension .zip
                        destination_path = os.path.join(temp_directory, f"{os.path.splitext(file_in_archive)[0]}.zip")
                        # Copy the file to temp_directory
                        shutil.copyfile(full_path, destination_path)
                       
        except:
            pass
