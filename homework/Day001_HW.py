# 資料來源與檔案存取

# 根據需求引入正確的 Library

from urllib.request import urlretrieve
import os

# 下載檔案到 Data 資料夾，存成檔名 Homework.txt

try:
    os.makedirs( './Data', exist_ok=True )
    urlretrieve ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "./Data/Homework.txt") 
except:
    print('發生錯誤！')

# 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案

files = os.listdir('./Data')

if 'Homework.txt' in files:
    print('[O] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')
else:
    print('[X] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')
    
# 將「Hello World」字串覆寫到 Homework.txt 檔案

f = ''

with open("./Data/Homework.txt", "w") as fh:
    f = fh.write("Hello World")

try:
    with open("./Data/Homework.txt", "r") as fh:
        f = fh.read()
except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
    pass


# 檢查 Homework.txt 檔案字數是否符合 Hello World 字數

if len('Hello World') == len(f):
    print('[O] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
else:
    print('[X] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')