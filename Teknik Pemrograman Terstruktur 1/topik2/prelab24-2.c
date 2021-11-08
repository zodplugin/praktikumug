#include <stdio.h>

int main()
{
	// Mendeklarasikan variabel
	float hargaPaket1, hargaPaket2, hargaPaket3, kuantitas, diskon, totalBayar;
	int menu;
	
	// Menginisialisasi variabel
	hargaPaket1 = 20000;
	hargaPaket2 = 25000;
	hargaPaket3 = 30000;
	diskon = 0.06;

    // Mencetak kalimat output dan input nilai ke variabel menu
	printf("1. Paket 1: nasi + ayam + air putih\n");
	printf("2. Paket 2: nasi + ayam + es teh manis\n");
	printf("3. Paket 3: nasi + ayam + tahu tempe + eh teh manis\n");
	printf("Masukkan menu yang ingin Anda pesan [1 - 3]: \n");
	scanf("%d", &menu );
	printf("\n");

    // Menggunakan block statement if jika menu 1 yang dipilih
	if (menu == 1)
	{
		printf("Menu yang Anda pesan Paket 1: nasi + ayam + air putih\n");
		printf("Berapa jumlah paket yang dipesan? ");
		scanf("%f", &kuantitas);

		if (kuantitas >= 3) // Memilih menu 1 dan jika paket yang dipesan 3 atau lebih
		{
			printf("\nTotal pembelian kamu adalah %.f paket. Kamu berhak mendapat diskon sebanyak 6 persen!\n", kuantitas );
			totalBayar = (kuantitas * hargaPaket1) - (kuantitas * hargaPaket1 * diskon);
			printf("Total yang harus kamu bayar adalah : Rp. %.2f,-\n", totalBayar);
		}

		else if (kuantitas < 3) // Memilih menu 1 dan jika paket yang dipesan kurang dari 3 
		{
			printf("\nTotal pembelian kamu adalah %.f paket.\n", kuantitas);
			totalBayar = (kuantitas * hargaPaket1);
			printf("Total yang harus kamu bayar adalah : Rp. %.2f,-\n", totalBayar);
		}

	}
    // Menggunakan block statement else-if jika menu 2 yang dipilih
	else if (menu == 2 )
	{
		printf("Menu yang Anda pesan Paket 2: nasi + ayam + es teh manis\n");
		printf("Berapa jumlah paket yang dipesan? ");
		scanf("%f", &kuantitas);

		if (kuantitas >= 3) // Memilih menu 2 dan jika paket yang dipesan 3 atau lebih
		{
			printf("\nTotal pembelian kamu adalah %.f paket. Kamu berhak mendapat diskon sebanyak 6 persen!\n", kuantitas );
			totalBayar = (kuantitas * hargaPaket2) - (kuantitas * hargaPaket2 * diskon);
			printf("Total yang harus kamu bayar adalah : Rp. %.2f,-\n", totalBayar);
		}

		else if (kuantitas < 3) // Memilih menu 2 dan jika paket yang dipesan kurang dari 3
		{
			printf("\nTotal pembelian kamu adalah %.f paket.\n", kuantitas);
			totalBayar = (kuantitas * hargaPaket2);
			printf("Total yang harus kamu bayar adalah : Rp. %.2f,-\n", totalBayar);
		}

	}
	// Menggunakan block statement else-if jika menu 3 yang dipilih
	else if (menu == 3)
	{
		printf("Menu yang Anda pesan Paket 3: nasi + ayam + tahu tempe + es teh manis\n");
		printf("Berapa jumlah paket yang dipesan? ");
		scanf("%f", &kuantitas);

		if (kuantitas >= 3) // Memilih menu 3 dan jika paket yang dipesan 3 atau lebih
		{
			printf("\nTotal pembelian kamu adalah %.f paket. Kamu berhak mendapat diskon sebanyak 6 persen!\n", kuantitas );
			totalBayar = (kuantitas * hargaPaket3)-(kuantitas * hargaPaket3 * diskon);
			printf("Total yang harus kamu bayar adalah : Rp. %.2f,-\n", totalBayar);
		}

		else if (kuantitas < 3) // Memilih menu 3 dan jika paket yang dipesan kurang dari 3
		{
			printf("\nTotal pembelian kamu adalah %.f paket.\n", kuantitas);
			totalBayar = (kuantitas * hargaPaket3);
			printf("Total yang harus kamu bayar adalah : Rp. %.2f,-\n", totalBayar);
		}
	}
}
