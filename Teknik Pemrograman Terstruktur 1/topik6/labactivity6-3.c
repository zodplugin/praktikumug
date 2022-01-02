  // Program deklarasi typedef
#include <stdio.h>

// Deklarasi typedef dengan tipe data awal integer dan nama alias age
typedef int age;
 
int main()
{
    //Deklarasi variabel a1 dan a2 dengan nama alias
    age a1;
    age a2;
 
    a1 = 123456;
    printf("Isi variabel a1: %d \n",a1);
 
    a2 = 234513;
    printf("Isi variabel a2: %d \n",a2);
 
    return 0;
    
}
   
