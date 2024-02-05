# width and multiline

# data

data_nama = "Ucup"
data_umur = "17"
data_tinggi = 150.1
data_nomor_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string)

# string multiline (enter, multiline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}"""
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string)

# merapikan widht and alignment
data_string = f"""nama    = {data_nama:>10}
umur    = {data_umur:>10}
tinggi  = {data_tinggi:>10}
sepatu  = {data_nomor_sepatu:>10}"""
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string + "\n")