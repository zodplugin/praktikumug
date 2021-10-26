// Program inputData.c
#include <stdio.h>

// Fungsi main untuk memulai eksekusi program
int main()
{
    // Deklarasi variabel x dan y dengan tipe data integer
    int x;
    int y;
    
    // Mencetak output kalimat dan menginput variabel x dan y 
    // dalam satu statement dengan 2 digit field pada variabel x 
    printf("Masukkan enam digit angka: \n");
    scanf("%2d", &x);
    scanf("%4d", &y);
    

    // Mencetak output variabel x dan y dalam satu statement
    printf("\nInteger yang di-input adalah %d dan %d\n", x , y );
	
} // Mengakhiri fungsi main()
