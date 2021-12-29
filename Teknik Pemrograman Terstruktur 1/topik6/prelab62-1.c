#include <stdio.h>

// Deklarasi tipe union dengan nama union bilangan
union bilangan
{
    int x;
    double y;
};
int main()
{
    union bilangan nilai; // Deklarasi nama union dengan variabel union nilai
    nilai.x = 50; // Menginisialisasi variabel x untuk ditugaskan dengan nilai 50

    printf("Mencetak nilai dari variabel-variabel di dalam union:\n"); 
    // Mencetak nilai x
    printf("Nilai variabel x = %d\n",nilai.x);
    // Mencetak nilai y
    printf("Nilai variabel y = %f\n",nilai.y);
    
    return 0;
    
}
