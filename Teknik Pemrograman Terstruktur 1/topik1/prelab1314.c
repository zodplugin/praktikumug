// Program var.c
#include <stdio.h>

int main()
{
    // Mendefinisikan variabel a, b, x, f, dan y yang bertipe data integer 
    int a,b,x,f,y ;
  
    // Menginisialisasikan nilai pada variabel a, b, x, dan y
    a = 5;
    b = 1;
    x = 10;
    y = 5;

    //Melakukan operasi aritmatika pada variabel f 
    f = (a - b)*(x - y);

    //Mencetak nilai variabel f 
    printf("nilai f: %d \n",f);
    
    return 0; 
}
