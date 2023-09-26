import datetime
import os
import string
import random

# template dict mahasiswa
mahasiswa_template = {
    "nama":"nama",
    "nim":"00000000",
    "sks_lulus":0,
    "lahir":datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':^50}")
    print(f"{'SILAKAN INPUT DATA MAHASISWA':^50}")
    print("-"*50)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa["nama"] = input("Nama Mahasiswa\t: ")
    mahasiswa["nim"] = input("NIM Mahasiswa\t: ")
    mahasiswa["sks_lulus"] = int(input("SKS Lulus\t: "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir\t: "))
    BULAN_LAHIR = int(input("Bulan Lahir\t: "))
    TAHUN_LAHIR = int(input("Tahun Lahir\t: "))
    mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    
    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    os.system("cls")
    print(f"\n{'KEY':<6}  {'Nama':<17}  {'SKS':<3}  {'Tanggal Lahir':<15}")
    print("-"*50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]["nama"]
        NIM = data_mahasiswa[KEY]["nim"]
        SKS = data_mahasiswa[KEY]["sks_lulus"]
        LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%d/%m/%Y")

        print(f"{KEY:<6}  {NAMA:<17}  {SKS:<3}  {LAHIR:<15}")
    
    isDone = input("\nInput Data Mahasiswa Lain? (y/n) ")
    if isDone == "n":
        break

print("-"*50)
print(f"{'INPUT DATA MAHASISWA SELESAI':^50}")
print(f"{'TERIMA KASIH':^50}")