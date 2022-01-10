import os
import requests
import time
import pandas as pd
from datetime import datetime

http_get_url = "Your_IFTTT_Webhook_Link_here"
post_join_timeout = 60
Code_rerun_timeout = 5

print("Zoom Auto Class Join Bot v1")

def sign_in(meetingid, pswd):
    os.system('TASKKILL /IM Zoom.exe') #Leaves the currently open meeting before joining the upcoming meeting.
    os.system('%APPDATA%\Zoom\\bin\Zoom.exe "--url=zoommtg://zoom.us/join?action=join&confno=' + str(meetingid) + '&pwd=' + str(pswd) + "\"")

while True:
    # checking if the current time exists in our csv file
    df = pd.read_csv('timing.csv')
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])
       class_name = str(row.iloc[0,3])

       sign_in(m_id, m_pswd)
       print(class_name + " class started")
       requests.get(http_get_url + "?value1=" + class_name)
       time.sleep(post_join_timeout)
    else:
        time.sleep(Code_rerun_timeout)