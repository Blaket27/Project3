import pathlib
import re
import urllib.request

file = pathlib.Path("./http_access_log.txt")

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
urllib.request.urlretrieve(url, "./http_access_log.txt")

months = 0

filelines = len(open("./http_access_log.txt").readlines(  ))

with open("./http_access_log.txt") as d:
    for line in d:
        if re.search('(/Apr/)', line):
            months += 1
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
print("The total number of requests made in the previous 6 months is " + str(months) + ".")
#print("The total number of requests made in the time period of this log is " + str(line_count))
print("The total number of requests made over the lifetime of the log file is " + str(filelines) + ".")
