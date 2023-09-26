# operator dalam bentuk method

## merubah case dari string

# mengubah ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# mengubah ke lower case
alay = "aKu KeCe AbieezZzZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- mengecek huruf
# isalnum() <-- mengecek huruf dan angka
# isdecimal() <--  mengecek angka
# isspace() <-- mengecek spasi, tab, inline
# istitle() <-- mengecek semua kata diawali huruf kapital

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

## mengecek komponen startswith() dan endswith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

## penggabungan dan pemisahan komponen join() dan split()
pisah = ["aku", "sayang", "kamu"]
gabung = ",".join(pisah)
print(pisah)
print(gabung)

gabung = " ".join(pisah)
print(gabung)

gabung = " ehm ".join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung.split("ehm"))

## alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(20)
print("'" + kanan + "'")

kiri = "kiri".ljust(20)
print("'" + kiri + "'")

tengah = "tengah".center(20,":")
print("'" + tengah + "'")

# menghilangkan adjustment strip()
tengah = tengah.strip(":")
print("'" + tengah + "'")