def hitung_kembalian(total_pembayaran, total_belanja):
    kembalian = total_pembayaran - total_belanja
    
    if kembalian == 0:
        return "Pembayaran Pas"
    elif kembalian < 0:
        return "Pembayaran Kurang"
    
    pecahan = [10000, 5000, 2000, 1000, 500, 200, 100]
    
    # Inisialisasi dictionary untuk menyimpan hasil
    hasil = {}
    
    
    for nilai in pecahan:
        # Hitung jumlah lembar untuk pecahan ini
        jumlah_lembar = kembalian // nilai
        if jumlah_lembar > 0:
            # Simpan ke dictionary
            hasil[str(nilai)] = jumlah_lembar
            # Kurangi kembalian dengan nilai yang sudah digunakan
            kembalian -= jumlah_lembar * nilai
    
    return hasil

while True:
    try:
        belanja = int(input("Masukkan total belanja: "))
        pembayaran = int(input("Masukkan total pembayaran: "))

        
        if pembayaran < 0 or belanja < 0:
            print("Input tidak boleh negatif.")
            continue
        
        hasil = hitung_kembalian(pembayaran, belanja)
        print(f"Kembalian: {pembayaran - belanja}")
        print(f"Hasil: {hasil}")
        break
    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")