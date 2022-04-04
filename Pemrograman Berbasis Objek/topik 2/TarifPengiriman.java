import java.util.Scanner;

public class TarifPengiriman
{
    public static void main(String[] args)
    {
        double berat,jarak,harga,result;
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan berat paket Anda (kg): ");
        berat = input.nextDouble();
        System.out.print("Masukkan jarak pengiriman (km): ");
        jarak = input.nextDouble();
        if ((berat >=0) && (berat <= 2.0)){
            harga = 1500;
            result = harga * (int)jarak;
            System.out.printf("Tarif Pengiriman = Rp.%,.2f",result);
        }else if ((berat > 2.0) && (berat <=6.0)){
            harga = 3000;
            result = harga * (int)jarak;
            System.out.printf("Tarif Pengiriman = Rp.%,.2f",result);
        }else if ((berat > 6.0) && (berat <=10.0)){
            harga = 5000;
            result = harga * (int)jarak;
            System.out.printf("Tarif Pengiriman = Rp.%,.2f",result);
        }else if(berat > 10.0){
            harga = 5500;
            result = harga * (int)jarak;
            System.out.printf("Tarif Pengiriman = Rp.%,.2f",result);
        }
        
        
        
        
        
        
    }
}

  
  
