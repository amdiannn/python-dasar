# operasi arimatika

a = 10
b = 3

# penambahan +
hasil = a + b
print(a, "+", b, "=", hasil)

# pengurangan -
hasil = a - b
print(a, "-", b, "=", hasil)

# perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)

# pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)

# eksponen (pangkat) **
hasil = a ** b
print(a, "**", b, "=", hasil)

# modulus %
hasil = a % b
print(a, "%", b, "=", hasil)

# floor division //
hasil = a // b
print(a, "//", b, "=", hasil)

# operational precedence, prioritas operasi

# 1. tanda kurung ()
# 2. eksponen **
# 3. perkalian dkk * / % //
# 4. pertambahan, pengurangan + -

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

hasil = x + y * z
print(x, "+", y, "*", z,  "=", hasil)

# tanda kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print("(", x, "+", y, ") *", z,  "=", hasil)