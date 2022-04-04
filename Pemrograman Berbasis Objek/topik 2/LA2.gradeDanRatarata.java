import java.util.Scanner;

public class NilaiUjian 
{
    // Tuliskan definisi-definisi method yang diperlukan di bawah comment ini.
    static double hitungRatarata(double a, double b, double c, double d, double e){
        return (a+b+c+d+e)/5;
    }
    public static String tentukanGrade(double a){
        String hasil = a >= 90 ? "A" :
        a < 90 && a >= 80 ? "B":
        a < 80 && a >= 70 ? "C":
        a < 70 && a >= 60 ? "D": "E";
        return hasil;
    }

    /****************************************
     *  !!! JANGAN UBAH KODE DI BAWAH !!!   *
     ****************************************/
    public static void main(String[] args)
    {
        double nilai1;
        double nilai2;
        double nilai3;
        double nilai4;
        double nilai5;
        double ratarata;

        Scanner keyboard = new Scanner(System.in);

        System.out.print("Masukkan nilai ujian ke-1: ");
        nilai1 = keyboard.nextDouble();
        
        System.out.print("Masukkan nilai ujian ke-2: ");
        nilai2 = keyboard.nextDouble();

        System.out.print("Masukkan nilai ujian ke-3: ");
        nilai3 = keyboard.nextDouble();

        System.out.print("Masukkan nilai ujian ke-4: ");
        nilai4 = keyboard.nextDouble();

        System.out.print("Masukkan nilai ujian ke-5: ");
        nilai5 = keyboard.nextDouble();

        ratarata = hitungRatarata(nilai1, nilai2, nilai3, nilai4, nilai5);

        System.out.println("Rata-rata nilai ujian = " + ratarata);
        System.out.println("Grade Anda = " + tentukanGrade(ratarata));

    }
}