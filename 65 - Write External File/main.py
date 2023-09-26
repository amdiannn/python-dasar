# 1. mode write

# dia akan membuat file baru jika tidak ada
# lalu akan menimpa atau overwrite isinya

with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("jhon si jhonny")

with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("overwrite")

# 2. mode append

with open("data_2.txt","w",encoding="utf-8") as file:
    file.write("jhon si jhonny\n")

with open("data_2.txt","a",encoding="utf-8") as file:
    file.write("ucup surucup\n")

with open("data_2.txt","a",encoding="utf-8") as file:
    file.write("tambah lagi dengan append\n")

# mode r+

with open("data_3.txt","w",encoding="utf-8") as file:
    file.write("data ke-3\n")

with open("data_3.txt","r+",encoding="utf-8") as file:
    file.write("baris ke-1\n")
    file.write("baris ke-2\n")
    file.write("baris ke-3\n")

with open("data_3.txt","r+",encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt","r+",encoding="utf-8") as file:
    file.write("otong") # menimpa isi text sesuai dengan panjang data