# data yang dimasukkan pasti bertipe string
data = input("masukkan data: ")
print("data = ", data, ", type = ", type(data))

# jika ingin mengambil data lain, maka harus dicasting dulu
angka = int(input("masukkan angka: "))
print("angka = ", angka, ", type = ", type(angka))

desimal = float(input("masukkan desimal: "))
print("desimal = ", desimal, ", type = ", type(desimal))

# lalu bagaimana dengan boolean?
biner = bool(int(input("masukkan biner: ")))
print("biner = ", biner, ", type = ", type(biner))
# agar menghasilkan false, maka input dicasting ke int dulu