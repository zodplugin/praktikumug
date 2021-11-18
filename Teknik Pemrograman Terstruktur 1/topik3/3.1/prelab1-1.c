#include<stdio.h>

int main()
{
    // Deklarasi variabel a, b, dan c dengan tipe data int
    int a,b,c;
    a = 15;     // Menugaskan a dengan nilai 15
    b = 5;             // Menugaskan b dengan nilai 5
    c = a+b;// Hitung variabel c dengan a ditambah dengan b
    
    a++;    // Post-increment variabel a
    // Sekarang nilai variabel a adalah 16
    printf("Setelah post-increment, a = %d\n", a); 
     
    b--;     // Post-decrement variabel b
    // Sekarang nilai variabel b adalah 4
    printf("Setelah post-decrement, b = %d\n", b); 
    b++;    // Post-increment variabel b, sekrang nilai variabel b adalah 5
     
    // Variabel c ditugaskan kembali dengan a + b, sehingga 16 + 5
    c = a + b;
    // Mencetak kalimat dan memanggil variabel c
    printf("Nilai a + b = %d\n", c);

    return 0;
}
