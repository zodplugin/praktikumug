public class PopulasiBakteri
{
    public static void main(String[] args)
    {
        int popAwal = 150000;   // Populasi awal
        int t = 10;             // Durasi waktu
        int popAkhir;           // Untuk menyimpan populasi akhir
        
        // [1] Hitung populasi akhir.
        // Populasi akhir harus dalam nilai bulat.
        popAkhir = (int)(popAwal*Math.exp(0.5*t));
       
        
        // [2] Cetak populasi awal dan populasi akhir.
        System.out.println("Populasi awal = "+popAwal);
        System.out.println("Populasi akhir = "+popAkhir);


    }
}
