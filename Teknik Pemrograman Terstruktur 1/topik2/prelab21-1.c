#include <stdio.h>

int main()
{
	// Mendeklarasikan variabel totalBelanja dan gratisOngkir
	float totalBelanja,gratisOngkir;

    // Menampilkan output dan melakukan input ke variabel totalBelanja
  	printf("Masukkan total belanja Anda : Rp. \n");
  	scanf("%f",&totalBelanja);

    // Block statement if, jika totalBelanja lebih besar atau sama dengan 75000 maka akan mendapatkan ongkir
    if (totalBelanja >= 75000)
  	{
  	        gratisOngkir = 20000;
            printf("Total belanja Anda : Rp. %.2f\n", totalBelanja);
            printf("Selamat! Anda mendapatkan gratis ongkir sebesar Rp. %.2f\n", gratisOngkir );
 	}
 	// Block statement else dijalankan jika kondisi if di atas tidak terpenuhi
 	else
 	{
      	    gratisOngkir = 0;
       	    printf("Total belanja Anda : Rp. %.2f\n", totalBelanja);
    	      printf("Maaf, Anda belum mendapatkan gratis ongkir. \n");
 	}

    return 0;
}
