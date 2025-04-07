function hitung(rating){
    const rating_terendah = Math.min(...rating);
    const rating_tertinggi = Math.max(...rating);

    const total = rating.reduce((acc, val) => acc + val, 0);
    const rata_rata = Math.round((total / rating.length) * 100) / 100; // Pembulatan dua angka di belakang koma

    hasil = [rating_terendah, rating_tertinggi, rata_rata];
    return hasil;
}

const rating_contoh = [4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0] 
console.log("Input Contoh: " + rating_contoh);
console.log("Output: " + hitung(rating_contoh));

const rating_1 = [5,4,2.5,5,3.6,1.1,3.6,4,4.2,1.5]
console.log("\nInput 1: " + rating_1);
console.log("Output: " + hitung(rating_1));
