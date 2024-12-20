# Membuat fungsi
def salam():
    print ("Hello,Selamat pagi")

## Pemanggilan fungsi
salam()
salam()
salam()

# Membuat fungsi dengan parameter 
def luas_segtiga(alas,tinggi):
    luas = (alas * tinggi) / 2
    print ("luas segitiga: %f" % luas)

# Pemanggilan fungsi
luas_segtiga(4, 6)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas 

# pemanggilan fungsi
print ("luas persegi: %d" % luas_persegi(6))

# rumus: sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    voulume = luas_persegi(sisi) * sisi

# membuat variabel global
nama = "belajar kode"
versi = "1.0.0"

def help():
    # ini variabel lokal
    nama = "programku"
    versi = "1.0.1"
    # mengakses variabel lokal 
    print ("nama: %s" % nama)
    print ("versi %s" % versi)

    # mengakses variabel lokal 
    print ("nama: %s" % nama)
    print ("versi %s" % versi)

    # memanggil fungsi help()
    help()


    