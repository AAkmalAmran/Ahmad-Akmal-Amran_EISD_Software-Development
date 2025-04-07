def cek_palindrome(kalimat):
    # Mengubah kalimat menjadi huruf kecil serta menghapus spasi dan tanda baca
    kalimat_mentah = ''.join(huruf.lower() for huruf in kalimat if huruf.isalnum())
    
    if kalimat_mentah == kalimat_mentah[::-1]:
        return "eureeka!"
    else:
        return "suka blyat"
    
while True:
    inputan = input("Masukkan kata: ")
    if inputan.strip() != "":
        hasil = cek_palindrome(inputan)
        print(hasil)
        break
    else:
        print("Tolong input sesuatu")