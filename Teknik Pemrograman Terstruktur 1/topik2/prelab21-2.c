#include <stdio.h>

int main()
{
    // Mendeklarasikan variabel umur dengan tipe data int
    int umur;
    
    // Menampilkan output berupa kalimat dan input nilai ke variabel umur
    printf("Silahkan masukkan umur: \n");
    scanf("%d", &umur );

    // Block if jika umur lebih besar dari 11 maka dapat divaksin
    if (umur >= 6){
        printf("Umur Anda sudah 6 tahun ke atas. Anda dapat divaksin.\n");
    }
    // Block else jika kondisi if di atas tidak terpenuhi
    else{
        printf("Umur Anda kurang dari 6 tahun. Maaf, Anda tidak dapat divaksin.\n");
    }
    return 0;
}
