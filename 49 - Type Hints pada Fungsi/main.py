'''type hints untuk fungsi'''

# bentuk standar fungsi yang udah kita pelajari

# # studi kasus
# def fungsi(parameter):
#     hasil = parameter**2
#     print(hasil)

# fungsi(1)
# fungsi("ucup")
# fungsi(True)

# penggunaan type hints

import string

def sepuluh_pangkat(argument:int) -> int:
    '''fungsi dengan hints'''
    output = 10**argument
    return output

hasil = sepuluh_pangkat(4)
print(hasil)

def display(argument:string):
    print(argument)

display("ucup")