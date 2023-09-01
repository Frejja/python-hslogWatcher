# findLatestDirectory.py
# Latest Creaeted Directory in logs for hearhtstone

import os

if __name__ == '__main__':
	hsLogPath = 'K:\games\Hearthstone\Logs'
	all_subdirs = [d for d in os.listdir(hsLogPath) if os.path.isdir(d)]
	latest_subdir = max(all_subdirs, key=os.path.getmtime)
	print(latest_subdir)
