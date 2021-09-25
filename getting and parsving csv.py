from datetime import datetime
from matplotlib.dates import date2num

import mplfinance as mpf


f = open("AAPL.csv",'r')

data = {}

header = f.readline()
print(header)

header = header.strip("\n")
print(header)
header = header.split(",")
print(header)
test = [1,2,3,4]
for name in header:
    data[name] = []

for line in f:
    line = line.strip("\n").split(",")


    date = [int(x) for x in line[0].split("-")]
    date = datetime(date[0],date[1],date[2])
    date = date2num(date)
    data["Date"].append(line [0])
    data["Open"].append(line[1])
    data["High"].append(line[2])
    data["Low"].append(line[3])
    data["Close"].append(line[4])
    data["Volume"].append(line[5])
    data["Adj Close"].append(line[6])

print(data)
f.close()
