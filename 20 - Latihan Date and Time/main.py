# date and time (latihan)

import datetime as dt

print("Silakan masukkan tanggal, \nbulan, dan tanggal lahir anda. \n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir \t: {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini\t: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30 

print(f"Hari\t\t: {tanggal_lahir:%A}")
print(f"Umur\t\t: {umur_tahun} tahun, {umur_bulan} bulan")