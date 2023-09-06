# readPowerLog.py
# Watch and read power.log from the latest directory

import os
import sys
import time
import asyncio
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
from findLatestDirectory import find_latest_directory

class PowerLogWatcher:
    def __init__(self):
        self.power_log = ""
        self.latest_dir = find_latest_directory()
        self.power_log_path = os.path.join(self.latest_dir, 'power.log')
        self.log_file_path = os.path.join('h:\\dev\\logs', datetime.now().strftime('%Y-%m-%d_%H-%M-%S-Power.log'))
        logging.basicConfig(filename=self.log_file_path, level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    class PowerLogHandler(FileSystemEventHandler):
        def __init__(self, watcher):
            self.watcher = watcher

        def on_modified(self, event):
            if event.src_path == self.watcher.power_log_path:
                with open(self.watcher.power_log_path, 'r') as file:
                    self.watcher.power_log = file.read()
                logging.info(self.watcher.power_log)

    async def monitor_power_log(self):
        event_handler = self.PowerLogHandler(self)
        observer = Observer()
        observer.schedule(event_handler, self.latest_dir, recursive=True)
        observer.start()
        try:
            while True:
                await asyncio.sleep(1)
        except Exception as e:
            observer.stop()
            logging.error("Error occurred: ", e)
        observer.join()

    def get_power_log(self):
        return self.power_log

if __name__ == '__main__':
    power_log_watcher = PowerLogWatcher()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(power_log_watcher.monitor_power_log())