import json
import re
import urllib.request

file = open('D:/http_access_log.txt', 'r')

months = 0
line_count = 0
for i in file:
    if i:
        line_count += 1

with open("D:/http_access_log.txt") as d:
    for line in d:
        if re.search('(/May/)', line):
            months += 1
        if re.search('(/Jun/)', line):
            months +=1
        if re.search('(/Jul/)', line):
            months += 1
        if re.search('(/Aug/)', line):
            months += 1
        if re.search('(/Sep/)', line):
            months += 1
        if re.search('(/Oct/1995)', line):
            months += 1
print("The total number of requests made in the previous 6 months is " + str(months))
print("The total number of requests made in the time period of this log is " + str(line_count))

