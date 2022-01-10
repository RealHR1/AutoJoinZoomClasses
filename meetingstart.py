import subprocess
import time
import requests
import sys
from discord_webhook import DiscordWebhook, DiscordEmbed

check_delay = int(sys.argv[3]) 
http_get_url = sys.argv[1]
webhook = DiscordWebhook(url=sys.argv[2])

while True:
    tasklist_output = str(subprocess.check_output('TASKLIST /FI "WINDOWTITLE eq Waiting For Host"', shell=True))
    if "Zoom.exe" in tasklist_output:
        time.sleep(check_delay)
    else:
        print("Meeting Started")
        class_name = str(sys.argv[4])
        requests.get(http_get_url + "?value2=" + class_name + " Class has started.")
        embed = DiscordEmbed(title='School', description=class_name+' class has started.', color='ff007b')
        webhook.add_embed(embed)
        webhook.execute()
        exit()