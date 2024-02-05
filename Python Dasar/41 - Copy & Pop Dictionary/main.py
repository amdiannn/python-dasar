# copy dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

friends = teman_teman.copy()

print(f"\nteman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"] = "ucup si kweren"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (mengambil data berdasarkan key)
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends: {friends}\n")

# popitem dictionary (mengambil data yang terakhir aja)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends: {friends}\n")