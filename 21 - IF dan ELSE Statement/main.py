# if dan else statement

nama = input("siapa nama anda? ")

# 1. program if inline
if nama == "ucup" : print("kamu ganteng abiezz!!")
print(f"terima kasih {nama}")

nama = input("siapa nama anda? ")

# 2. program if indentation
if nama == "tatang" :
    print("kamu ganteng abiezz!!")
    print("kamu juga keren banget!!")
print(f"terima kasih {nama}")

nama = input("siapa nama anda? ")

# 3. else statement
if nama == "otong" :
    print("hai otong, si keren!!")
else :
    print("ah kamu bukan otong, kamu gak keren! :(")
print(f"terima kasih {nama}")