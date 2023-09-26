import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("="*100)
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("-"*100)

    CRUD.init_console()

    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("="*100)
        print("SELAMAT DATANG DI PROGRAM SEDERHANA DATABASE PERPUSTAKAAN")
        print("-"*100)

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Masukkan Opsi: ")

        print("="*100+"\n")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": print("Delete Data")

        print("\n"+"="*100+"\n")

        isDone = input("Input Database Selesai? (y/n) ")
        if isDone == "y" or isDone == "Y":
            break

    print("Program Berakhir, Terima Kasih")