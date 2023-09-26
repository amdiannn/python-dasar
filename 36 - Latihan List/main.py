# program list buku

list_buku = []
while True:
    print("\nSilakan Masukkan Data Buku.")
    judul = input("Judul Buku\t: ")
    penulis = input("Nama Penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("\n","="*10,"Data Buku","="*10,"\n")
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n","="*32,"\n")
    isLanjut = input("Apakah Ada Buku Lagi? (y/n): ")

    if isLanjut == "n":
        break

print("Program Input Data Buku Selesai.")