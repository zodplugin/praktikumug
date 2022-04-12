import java.util.Scanner;

public class TesBujurSangkar 
{
    public static void main(String[] args)
    {
        double sisi;    // Untuk menyimpan input dari pengguna.
        
        // Buat object Scanner untuk mendapatkan input pengguna.
        Scanner keyboard = new Scanner(System.in);

        // Buat sebuah object bujur sangkar dan referensikan ke variabel kotak.
        
        BujurSangkar kotak = new BujurSangkar();

        
        // Minta pengguna memasukkan sisi bujur sangkar dan
        // simpan input pengguna ke variabel sisi.
        System.out.print("Masukkan sisi bujur sangkar: ");
        
        sisi = keyboard.nextDouble();

        
        // Simpan nilai yang dimasukkan pengguna ke field sisi.
        
        kotak.setSisi(sisi);

        
        // Tampilkan luas bujur sangkar.
        System.out.println("Luas bujur sangkar = " + kotak.getLuas());
    }        
}
