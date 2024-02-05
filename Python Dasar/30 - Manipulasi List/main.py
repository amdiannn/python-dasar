## operasi

# index  0(-3)   1(-2)    2(-1)
data = ["ucup", "otong", "dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama adalah {data_0}")

data_terakhir = data[-1]
print(f"\ndata terakhir adalah {data_terakhir}")

data_ucup = data[-3]
print(f"\ndata ucup adalah {data_ucup}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"\npanjang data adalah {panjang_data}")

## manipulasi data list

# menambahkan item pada list sesuai posisi

print(f"\ndata sebelum ditambah adalah \n{data}")

data.insert(1, "asep")
print(f"\ndata setelah ditambah adalah \n{data}")

# menambah di akhir list
data.append("jajang")
print(f"\ndata setelah ditambah lagi adalah \n{data}")

# menambah list dengan list
data_baru = ["ujang", "usep", "dadang"]
data.extend(data_baru)
print(f"\ndata gabungan adalah \n{data}")

# mengubah data dalam list
data[2] = "michael"
print(f"\ndata setelah diubah adalah \n{data}")

# meremove data dalam list

data.remove("ujang")
print(f"\ndata setelah diremove adalah \n{data}")

# meremove data paling akhir
data_akhir = data.pop()
print(f"\ndata setelah yang akhir diremove adalah \n{data}")

print(f"\ndata akhir yang diremove adalah {data_akhir}")