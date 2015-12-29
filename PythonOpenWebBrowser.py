
# prompts user to take a break by opening a web browser to play jazz music
# The duration variable would be set to 2 * 60 * 60 to prompt every 2 hours
# Note: derived from Programming Foundations with Python on Udacity.com

import time
import webbrowser

total_breaks = 3
break_count = 0
duration = 10 # 2 * 60 * 60

print("This program started on " + time.ctime())
while(break_count < total_breaks):
	time.sleep(duration)
	webbrowser.open("https://www.youtube.com/watch?v=0gcu3GI3nA4")
	break_count = break_count + 1