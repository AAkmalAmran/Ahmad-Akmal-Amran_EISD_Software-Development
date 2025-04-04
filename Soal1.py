def hitung(rating):

    rating_terendah = min(rating)
    rating_tertinggi = max(rating)
    rating_rata = sum(rating) / len(rating)

    rating_rata = round(rating_rata, 1)

    return [rating_terendah, rating_tertinggi, rating_rata]


while True:
    inputan = input("Masukkan rating: ")
    if (inputan != ""):
        try:
            angka = list(map(float, inputan.split()))
            hasil = hitung(angka)
            print(hasil)
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")
    else:
        print("Input kosong. Masukkan angka yang benar.")
        