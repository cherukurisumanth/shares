
from yahoo_fin import stock_info as st
from tabulate import tabulate
import requests_html
import numpy


def fileRead(filename):
    file = open(filename, 'r')
    matrix = []

    for line in file:
        line.split("\n")
        word = line.split("ccc", 2)
        matrix.append(word)

    new = numpy.transpose(matrix).tolist()
    nameString, buyPrice, quantity = new

    for i in buyPrice:
        buyPrice[buyPrice.index(i)] = float(i)
    for i in quantity:
        j = i
        i = i.rstrip("\n")
        quantity[quantity.index(j)] = int(i)
    oldData = [nameString, buyPrice, quantity]
    return oldData


def calculate(nameString, buyPrice, quantity):
    shareName = nameString+".NS"
    livePrice = st.get_live_price(shareName)
    profit = quantity * (livePrice - buyPrice)
    details = {'shareName': shareName, 'livePrice': livePrice,
               'buyPrice': buyPrice, 'quantity': quantity, 'profit/loss': profit}
    return details


def convert(oldData):
    nameString, buyPrice, quantity = oldData
    NUMBER = len(quantity)
    shares = [{}] * NUMBER
    tpl = 0
    for i in range(NUMBER):
        shares[i] = calculate(nameString[i], buyPrice[i], quantity[i])
        tpl = tpl+shares[i].get('profit/loss')
    return shares, tpl


def table(listOfDict):
    header = listOfDict[0].keys()
    rows = [x.values() for x in listOfDict]
    return tabulate(rows, header)
