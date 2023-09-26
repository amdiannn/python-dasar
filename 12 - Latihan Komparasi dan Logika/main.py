# membuat gabungan area rentang dari angka

# +++++ 3 ----- 10 +++++

inputUser = float(input("masukkan angka yang bernilai\nkurang dari 3\natau\nlebih dari 10: "))

# +++++ 3 -----
isKurangDari3 = (inputUser < 3)
print("kurang dari 3 =", isKurangDari3)

# ----- 10 +++++
isLebihDari10 = (inputUser > 10)
print("lebih dari 10 =", isLebihDari10)

# +++++ 3 ----- 10 +++++
isCorrect1 = isKurangDari3 or isLebihDari10
print("angka yang anda masukkan =", isCorrect1)

print("\n", 10*"=", "\n")

# ----- 3 +++++ 10 -----

inputUser = float(input("masukkan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10: "))

# ----- 3 +++++
isLebihDari3 = (inputUser > 3)
print("lebih dari 3 =", isLebihDari3)

# +++++ 10 -----
isKurangDari10 = (inputUser < 10)
print("kurang dari 10 =", isKurangDari10)

# ----- 3 +++++ 10 -----
isCorrect2 = isLebihDari3 and isKurangDari10
print("angka yang anda masukkan =", isCorrect2)

print("\n", 10*"=", "\n")

# ----- 0 +++++ 5 ----- 8 +++++ 11 -----

inputUser = float(input("masukkan angka yang bernilai\nlebih dari 0\ndan\nkurang dari 5\natau\nlebih dari 8\ndan\nkurang dari 11: "))

# ----- 0 +++++
isLebihDari0 = (inputUser > 0)
print("lebih dari 0 =", isLebihDari0)

isKurangDari5 = (inputUser < 5)
print("kurang dari 5 =", isKurangDari5)

isLebihDari8 = (inputUser > 8)
print("lebih dari 8 =", isLebihDari8)

isKurangDari11 = (inputUser < 11)
print("kurang dari 11 =", isKurangDari11)

isCorrect3 = (isLebihDari0 and isKurangDari5) or (isLebihDari8 and isKurangDari11)
print("angka yang anda masukkan =", isCorrect3)

print("\n", 10*"=", "\n")

# +++++ 0 ----- 5 +++++ 8 ----- 11 +++++

inputUser = float(input("masukkan angka yang bernilai\nkurang dari 0\natau\nlebih dari 5\ndan\nkurang dari 8\natau\nlebih dari 11: "))

# +++++ 0 -----
isKurangDari0 = (inputUser < 0)
print("kurang dari 0 =", isKurangDari0)

isLebihDari5 = (inputUser > 5)
print("lebih dari 5 =", isLebihDari5)

isKurangDari8 = (inputUser < 8)
print("kurang dari 8 =", isKurangDari8)

isLebihDari11 = (inputUser > 11)
print("lebih dari 11 =", isLebihDari11)

isCorrect4 = isKurangDari0 or (isLebihDari5 and isKurangDari8) or isLebihDari11
print("angka yang anda masukkan =", isCorrect4)