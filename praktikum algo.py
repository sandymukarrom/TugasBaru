def jumlah_hari(bulan, tahun):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        # Cek apakah tahun kabisat
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            return 29
        else:
            return 28
    else:
        return "Bulan tidak valid"

while True:
    try:
        bulan = int(input("Masukkan bulan (1-12): "))
        tahun = int(input("Masukkan tahun: "))
        
        if 1 <= bulan <= 12:
            hari = jumlah_hari(bulan, tahun)
            print(f"Jumlah hari di bulan {bulan}, tahun {tahun} adalah: {hari}")
            break
        else:
            print("Bulan harus di antara 1 dan 12. Coba lagi.")
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
