## global dan local scope

nama_global = "otong" # <- variabel global

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")

## variabel local scope

def fungsi2():
    nama_local = "ucup" # <- variabel local

fungsi2()
# print(nama_local) <- tidak bisa dijalankan

## contoh 1: penggunaan akses variabel
def say_otong():
    print(f"hello {nama}")

nama = "otong"
say_otong()

## contoh 2: mengubah variabel global
angka = 0
name = "ucup"

def ubah_angka(nilai_baru, nama_baru):
    global angka # mengubah variabel local menjadi global
    global name
    angka = nilai_baru
    name = nama_baru

print(f"sebelum = {angka,name}")
ubah_angka(10, "otong")
print(f"setelah = {angka,name}")

## contoh 3:
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 3
    angka_dummy = 7

print(angka)
print(angka_dummy)