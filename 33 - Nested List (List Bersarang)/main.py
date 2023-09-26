data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2d = [data_0,data_1,6,7]

print(f"list 2d = {list_2d}")

# contoh penggunaan

peserta_0 = ["ucup",25,"laki-laki"]
peserta_1 = ["otong",10,"laki-laki"]
peserta_2 = ["dedeh",50,"perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2]

print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}")

#dengan reference

list_copy = list_peserta.copy()
print(f"peserta = {list_copy}")

peserta[0] = "michael"
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")