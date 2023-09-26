from . import Operasi

# Fungsi view read
def read_console():
    data_file = Operasi.read()

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:<4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")

    # Footer
    print("="*100+"\n")

# Fungsi view create
def create_console():
    print("-"*100)
    print("Silakan Tambah Data Buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Input Tidak Valid, Silakan Masukkan Lagi")
        except:
            print("Input Tidak Valid, Silakan Masukkan Lagi")

    Operasi.create(tahun,judul,penulis)
    print("\nBerikut Adalah Data Baru Anda:")
    read_console()

# Fungsi view update
def update_console():
    read_console()
    while(True):
        print("\n"+"="*100)
        print("Silakan Pilih Nomor Buku Untuk Diupdate\n")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Input Tidak Valid, Silakan Masukkan Lagi")
    
    data_break = data_buku.split(",")
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while(True):
        # Menampilkan data yang akan diupdate
        print("\n"+"="*100)
        print("Silakan Pilih Data Untuk Diupdate\n")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # Memilih data yang akan diupdate
        user_option = input("\nPilih Data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":
                 while(True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Input Tidak Valid, Silakan Masukkan Lagi")
                    except:
                        print("Input Tidak Valid, Silakan Masukkan Lagi")
            case _: print("Input Tidak Valid, Silakan Masukkan Lagi")
        
        print("\nSilakan Cek Data Baru Anda\n")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        isDone = input("\nUpdate Database Selesai? (y/n) ")
        if isDone == "y" or isDone == "Y":
            break

    Operasi.update(no_buku,pk,data_add,judul,penulis,tahun)