## teknik menduplikat list

a = ["ucup","otong","dudung"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# kita akan mengubah member dari a

# ini akan mengubah kedua list
a[1] = "michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# mencuplikat list dengan copy

print("membuat list c dengan a.copy()")
c = a.copy()

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[0] = "dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 1")
a[1] = "otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")