# operasi dan manipulasi string

# 1. menyambung string (concatenate)

nama_awal = "ucup"
nama_tengah = "d"
nama_akhir = "fame"

nama_lengkap = nama_awal + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string

panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada kompenen char dalam string
d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk" * 10)
print(15 * "ha")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-(0:3) : " + nama_lengkap[0:4])
print("index ke-(3:7) : " + nama_lengkap[3:8])
print("index ke-(0,2,4,6,8,10) : " + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ascii code untuk spasi adalah " + str(ascii_code))
data = 177
print("char untuk ascii 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))