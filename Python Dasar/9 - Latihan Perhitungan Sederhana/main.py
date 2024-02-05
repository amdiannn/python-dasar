print("PROGRAM KONVERSI TEMPERATUR")

# konversi celcius

celcius = float(input('suhu dalam celcius:'))
print("suhu dalam celcius:", celcius, "celcius")

reamur = (4/5) * celcius
print("suhu dalam reamur:", reamur, "reamur")

fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit:", fahrenheit, "fahrenheit")

kelvin = celcius + 273
print("suhu dalam kelvin:", kelvin, "kelvin")

# konversi reamur

reamur = float(input('suhu dalam reamur:'))
print("suhu dalam reamur:", reamur, "reamur")

celcius = (5/4) * reamur
print("suhu dalam celcius:", celcius, "celcius")

fahrenheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit:", fahrenheit, "fahrenheit")

kelvin = ((5/4) * reamur) + 273
print("suhu dalam kelvin:", kelvin, "kelvin")

# konversi fahrenheit

fahrenheit = float(input('suhu dalam fahrenheit:'))
print("suhu dalam fahrenheit:", fahrenheit, "fahrenheit")

celcius = (5/9) * (fahrenheit - 32)
print("suhu dalam celcius:", celcius, "celcius")

reamur = (4/9) * (fahrenheit - 32)
print("suhu dalam fahrenheit:", fahrenheit, "fahrenheit")

kelvin = ((5/9) * (fahrenheit - 32)) + 273
print("suhu dalam kelvin:", kelvin, "kelvin")

# konversi kelvin

kelvin = float(input('suhu dalam kelvin:'))
print("suhu dalam kelvin:", kelvin, "kelvin")

celcius = kelvin - 273
print("suhu dalam celcius:", celcius, "celcius")

reamur = (4/5) * (kelvin - 273)
print("suhu dalam kelvin:", kelvin, "kelvin")

fahrenheit = ((9/5) * (kelvin - 273)) + 32
print("suhu dalam fahrenheit:", fahrenheit, "fahrenheit")