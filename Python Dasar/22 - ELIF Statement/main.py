# elif = else if statement

nama = input("nama kamu siapa? ")

if nama == "ucup": # kondisi 1
    print("hai ganteng!!") # aksi true 1
elif nama == "otong": # kondisi 2
    print("hai kece!!") # aksi true 2
elif nama == "mario": # kondisi 3
    print("hai humoris!!") # aksi true 3
else:
    print("au ah gak kenal!!") # aksi false

print(f"terima kasih {nama}")