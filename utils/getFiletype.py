import magic
import os
import shutil
import errno
import gzip
import tarfile

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
def ignore_errors(func, path, exc_info):
    if exc_info[1].errno == errno.EACCES:
        return
    raise

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
    # Check if the file type is "gzip compressed data"
    if "gzip compressed data" in file_type:
        # Open the gzip file
        with gzip.open(full_path, 'rb') as f:
            # Open the tar file
            with tarfile.open(fileobj=f) as tar:
                # Check if "replay.xml" is in the tar file
                if any(name.endswith("replay.xml") for name in tar.getnames()):
                    print(f"File: {file}, Type: {file_type}")
                    # Rename the file to have the extension .zip
                    new_file_name = f"{os.path.splitext(file)[0]}.zip"
                    os.rename(full_path, os.path.join(directory, new_file_name))
                    # Move the file to temp_directory
                    shutil.move(os.path.join(directory, new_file_name), os.path.join(temp_directory, new_file_name))