from main import *
import os
import sys
import logging
import datetime
import time

date = datetime.datetime.now()
dir = os.path.dirname(__file__)
log_name = os.path.basename(__file__)
# folder = os.path.join(dir, "output")
# if os.chdir != 'output':
#     os.mkdir(folder)
# log_path = f"{dir}\output\{log_name}.log"
log_path = f"{dir}\{log_name}.log"

stdoutOrigin = sys.stdout
sys.stdout = open(log_path, "a+")

dataList = fileRead("stocks.txt")
convertedData, tpl = convert(dataList)
dataTable = table(convertedData)

print(date)
print(dataTable)
print(f"\n{'='*40+' '}{round(tpl,2)}{' '+'='*40}")
