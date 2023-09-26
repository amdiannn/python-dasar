data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"halo, apa kabar?"')
print("'halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. menggunakan tanda backslash ( \ )

# membuat single quote menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# membuat tanda backslash menjadi string
print("C:\\user\\ucup")

# membuat tab menjadi string
print("ucup\totong, jauhan")

# membuat backspace menjadi string
print("ucup \botong, deketan")

# membuat newline menjadi string
print("baris pertama\nbaris kedua") # LF = line feed
print("baris pertama\rbaris kedua") # CR = carriage return
print("baris pertama\r\nbaris kedua") # CRLF = carriage return line feed

# string literal atau raw

# hati-hati
print("C:\new folder") # akan salah pathnya

# menggunakan raw string
print(r"C:\new folder")

# multiline literal string
print("""
nama : ucup
kelas : 3 sd
""")

# multiline literal string and raw
print(r"""
nama : ucup
kelas : 3 sd\new normal
website : www.ucup.com/newid
""")