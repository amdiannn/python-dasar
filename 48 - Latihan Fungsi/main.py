'''latihan fungsi'''

import os

# built up fungsi
def header_utama():
    '''fungsi header'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^50}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^50}")
    print(f"{'='*50}")

def header_luas():
    os.system("cls")
    print(f"{'MENGHITUNG LUAS':^50}")
    print(f"{'='*50}")

def header_keliling():
    os.system("cls")
    print(f"{'MENGHITUNG KELILING':^50}")
    print(f"{'='*50}")

def header_both():
    os.system("cls")
    print(f"{'MENGHITUNG LUAS & KELILING':^50}")
    print(f"{'='*50}")

def menu_program():
    print(f"Menu Program Yang Tersedia:")
    print(f"1. Luas")
    print(f"2. Keliling")
    print(f"3. Luas & Keliling")

def input_menu():
    opsi = int(input("Pilih Menu Program: "))
    return opsi

def input_user():
    '''fungsi input user'''
    panjang = int(input("Masukkan Nilai Panjang: "))
    lebar = int(input("Masukkan Nilai Lebar: "))
    return panjang,lebar

def hitung_luas(panjang,lebar):
    '''fungsi luas'''
    return panjang*lebar

def hitung_keliling(panjang,lebar):
    '''fungsi keliling'''
    return 2*(panjang*lebar)

def display(message,value):
    '''fungsi display'''
    print(f"Hasil Perhitungan {message}: {value}")

def ulang_program():
    ulang_program = input("Jalankan Program Kembali? (y/n) ")
    return ulang_program

def error():
    print(f"{'='*50}")
    print(f"{'PROGRAM ERROR':^50}")
    print(f"{'MASUKKAN INPUT YANG BENAR':^50}")

def program_selesai():
    print(f"{'='*50}")
    print(f"{'PROGRAM SELESAI, TERIMA KASIH':^50}")

###

# program utama
while True:
    header_utama()

    menu_program()
    
    isMenu = input_menu()
    if isMenu == 1:
        header_luas()

        PANJANG,LEBAR = input_user()
        LUAS = hitung_luas((PANJANG),(LEBAR))

        display("Luas", (LUAS))
        
        isContinue = ulang_program()
        if isContinue == "y":
            continue
        elif isContinue == "n":
            break
        else:
            error()
            break
            
    elif isMenu == 2:
        header_keliling()

        PANJANG,LEBAR = input_user()
        KELILING = hitung_keliling((PANJANG),(LEBAR))

        display("Keliling", (KELILING))

        isContinue = ulang_program()
        if isContinue == "y":
            continue
        elif isContinue == "n":
            break
        else:
            error()
            break

    elif isMenu == 3:
        header_both()

        PANJANG,LEBAR = input_user()
        LUAS = hitung_luas((PANJANG),(LEBAR))
        KELILING = hitung_keliling((PANJANG),(LEBAR))

        display("Luas", (LUAS))
        display("Keliling", (KELILING))

        isContinue = ulang_program()
        if isContinue == "y":
            continue
        elif isContinue == "n":
            break
        else:
            error()
            break

    else:
        error()
        break

program_selesai()