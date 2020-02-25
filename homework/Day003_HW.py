# Python 下載XML檔案與解析
'''
了解 xml 檔案格式與內容
能夠利用套件存取 xml 格式的檔案
'''

# 比較一下範例檔案中的「File I/O」與「xmltodict」讀出來的內容有什麼差異
# 下載檔案
import urllib.request
import zipfile
import os

res = 'http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314'
download_path = './data/example.zip'
extract_path = './data'

# create download directory
try:
    os.makedirs(extract_path)
except:
    pass

# Download the file into specified path
urllib.request.urlretrieve(res, download_path)

# Unzip the file 
f = zipfile.ZipFile(download_path)
f.extractall(extract_path)

# 1. 請問高雄市有多少地區有溫度資料？

import xmltodict

with open("./data/64_72hr_CH.xml", "r", encoding='UTF-8') as file:
    xml = file.read()
    d = dict(xmltodict.parse(xml))
    print('共', len(d['cwbopendata']['dataset']['locations']['location']), '個地區')
    
# 2. 請取出每一個地區所記錄的第一個時間點跟溫度
import xmltodict

with open("./data/64_72hr_CH.xml", "r", encoding='UTF-8') as file:
    xml = file.read()
    d = dict(xmltodict.parse(xml))
    for location in d['cwbopendata']['dataset']['locations']['location']:
        locationName = location['locationName']
        timing = location['weatherElement'][0]['time'][0]['dataTime']
        value = location['weatherElement'][0]['time'][0]['elementValue']['value']
        print(locationName, '時間點:', timing, '溫度:', value)