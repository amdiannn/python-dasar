# break

angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang = {angka}")

    if angka == 3:
        print("nice!")
        break

    print("wassap!")

print("cukuuuupp!")

# contoh penerapan dalam input

data_int = int(input("silakan berhitung sampai: "))

angka = 0

while True:
    angka += 1
    print(f"angka sekarang = {angka}")

    if angka == data_int:
        print("nice!")
        break

    print("wassap!")

print("cukuuuupp!")