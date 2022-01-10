**Zoom Auto Class Join Bot v1**

To run this bot, you need these python libraries:
os
requests
time
pandas
datetime

This works on windows only. You may be able to modify the code and get it to work on linux but I have not tried it.

http_get_url is the variable used to keep the url to the webhook link which you get from ifttt. You do not need to add "?value1" at the end of it, just paste the url withn the double quotation marks in Line 7 of main.py

post_join_timeout is the time (in seconds) the bot will wait before re-running itself. Note that I recommend keeping it at 60 seconds minimum or else you could have the bot trying to rejoin the same meeting multiple times. To modify it, put the number of seconds in Line 8 of main.py

Code_rerun_timeout is the time(in seconds) the bot waits before re-running the script in the event that the bot does not find any meetings to join for the current time. I recommend a Code_rerun_timeout of atleast 5. Making it very low could cause high CPU utilization. To modify it, put the number of seconds in Line 9 of main.py

Line 12 in main.py leaves the currently open meeting before joining the upcoming meeting. If you want it to let you manually choose if you want to leave the previous meeting every time instead of the running meeting being left automatically, comment that line by adding a "#" before it. By default, it is set to on

To edit the timings and names of your classes, edit timings.csv
