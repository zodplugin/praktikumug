package Praktikum;

import java.util.Scanner;

/**
 *
 * @author RizkyBagaskara
 */
public class PreLab_Topik2 {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.print("Masukkan nilai n: ");
        int n = keyboard.nextInt();
        do
            {
             System.out.println("Halo");
                n++;
            }
        while (n < 50);
    }
}

//Code prelab ada di dalam class
class small{
    public static double smallest(double num1, double num2, double num3){
    double a = Math.min(num1,num2);
    return Math.min(a,num3);
    }
}

class berbeda{
    public static boolean semuaBerbeda(double num1, double num2, double num3){
    boolean semuaBerbeda;
    if(num1 == num2 && num2 == num3 && num1 == num3){
        semuaBerbeda = false;
    }else if(num1 == num2 && num2 == num3 || num1 == num3){
        semuaBerbeda = false;
    }else{
        semuaBerbeda = true;
    }
    return semuaBerbeda;
    }
}

class waktu{
    public static void kerja(){
//     Cuma buat inisialisasi
     int jam = 0, gaji = 0;
     if(jam > 40)
     {
        gaji *=1.5;
     }
  }  
}

class readDouble{
    public static double readDouble(String prompt){
    System.out.print(prompt+" ");
    Scanner scan = new Scanner(System.in);
    return scan.nextDouble();
    }
}
