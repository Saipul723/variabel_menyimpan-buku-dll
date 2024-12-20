# Variabel global untuk menyimpan buku
buku = []

# Fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print(f"[{indeks}] {buku[indeks]}")

# Fungsi untuk menambah data
def insert_data():
    buku_baru = input("Judul buku: ")
    buku.append(buku_baru)
    print("Buku berhasil ditambahkan!")

# Fungsi edit data
def edit_data():
    show_data()
    try:
        indeks = int(input("Inputkan ID buku: "))
        if 0 <= indeks < len(buku):
            buku_baru = input("Judul buku baru: ")
            buku[indeks] = buku_baru
            print("Data berhasil diperbarui!")
        else:
            print("ID salah!")
    except ValueError:
        print("Masukkan angka yang valid!")

# Fungsi untuk menghapus data
def delete_data():
    show_data()
    try:
        indeks = int(input("Inputkan ID buku: "))
        if 0 <= indeks < len(buku):
            buku.pop(indeks)
            print("Data berhasil dihapus!")
        else:
            print("ID salah!")
    except ValueError:
        print("Masukkan angka yang valid!")

# Fungsi untuk menampilkan menu
def show_menu():
    print("\n")
    print("--------- MENU ----------")
    print("[1] Show data")
    print("[2] Insert data")   
    print("[3] Edit data")
    print("[4] Delete data")
    print("[5] Exit")

    try:
        menu = int(input("PILIH MENU> "))
        print("\n")
        if menu == 1:
            show_data()
        elif menu == 2:
            insert_data()
        elif menu == 3:
            edit_data()
        elif menu == 4:
            delete_data()
        elif menu == 5:
            print("Keluar dari program. Sampai jumpa!")
            exit()
        else:
            print("Pilihan tidak valid!")
    except ValueError:
        print("Masukkan angka yang valid!")

# Main program
if __name__ == "__main__":
    while True:
        show_menu()
