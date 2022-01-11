Zoom Auto Class Join Bot v1.2

To run this bot, you need libraries listed in requirements.txt

Note: Make sure zoom is running before starting this program.

This works on windows only. You may be able to modify the code and get it to work on linux but I have not tried it.

http_get_url in main.py is the variable used to keep the url to the webhook link which you get from ifttt. To disable IFTTT alert functionality, comment out Lines 41, 48 and set http_get_url to "NA in main.py and comment out Line 18 in meetingstart.py

discord_webhook_url in main.py is the variable used to keep the url to the webhook link which you can get from discord. To disable discord server webhook send alert functionality, comment out Lines: 44, 51 and set discord_webhook_url to "NA" in main.py and comment out Line 21 in meetingstart.py

post_join_timeout in main.py is the time (in seconds) the bot will wait before re-running itself. Note that I recommend keeping it at 60 seconds minimum or else you could have the bot trying to rejoin the same meeting multiple times.

Code_rerun_timeout in main.py is the time(in seconds) the bot waits before re-running the script in the event that the bot does not find any meetings to join for the current time. I recommend a Code_rerun_timeout of atleast 5. Making it very low could cause high CPU utilization.

startquery variable is how much time(in seconds) does the bot wait before it checks if meeting is started or not. If you have a slow connection, you may want to increase it.

checkdelay is how much time(in seconds) does the bot wait between each of its checks on whether meeting is started or not after the initial check.

To edit the timings and names of your classes, you will find .csv files with days of the weeks as their names. Just open those and put in the schedule for the days corresponding to their names. Keep in mind that time has to be in dd:mm format and 24 hour format. Any other time format can cause that entry in the schedule to be ignored completely by the program. 
Example for correct time format:
    07:15 - 7:15 AM
    14:30 - 2:30 PM

NOTE: NAMES OF YOUR CLASSES CANT HAVE ANY SPACES IN BETWEEN WORDS

Changelog:
v1.1:
 - Fixed issue: HTTP GET request not being sent sometimes.
 - Added support for different schedules for different days of the week.
 - Added support for knowing if the meeting has started or not via http get and console.

v1.2:
 - Added support for discord server webhooks to get bot notifications.
