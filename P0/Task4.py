"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
import re

list_of_numbers = []
tele_re = "$140\d+"

# Collect all sending and receiving call numbers.
out_call = []
in_call = []
for c in calls:
	out_call.append(c[0])
	in_call.append(c[1])
out_call = list(set(out_call))
in_call = list(set(in_call))

# Collect all sending and receiving text numbers.
out_in_text = []
for t in texts:
	out_in_text.append(t[0])
	out_in_text.append(t[1])
out_in_text = list(set(out_in_text))

for oc in out_call:
	if (oc not in in_call) and (oc not in out_in_text):
		list_of_numbers.append(oc)

print("These numbers could be telemarketers: ")
list_of_numbers.sort()
for n in list_of_numbers:
	print(n)