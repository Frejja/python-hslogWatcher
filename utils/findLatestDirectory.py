# findLatestDirectory.py
# Latest Created Directory in logs for hearthstone

import os

if __name__ == '__main__':
	hsLogPath = 'K:\games\Hearthstone\Logs'
-	all_subdirs = [d for d in os.listdir(hsLogPath) if os.path.isdir(d)]
+	all_subdirs = [os.path.join(hsLogPath, d) for d in os.listdir(hsLogPath) if os.path.isdir(os.path.join(hsLogPath, d))]
	latest_subdir = max(all_subdirs, key=os.path.getmtime)
	print(latest_subdir)