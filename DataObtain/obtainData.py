#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 21:27:10 2017

@author: wanggengyu
"""

#get 

import urllib2
import xml.etree.ElementTree as ET
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

tree = ET.parse('getCityList.xml')
root = tree.getroot()

writefile = open("AmountByCityDay.txt","w")
count = 0
monthList = ['01','02','03']
url ='http://apis.data.go.kr/B552584/RfidFoodWasteService/getCityDateList?ServiceKey=SxQJSl5WgwoPnFC94xJToMpg2cz%2B0WQRb%2BA1DqFgDfCzdu6EW4OS8KWIauSp5tcG0k5dnbF0UIj3uTMO97SKPg%3D%3D&type=xml&page=1&rowNum=32&disYear=2017'
#file = urllib2.urlopen(url+'&cityCode=W01'+'&disMonth=01')
#dataSet = ET.fromstring(file.read())
#for feature in dataSet[3]:
#    print feature.text
#    writefile.write(feature.text+'\t')
#writefile.write('\n')
for sido in root:
    urlcity = url + '&cityCode='+ sido[0].text
    for month in monthList:
        urlcitymonth = urlcity + '&disMonth='+ month
        file = urllib2.urlopen(urlcitymonth)
        print urlcitymonth
        dataSet = ET.fromstring(file.read())
        for dayData in dataSet: #each day
            for feature in dayData:
                print feature.text
                writefile.write(feature.text+'\t')
            writefile.write('\n')
        time.sleep(1) #pause for 1 second

writefile.close
            
