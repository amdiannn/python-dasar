# mengimport program datetime

import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now: {data_waktu}")
print(f"tahun: {data_waktu.year}")
print(f"hari: {data_waktu.strftime('%A')}")

# mengimport program counter dari collections

from collections import Counter

data = ["a","b","c","d","a","d","a"]
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah d = {data_count['d']}")

# memindahkan file directory dengan os.chdir

import os

os.chdir("C:\\Penyimpanan Utama\\Documents\\Long-Life Learning\\VSC - Python\\.vscode\\58 - Menggunakan Standard Library")

# membuka file txt dengan program open dari io

import io

file = open("file_text.txt","r")
print(file.read())
file.close()