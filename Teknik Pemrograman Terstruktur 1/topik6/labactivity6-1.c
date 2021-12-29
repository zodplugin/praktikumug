// Program deklarasi typedef struct
#include <stdio.h>
#include <string.h>

// Deklarasi typedef dengan tipe data awal struct dan nama alias Date
typedef struct 
{
    int day;
    char month[4];
    int year;
} Date;

 
int main()
{
    // Deklarasi variabel dob dengan nama alias
    Date dob;
    
    // Inisialisasi variabel day dengan nilai yang ditugaskan adalah 14
    dob.day = 14;
    
    // Inisialisasi variabel month dengan nilai yang ditugaskan adalah "Nov" menggunakan fungsi strcpy
    strcpy(dob.month,"Nov");
    
    // Inisialisasi variabel year dengan nilai yang ditugaskan adalah 2015
    dob.year = 2015;
    
    // Mencetak nilai month, day, dan year
    printf("%s %d, %d",dob.month,dob.day,dob.year);
        
    return 0;
    
}
