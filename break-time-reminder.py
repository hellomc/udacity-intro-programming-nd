#Take A Break
#Description: Write a function that will remind the user to take a break every two hours.

#Fix code below to create a loop that tells the user to take 3 breaks.
#import time
#import webbrowser
t#time.sleep(10)
#webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")

import time
import webbrowser

total_breaks = 3
num_breaks = 0

while (num_breaks<total_breaks):
    time.sleep(15)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    num_breaks = num_breaks + 1
