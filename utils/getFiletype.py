import magic
import os

directory = "C:\Users\Mikael\AppData\Local\Overwolf\BrowserCache\Cache\Cache_Data"

# Get list of all files in the directory
files = os.listdir(directory)

# Iterate over the list of files
for file in files:
    # Construct full path
    full_path = os.path.join(directory, file)
    # Feed the full path to magic.from_file()
    file_type = magic.from_file(full_path)
    print(f"File: {file}, Type: {file_type}")