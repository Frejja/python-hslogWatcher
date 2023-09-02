# findLatestDirectory.py
# Latest Created Directory in logs for hearthstone

import os

def find_latest_directory():
    hsLogPath = 'K:\games\Hearthstone\Logs'
    all_subdirs = [os.path.join(hsLogPath, d) for d in os.listdir(hsLogPath) if os.path.isdir(os.path.join(hsLogPath, d))]
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    return latest_subdir

if __name__ == '__main__':
    print(find_latest_directory())