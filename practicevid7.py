import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

eachStock = ('TSLA', 'AAPL')

def graphData(stock):
    try:
        stockFile = stock+'1.txt'
        
        date, closep, highp, lowp,openp, volume = np.loadtxt(stockFile, delimiter=',',uppack=True,
                                                             converters={ o: mdates.strpdate2num('%Y%m%d')})
        fig = plt.figure()
        ax1 = plt.subplot(1,1,1)
        ax1.plot(date, openp)
        ax1.plot(date, highp)
        ax1.plot(date, lowp)
        ax1.plot(date, closep)
        
        plt.show()
        
    except Exception as e:
        print ('failed main loop'), e
        
for stock in eachStock:
    graphData(stock)
    time.sleep(5)