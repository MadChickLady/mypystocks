import urllib.request
import time
import datetime

stocksToPull = ('AAPL', 'GOOG','MSFT','CMG','AMZN','EBAY','TSLA','CZBS','MFBP','BYFC')

def pullData(stock):
    try:
        print ('Currently pulling',stock)
        print (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        urlToVisit = ('http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv')
        saveFileLine = stock+'.txt'

        try:
            readExistingData = open(saveFileLine,'r').read()
            splitExisting = readExistingData.split('\n')
            mostRecentLine = splitExisting[-2]
            lastUnix = mostRecentLine.split(',')[0]
        except:
            lastUnix = ('0')

        saveFile = open(saveFileLine,'a')
        sourceCode = urllib.request.urlopen(urlToVisit).read().decode()
        splitSource = sourceCode.split('\n')

        for eachLine in splitSource:
            if 'values' not in eachLine:
                splitLine = eachLine.split(',')
                if len(splitLine)==6:
                    if (splitLine[0]) > lastUnix:
                    
                        lineToWrite = eachLine+'\n'
                        saveFile.write(lineToWrite)
                        
        saveFile.close()

        print ('Pulled',stock)
        print ('sleeping....')
        print (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(10)
                
    except Exception.e:
        print ('main loop'), str(e)


for eachStock in stocksToPull:
    pullData(eachStock)

    

    
