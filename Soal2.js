function cek_palindrom(kalimat) {
    //Mengubah kalimat menjadi huruf kecil dan menghapus spasi
    kalimat = kalimat.toLowerCase().trim();
    //Mengecek apakah kalimat adalah palindrom
    return kalimat == kalimat.split('').reverse().join('');
}

function hasil_palindrom(kalimat) {
    if (cek_palindrom(kalimat)) {
        return "eureka!";
    }else {
        return "suka blyat";
    }
}

const contoh_kata = [
    "Angsa",
    "KataK",
    "kasur empuk",
    "Aku Suka Kamu",
    "Ibu ratna antar ubi",
    "Kasur ini rusak",
    "katak suka"
];

contoh_kata.forEach(kalimat => {
    console.log(`${kalimat} -> ${hasil_palindrom(kalimat)}`);
});