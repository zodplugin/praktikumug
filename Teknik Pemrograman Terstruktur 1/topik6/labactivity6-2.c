// Program deklarasi typedef struct
#include <stdio.h>
#include <string.h>

// Deklarasi typedef dengan tipe data awal struct dengan nama struct adalah student dan nama alias st
typedef struct student
{
    char name[50];
    int score;
} st;

 
int main()
{
    // Deklarasi variabel s1 dengan nama alias
    st s1;
    
    
    // Inisialisasi variabel name dengan nilai yang ditugaskan adalah "James" menggunakan fungsi strcpy
    strcpy(s1.name, "James");
    
    // Inisialisasi variabel score dengan nilai yang ditugaskan adalah 100
    s1.score = 100;
    
    // Mencetak nilai name dan score
    printf("%s mendapatkan nilai %d pada saat ujian lisan.", s1.name, s1.score);
    
    return 0;
}
