# latihan perulangan membuat segitiga

sisi = 10

# 1. menggunakan for

count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

# 2. menggunakan while

print("\n")

count = 1

while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

# 3. hanya ganjil saja

print("\n")

count = 1

while True:
    if(count%2):
        print(count)
        print("*"*count)
        count += 1
    
    else:
        count += 1
        continue

    if count > sisi:
        break

# 4. segitiga sama kaki

print("\n")

count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        print(" "*spasi, "*"*count)
        spasi -= 1
        count += 1

    else:
        count += 1
        continue

    if count > sisi:
        break