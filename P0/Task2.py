"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from collections import defaultdict
from pprint import pprint

dic = defaultdict(int)
for c in calls: 
	sending = c[0]
	receiving = c[1]
	duration = int(c[-1])
	dic[sending] += duration
	dic[receiving] += duration

max_duration = (0,0)
for number, duration in dic.items():
	if duration > max_duration[1]:
		max_duration = (number, duration)

print(max_duration[0] + " spent the longest time, " + str(max_duration[1]) + \
	" seconds, on the phone during September 2016.")



