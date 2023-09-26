# latihan, kalkulator sederhana

print("""""")
print(25 * "=")
judul = "kalkulator sederhana"
print(judul.center(25))
print(25 * "=")
print("""""")

angka_pertama = float(input("masukkan angka pertama: "))
operator = input("masukkan operator aritmatika: ")
angka_kedua = float(input("masukkan angka kedua: "))

# percabangannya:

if operator == "+":
    hasil = angka_pertama + angka_kedua
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_pertama - angka_kedua
    print(f"hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_pertama * angka_kedua
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_pertama / angka_kedua
    print(f"hasilnya adalah {hasil}")
else:
    print("masukin yang bener dong!")

print("terima kasih ya!!!")