# operasi yang dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # ini adalah assignment
print("nilai a =", a)

a += 1 # artinya a = a + 1
print("nilai a += 1 adalah", a)

a -= 2 # artinya a = a - 2
print("nilai a -= 2 adalah", a)

a *= 5 # artinya a = a * 5
print("nilai a *= 5 adalah", a)

a /= 1 # artinya a = a / 2
print("nilai a /= 2 adalah", a)

# modulus dan floor division

b = 10
print("\nnilai b =", b)
b %= 3
print("nilai b %= 2 adalah", b)

b = 10
print("\nnilai b =", b)
b //= 3
print("nilai b //= 3 adalah", b)

# pangkat atau eksponen

a = 5
print("\nnilai a =", a)
a **= 3
print("nilai a **= 3 adalah", a)

# operasi bitwise

# OR
c = True
print("\nnilai c =", c)
c |= False
print("nilai c |= False adalah", c)
c = False
print("nilai c =", c)
c |= False
print("nilai c |= False adalah", c)

# AND
c = True
print("\nnilai c =", c)
c &= False
print("nilai c &= False adalah", c)
c = True
print("nilai c =", c)
c &= True
print("nilai c &= True adalah", c)

# XOR
c = True
print("\nnilai c =", c)
c ^= False
print("nilai c ^= False adalah", c)
c = True
print("nilai c =", c)
c ^= True
print("nilai c ^= True adalah", c)

# shifting right and left
d = 0b0100
print("\nnilai d =", format(d, "04b"))
d >>= 2
print("nilai d >>= 2 adalah", format(d, "04b"))
d <<= 1
print("nilai d <<= 1 adalah", format(d, "04b"))