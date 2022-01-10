import subprocess
import time
import requests
import sys

check_delay = sys.argv[2]
http_get_url = sys.argv[1]

while True:
    tasklist_output = str(subprocess.check_output('TASKLIST /FI "WINDOWTITLE eq Waiting For Host"', shell=True))
    if "Zoom.exe" in tasklist_output:
        time.sleep(check_delay)
    else:
        print("Meeting Started")
        class_name = str(sys.argv[3])
        requests.get(http_get_url + "?value2=" + class_name + " Class has started.")
        exit()