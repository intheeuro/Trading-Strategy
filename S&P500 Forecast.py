#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 10:33:45 2018

@author: Euro
"""
import urllib2
import urllib
from bs4 import BeautifulSoup
import pandas as pd
#from pandas_datareader import data, wb
import numpy as np

ticker = 'aapl'
def getdata(ticker, command = 'h'):
    while command not in ['h', 'f']:
        print "Please enter h/f to retreive historical or forecast data: \n>>"
        command = raw_input()
    if command == 'h':
        url = 'http://www.nasdaq.com/symbol/' + ticker + '/earnings-surprise'
        period = 5
        col = ['quarter', 'date reported', 'earning per share', 'consensus EPS', '%suprise']
    else:
        url = 'http://www.nasdaq.com/symbol/' + ticker + '/earnings-forecast'
        period = 7
        col = ['year end', 'consensus EPS', 'high eps forecast', 'low eps forecast', '#estimate', 'up', 'down']
        
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    body = BeautifulSoup(content, "lxml").body
    
    try:
        data_his = body.find('div', {'class': 'genTable'})        
        data_his = data_his.find_all('td')
        df = pd.DataFrame(columns = col)
        i = 0
        while i < len(data_his):
            temp = [x.text for x in data_his[i:i+period]]
            df = df.append(pd.DataFrame([temp], columns = col), ignore_index = True)
            i += period  
        print df
        
    except Exception:
        print "No data for", ticker

getdata(ticker, 'f')

command = 'f'
if command == 'h':
    url = 'http://www.nasdaq.com/symbol/' + ticker + '/earnings-surprise'
else:
    url = 'http://www.nasdaq.com/symbol/' + ticker + '/earnings-forecast'
    
request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')
body = BeautifulSoup(content, "lxml").body


data_his = body.find('div', {'class': 'genTable'})        
data_his = data_his.find_all('td')
col = ['quarter', 'date reported', 'earning per share', 'consensus EPS', '%suprise']
df = pd.DataFrame(columns = col)
i, period = 0, 7
while i < len(data_his):
    temp = [x.text for x in data_his[i:i + 5]]
    df = df.append(pd.DataFrame([temp], columns = col), ignore_index = True)
    i += period  
print df
    
