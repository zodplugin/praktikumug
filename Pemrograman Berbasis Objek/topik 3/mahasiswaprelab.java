import java.util.Scanner;

public class ArrayMahasiswa 
{
    public static void main(String[] args)
    {
        String nama;    // Untuk menyimpan input nama
        String email;   // Untuk menyimpan input email

        Scanner keyboard = new Scanner(System.in);

        // Buat sebuah array bertipe data Mahasiswa dengan lima elemen.
        // Referensikan array tersebut ke variabel mhs.
        
        Mahasiswa[] mhs = new Mahasiswa[5];


        // Minta pengguna untuk memasukkan nama, tingkat, dan email
        // setiap mahasiswa.
        for (int i = 0; i < mhs.length;i++)
        {
            System.out.println("Input mahasiswa ke-" + (i + 1) + ":");
            System.out.print("Nama: ");
            nama = keyboard.nextLine();
            System.out.print("Email: ");
            email = keyboard.nextLine();
            // Buat object Mahasiswa untuk elemen array ke-i.
            
            mhs[i] = new Mahasiswa(nama,email);

        }

        System.out.println();
        // Tampilkan data semua mahasiswa
        System.out.println("Data Mahasiswa: ");
        for (int i = 0; i < mhs.length; i++)
        {
            
            System.out.println(i+1+". "+mhs[i].getData());

        }
    }    
}
