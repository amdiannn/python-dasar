## tutorial membaca file eksternal

print(5*"=", " Membaca File .txt", 5*"=")
file = open("data.txt",mode="r")

print(f"status read: {file.readable()}")
print(f"status write: {file.writable()}")

## membaca seluruh file
print(file.read())

## membaca per baris
print(file.readline(),end="") # membaca baris pertama
print(file.readline(),end="") # membaca baris kedua

## membaca semua baris sebagai list
print(file.readlines())

print(f"apakah file sudah diclose? {file.closed}")
file.close()
print(f"apakah file sudah diclose? {file.closed}")

## salah satu teknik membuka file di python
print(5*"=", " Membaca File .txt", 5*"=")

with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah diclose? {file.closed}")
    
print(f"apakah file sudah diclose? {file.closed}")