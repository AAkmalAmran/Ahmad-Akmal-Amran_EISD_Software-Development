function cek_duplikat(angka){
    return angka.length !== new Set(angka).size
}

input = [20, 1, 3, 2, 4, 6, 8, 5, 7, 9, 11, 13, 15, 10,  12, 14, 16, 18, 20, 17, 19] 

if (cek_duplikat(input) == true) {
    console.log("Input: " + input)
    console.log("Output: " + cek_duplikat(input))
    console.log("\nAda angka yang duplikat")
}else {
    console.log("Input: " + input)
    console.log("Output: " + cek_duplikat(input))
    console.log("\nTidak ada angka yang duplikat")
}