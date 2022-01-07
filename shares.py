from main import *

####dataTable = table(convert(fileRead("stocks.txt")))
while True:
    dataList = fileRead("stocks.txt")
    convertedData, tpl = convert(dataList)
    dataTable = table(convertedData)

    print(dataTable)
    print(f"\n{'='*40+' '}{round(tpl,2)}{' '+'='*40}")
