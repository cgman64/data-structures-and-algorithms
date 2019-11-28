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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

import re

bangalore_re = "^\(080\)"
fixed_re = "\(0\d+\)"
mobile_re = "$\d{4}"
tele_re = "$140"
regex = "^\(080\)|^\(0\d+\)|^[^140]\d{4}|^140"
list_of_codes = []
# Part A
for c in calls:
	sending = c[0]
	receiving = c[1]
	m = re.search(bangalore_re, sending)
	if m:
		code = re.search(regex, receiving)
		if code.group() not in list_of_codes:
			list_of_codes.append(code.group())

#list_of_codes = list(set(list_of_codes))
print("The numbers called by people in Bangalore have codes:", list_of_codes)

# Part B
for c in calls:
	sending = c[0]
	receiving = c[1]
	m = re.search(bangalore_re, sending)
	if m:
		code = re.search(regex, receiving)
		list_of_codes.append(code.group())

# calculate percentage of call being to (080)
numerator = 0
total = float(len(list_of_codes))
for code in list_of_codes:
	if code == '(080)':
		numerator += 1
percentage = round((float(numerator) / total) * 100.0,2)

print("{} percent of calls from fixed lines in Bangalore are calls " \
"to other fixed lines in Bangalore.".format(percentage))


