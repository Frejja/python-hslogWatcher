# readPowerLog.py
# Read power.log from the latest directory

import os
from findLatestDirectory import find_latest_directory

def read_power_log():
    latest_dir = find_latest_directory()
    power_log_path = os.path.join(latest_dir, 'power.log')

    with open(power_log_path, 'r') as file:
        power_log = file.read()

    return power_log

if __name__ == '__main__':
    power_log = read_power_log()
    print(power_log)