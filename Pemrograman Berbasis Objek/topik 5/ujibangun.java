public class UjiBangun 
{
    public static void main(String[] args)
    {
        // Buat array empat elemen bertipe Bangun.
        Bangun[] obj = new Bangun[4];
        
        // Isi array dengan object-object berupa subclass dari Bangun.
        obj[0] = new PersegiPanjang(7.5, 5.0);
        obj[1] = new Lingkaran(4.5);
        obj[2] = new BujurSangkar(12.5);
        obj[3] = new SegitigaSiku(10.0, 7.5);

        // Cetak Daftar Bangun
        System.out.println("Daftar Bangun:");
  
        // Loop untuk mencetak informasi setiap object
        for (int i = 0; i < obj.length; i++)
        {
            System.out.println();
            // Cetak Judul nomor bangun.
            System.out.println("Bangun " + (i + 1) + ": ");
            // Cetak luas bangun
            System.out.println("Luas = "+ obj[i].getLuas());
            System.out.print("Jenis: ");

            // Statement if untuk menguji class dari setiap object
            // dan menampilkan informasi setiap object.
            
            // Case 1: Jika object adalah dari class PersegiPanjang
            if (obj[i] instanceof PersegiPanjang)
            {
                // Cetak Persegi Panjang
                System.out.println("Persegi Panjang");
                // Casting ke tipe PersegiPanjang
                PersegiPanjang p = (PersegiPanjang) obj[i];

                // Cetak panjang dan lebar
                System.out.println("panjang = "+ p.getPanjang() + ", lebar= "+ p.getLebar());
            }
            // Case 2: Jika object adalah dari class BujurSangkar
            else if (obj[i] instanceof BujurSangkar)
            {
                // Cetak Bujur Sangkar
                System.out.println("Bujur Sangkar");
                // Casting ke tipe BujurSangkar
                BujurSangkar b = (BujurSangkar) obj[i];

                // Cetak sisi
                System.out.println("sisi = "+b.getPanjang());                
            }
            // Case 3: Jika object adalah dari class Lingkaran
            else if (obj[i] instanceof Lingkaran)
            {
                // Cetak Lingkaran
                System.out.println("Lingkaran");
                // Casting ke tipe Lingkaran
                Lingkaran l = (Lingkaran) obj[i];

                // Cetak radius
                System.out.println("radius = "+ l.getRadius());
            }
            // Case 4: Jika object adalah dari class SegitigaSiku
            else if ( obj[i] instanceof SegitigaSiku)
            {
                // Cetak Segitiga Siku
                System.out.println("Segitiga Siku");
                // Casting ke tipe SegitigaSiku
                SegitigaSiku s = (SegitigaSiku) obj[i];

                // Cetak alas dan tinggi
                System.out.println("alas = "+ s.getAlas() + ", tinggi = "+ s.getTinggi());
            }
        }
    }    
}
