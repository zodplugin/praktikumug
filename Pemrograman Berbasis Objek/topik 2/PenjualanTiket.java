package Praktikum;

import java.util.Scanner;

/**
 *
 * @author RizkyBagaskara
 */
public class PenjualanTiket {
    public static void main(String[] args) {
        int totalTiket = 10;
        int beli, jumlahTiket,sisaTiket,count = 0;
        Scanner keyboard = new Scanner(System.in);
        
        while(totalTiket > 0){
            System.out.print("Masukkan jumlah tiket yang ingin dibeli: ");
            jumlahTiket = keyboard.nextInt();
            if(jumlahTiket > 4){
                System.out.println("Anda tidak bisa membeli lebih dari 4 tiket.");
                continue;
            }
            
            if(jumlahTiket <= totalTiket){
                System.out.println("Anda membeli sebanyak "+jumlahTiket+" tiket.");
                totalTiket -= jumlahTiket;
                if(totalTiket >0){
                 System.out.println("Sisa tiket yang tersedia: "+totalTiket);
                }
            }else{
                System.out.println("Maaf, sisa tiket yang tersisa adalah "+totalTiket+" tiket.");
                continue;
            }
            count++;
        } 
        System.out.println("Semua tiket telah terjual kepada "+count+" pembeli.");
    }
}
