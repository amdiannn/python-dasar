# module matematika dengan import

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as terserah

import matematika as math # bisa juga dilakukan

hasil_tambah = add(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = terserah(3)
print(f"hasil pangkat 3 = {pangkat_3(3)}")