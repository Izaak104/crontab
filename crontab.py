
##install packages for code interpretation
import pandas as pd 
import requests
import time
import os
import sys

##get current working directory
cwd = os.getcwd()

#print cwd
print(cwd)

##pull down api file
df=requests.get('https://data.cms.gov/data-api/v1/dataset/60ccbf1c-d3f5-4354-86a3-465711d81c5a/data')

##get current time stamp
now = time.time()

##save current time as a string
nowStr = time.strftime('%y-%m-%d_%H:%M:%S', time.localtime(now))

##save downloaded api file in the current working directory
with open(cwd + '/')

##df.to_csv(‘' + nowStr + '.txt', 'w') as f:
f.write(str(data))

