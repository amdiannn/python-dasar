'''fungsi dengan argument (input)'''

# template
# def nama_fungsi(argument):
#     badan fungsi

def hello_world(nama):
    '''fungsi hello world menerima input dengan variable nama'''
    print(f"selamat datang dunia wahai {nama}")

hello_world("ucup")
hello_world("asyep")

# program tambah

def tambah(angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(1000000,1)

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")

anggota_boyband = ["ucup","otong","dudung"]

say_hi(anggota_boyband)