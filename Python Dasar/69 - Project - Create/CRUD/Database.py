from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME,"r",encoding="utf-8") as file:
            print("Database Tersedia, Init Done!")
    except:
        print("Database Tidak Tersedia, Silakan Buat Database Baru")
        Operasi.create_first_data()