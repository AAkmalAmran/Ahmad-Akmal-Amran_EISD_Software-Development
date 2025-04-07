def cek_duplikat(angka):
    return len(angka) != len(set(angka))

while True:
    try:
        inputan = input("Masukkan angka: ")
        
        angka = list(map(int, inputan.split()))
        hasil = cek_duplikat(angka)
        if hasil == True:
            print(f"Hasil: {hasil}")
            print("Ada angka yang duplikat")
            break
        else:
            print(f"Hasil: {hasil}")
            print("Tidak ada angka yang duplikat")
            break
    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")