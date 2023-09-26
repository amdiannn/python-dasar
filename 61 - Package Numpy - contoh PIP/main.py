import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list_a = {list_a}\n")
# print(list_a**2) <- ini akan gagal
print(f"vector_a = {vector_a}\n")
print(f"a pangkat 2 = {vector_a**2}\n")
print(f"a kali 5 = {vector_a*5}\n")

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix b = \n{matrix_b}\n")
print(f"matrix b^2 = \n{matrix_b**2}\n")

zeros_c = np.zeros((2,2))
print(f"zeros c = \n{zeros_c}\n")

ones_d = np.ones((2,2))
print(f"ones d = \n{ones_d}\n")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah = \n{jumlah}")