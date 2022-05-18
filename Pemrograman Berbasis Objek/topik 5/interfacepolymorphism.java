public class InterfacePolymorphism 
{
  public static void main(String[] args)
  {
    BarangRitel[] produk = new BarangRitel[4];
    produk[0] = new CompactDisc("07 Des", "Sheila on 7", 50000);
    produk[1] = new CompactDisc("Let It Be", "Beatles", 75000);
    produk[2] = new DVD("Avengers: Endgame", 181, 200000);
    produk[3] = new DVD("The Raid", 101, 185000);

    // Loop untuk mencetak informasi setiap object
    for (int i = 0; i < produk.length ;i++)
    {
       // Cetak Nama Produk
       System.out.print("Nama: "+produk[i].getNamaProduk()+", ");
       // Cetak Harga Ritel
       System.out.printf("Harga: Rp%,.2f \n",produk[i].getHargaRitel());
    }    
}
