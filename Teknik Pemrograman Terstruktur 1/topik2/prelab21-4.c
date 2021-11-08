#include <stdio.h>

int main()
{
    // Deklarasi variabel platMobil dengan tipe data int
    int platMobil;

    // Menampilkan kalimat dan menginput nilai ke variabel platMobil
    printf("Masukkan nomor plat mobil Anda (nomornya saja): \n");
    scanf("%d", &platMobil );

    if (platMobil%2==0)
    {
        printf("Plat mobil Anda merupakan nomor genap");
    }
    else{
        printf("Plat mobil Anda merupakan nomor ganjil");
    }
    return 0;
}
