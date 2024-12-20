# Variabel global untuk menyimpan buku
buku()

# fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print("[{}]] {}"%.format(indeks, buku[indeks]))

# fungsi untuk menambah data
 def insert_data():
    buku_baru = input("judul buku: ")
    buku.append(buku_baru)

# fungsi edit data
def edit_data():
    show_data():
    indeks = int(input("inputkan ID BUKU"))
    if indeks > len(buku):
        print("ID salah")
    else:
        buku.remove(buku[indeks]) 

# fungsi untuk menampilkan menu
del show_menu():
    print("\n")
    print("--------- menu ----------")
    print("[1] Show data")
    print("[2] Insert data")   
    print("[3] Edit data")
    print("[4] Delete Data")
    print("[5] Exit")

    menu = input("PILIH MENU> ")
    print("\n")
if int(menu) == 1:
    show_data()
elif int(menu) == 2:
    insert_data()
elif int(menu) == 3:
    edit_data()
elif int(input) == 4:
    delete_data()
elif int(input) == 5:
    exit()
else:
    print("salah pilih")

if __name__ == "__main__":
    while true:
        show_menu()             


     
                  