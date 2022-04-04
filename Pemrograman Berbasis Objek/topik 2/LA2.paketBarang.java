//paket barang

import java.util.Scanner;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

public class TarifPengiriman
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.print("Masukkan berat paket Anda (kg): ");
        double berat = scan.nextDouble();
        System.out.print("Masukkan jarak pengiriman (km): ");
        double jarak = scan.nextDouble();
        int jarakBulat = (int) jarak;
        double harga = 0;
        if(berat <= 2){
            harga += (jarakBulat*1500);
        } else if(berat > 2 && berat <= 6){
            harga += (jarakBulat*3000);
        } else if(berat > 6 && berat <= 10){
            harga += (jarakBulat*5000);
        } else if(berat > 10){
            harga += (jarakBulat*5500);   
        } else{
            System.out.println("Error, mohon masukkan berat dengan tepat.");
        }
        DecimalFormat kursIndonesia = (DecimalFormat)DecimalFormat.getCurrencyInstance();
        DecimalFormatSymbols formatRp = new DecimalFormatSymbols();
        formatRp.setCurrencySymbol("Rp.");
        formatRp.setMonetaryDecimalSeparator('.');
        formatRp.setGroupingSeparator(',');
        
        kursIndonesia.setDecimalFormatSymbols(formatRp);
        System.out.printf("Tarif Pengiriman = %s %n", kursIndonesia.format(harga));
    }
}