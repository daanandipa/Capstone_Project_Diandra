gudang_buah = {
    "apel": 20,
    "jeruk": 15,
    "mangga": 10
}

def main_menu():
    print("\n============================")
    print(" Main Menu")
    print("1. Cek stock gudang")
    print("2. Menambahkan Buah di Gudang")
    print("3. Mengurangi Buah di Gudang")
    print("4. Menambahkan Buah Baru di Gudang")
    print("5. Menghilangkan Buah di Gudang")
    print("6. Menutup aplikasi")
    print("============================")

def cek_stok():
    print("\nStok Buah di Gudang:")
    if not gudang_buah:
        print("Gudang kosong.")
    else:
        for buah, jumlah in gudang_buah.items():
            print(f"- {buah.lower()}: {jumlah} buah")

def tambah_item():
    buah = input("Masukkan nama buah yang ingin ditambahkan: ").lower()
    if not buah.isalpha(): 
        print("Nama buah tidak valid.")
    else:
        jumlah_input = input(f"Masukkan jumlah {buah} yang ingin ditambahkan: ")
        if not jumlah_input.isdigit():
            print("Input jumlah tidak valid.")
        else:
            jumlah = int(jumlah_input)
            if jumlah < 0:
                print("Jumlah tidak boleh negatif.")
            else:
                if buah in gudang_buah:
                    gudang_buah[buah] += jumlah
                    print(f"{jumlah} buah {buah} berhasil ditambahkan.")
                else:
                    print(f"{buah} tidak ada di gudang. Tambahkan sebagai item baru? (y/n)")
                    konfirmasi = input().lower()
                    if konfirmasi == 'y':
                        gudang_buah[buah] = jumlah
                        print(f"{jumlah} buah {buah} berhasil ditambahkan sebagai item baru.")
                    else:
                        print("Penambahan dibatalkan.")

def kurangi_item():
    buah = input("Masukkan nama buah yang ingin dikurangi: ").lower()
    if buah in gudang_buah:
        jumlah_input = input(f"Masukkan jumlah {buah} yang ingin dikurangi: ")
        if not jumlah_input.isdigit():
            print("Input jumlah tidak valid.")
        else:
            jumlah = int(jumlah_input)
            if jumlah < 0:
                print("Jumlah tidak boleh negatif.")
            else:
                if jumlah >= gudang_buah[buah]:
                    del gudang_buah[buah]
                    print(f"Stok {buah} telah habis dan dihapus dari gudang.")
                else:
                    gudang_buah[buah] -= jumlah
                    print(f"{jumlah} buah {buah} berhasil dikurangi.")
    else:
        print(f"{buah} tidak ditemukan di gudang. Tidak bisa dikurangi.")

def tambah_buah_baru():
    buah = input("Masukkan nama buah baru: ").lower()
    if not buah.isalpha():
        print("Nama buah tidak valid.")
    elif buah in gudang_buah:
        print(f"{buah} sudah ada di gudang.")
    else:
        jumlah_input = input(f"Masukkan jumlah stok awal untuk {buah}: ")
        if not jumlah_input.isdigit():
            print("Input jumlah tidak valid.")
        else:
            jumlah = int(jumlah_input)
            if jumlah < 0:
                print("Jumlah tidak boleh negatif.")
            else:
                gudang_buah[buah] = jumlah
                print(f"Buah baru {buah} berhasil ditambahkan dengan stok {jumlah} buah.")

def hapus_item():
    buah = input("Masukkan nama buah yang ingin dihapus: ").lower()
    if buah in gudang_buah:
        del gudang_buah[buah]
        print(f"{buah} berhasil dihapus dari gudang.")
    else:
        print(f"{buah} tidak ditemukan di gudang.")

#===========
# Main Menu 
# ==========
while True:
    main_menu()
    pilihan = input("Masukkan pilihan menu (1-6): ")

    if pilihan == "1":
        cek_stok()
    elif pilihan == "2":
        tambah_item()
    elif pilihan == "3":
        kurangi_item()
    elif pilihan == "4":
        tambah_buah_baru()
    elif pilihan == "5":
        hapus_item()
    elif pilihan == "6":
        print("\nMenu Ditutup. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-6.")
