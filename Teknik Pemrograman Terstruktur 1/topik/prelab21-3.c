#include <stdio.h>

int main()
{
	// Mendeklarasikan variabel a, b, dan hasil dengan tipe data integer
	int a,b,hasil;
	
	// Menampilkan output kalimat dan melakukan input nilai
	printf("Masukkan nilai a : \n"); 
	scanf("%d", &a);
	printf("Masukkan nilai b : \n"); 
	scanf("%d", &b );

    // Melakukan perhitungan dengan operator ternary dan hasilnya akan ditugaskan ke variabel hasil
	hasil  = ((a)>(b)) ? a:b; // Statement akan mengevaluasi kondisi a 
	                         // jika kondisi nilai a lebih kecil dari nilai b

	printf("Dari nilai a dan b yang di-input, nilai yang paling besar adalah : %d\n", hasil);
}
