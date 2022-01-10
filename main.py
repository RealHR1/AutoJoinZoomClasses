import os
import requests
import time
import pandas as pd
from datetime import datetime
import subprocess

http_get_url = "YOUR IFTTT WEBHOOK URL HERE"
post_join_timeout = 60
Code_rerun_timeout = 5
startquery = 7
checkdelay = 5

print("Zoom Auto Class Join Bot v1.1")

def sign_in(meetingid, pswd):
    os.system('%APPDATA%\Zoom\\bin\Zoom.exe "--url=zoommtg://zoom.us/join?action=join&confno=' + str(meetingid) + '&pwd=' + str(pswd) + "\"")

while True:

    day = datetime.today().strftime('%A')
    csv = "Schedule\\" + day + ".csv"
    df = pd.read_csv(csv)
    now = datetime.now().strftime("%H:%M")

    if now in str(df['timings']):

        row = df.loc[df['timings'] == now]
        m_id = str(row.iloc[0,1])
        m_pswd = str(row.iloc[0,2])
        class_name = str(row.iloc[0,3])
        sign_in(m_id, m_pswd)
        time.sleep(startquery)
        tasklist_output = str(subprocess.check_output('TASKLIST /FI "WINDOWTITLE eq Waiting For Host"', shell=True))
        if "Zoom.exe" in tasklist_output:
            print(class_name + " class joined and class " + "has not" + " started")
            requests.get(http_get_url + "?value1=Bot has joined " + class_name + " class." + "&value2=Class has not started.")
            subprocess.Popen("meetingstart.py" + " " + http_get_url + " " + checkdelay + " " + class_name, shell=True)
        else:
            print(class_name + " class joined and class " + "has" + " started")
            requests.get(http_get_url + "?value1=Bot has joined " + class_name + " class." + "&value2=Class has started.")
        time.sleep(post_join_timeout)
    else:
        time.sleep(Code_rerun_timeout)