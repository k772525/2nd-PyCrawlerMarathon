# Python 下載CSV檔案與解析

# 下載檔案

import urllib.request

res = "http://opendata.hccg.gov.tw/dataset/432257df-491f-4875-8b56-dd814aee5d7b/resource/de014c8b-9b75-4152-9fc6-f0d499cefbe4/download/20150305140446074.csv"
urllib.request.urlretrieve(res, './data/example.csv')

import os, sys

# 打开文件
dirs = os.listdir( './data' )

# 输出所有文件和文件夹
for file in dirs:
    print(file)

# File I/O
fh = open("./data/example.csv", encoding = 'utf8')
f = fh.read()
fh.close()

print(f)

# CSV Reader

import csv

# 開啟 CSV 檔案
with open('./data/example.csv', encoding = 'utf8',newline='') as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        print(row)
        
# 1. 取出班次一的每一個時間
import csv

# 開啟 CSV 檔案
with open('./data/example.csv', encoding = 'utf8',newline='') as csvfile:
  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  # 以迴圈輸出每一列
  for row in rows:
    print(row[5])
    
# 2. 將班次一的每一個時間用一種資料型態保存

data = []
with open('./data/example.csv', encoding = 'utf8',newline='') as csvfile:
  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  # 以迴圈輸出每一列
  for row in rows:
    data.append(row[5])
print(data)

# 3. 將班次一到五與其所有時間用一種資料型態個別保存
import csv

d1 = []
d2 = []
d3 = []
d4 = []
d5 = []

with open('./data/example.csv', encoding = 'utf8', newline='') as csvfile:
  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  # 以迴圈輸出每一列
  for row in rows:
    d1.append(row[5])
    d2.append(row[6])
    d3.append(row[7])
    d4.append(row[8])
    d5.append(row[9])

data = {}
data[d1[0]] = d1[1:]
data[d2[0]] = d2[1:]
data[d3[0]] = d3[1:]
data[d4[0]] = d4[1:]
data[d5[0]] = d5[1:]

data