#include <stdio.h>

int main()
{
    // Deklarasi union dengan nama union elemenPersegi
    union elemenPersegi
    {
        int sisi1;
        int sisi2;
    };


    // Deklarasi nama union dengan variabel union Persegi dan menugaskannya dengan nilai {6}
    union elemenPersegi Persegi  = {6} ; // Angka 6 secara otomatis masuk ke dalam variabel sisi1

    // Inisialisasi nama union elemenPersegi dengan variabel pointer *ptr dan menugaskannya dengan nilai &Persegi
    union elemenPersegi *ptr = &Persegi  ;

       // Inisialisasi variabel LuasPersegi
       // Dan menugaskannya dengan nilai sisi1 * sisi2 dengan menggunakan pointer
    int LuasPersegi = ptr ->sisi1 * ptr->sisi2;

       // Mencetak nilai LuasPersegi
    printf("Luas Persegi adalah = %d\n", LuasPersegi);

    return 0;
    