/**
 *
 * @author RizkyBagaskara
 */
public class Kapal {
    private String nama;
    private int tahunPembuatan;
    
    public Kapal(String nama, int tahunPembuatan){
        this.nama = nama;
        this.tahunPembuatan = tahunPembuatan;
    }
    
    public String getNama(){
        return nama;
    }
    
    public int getTahunPembuatan(){
        return tahunPembuatan;
    }
    
     public String toString(){
        return String.format("Nama: %s\nTahun Pembuatan: %d", this.nama, this.tahunPembuatan);
    }
}
