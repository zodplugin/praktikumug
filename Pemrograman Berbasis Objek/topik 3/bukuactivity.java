public class Buku implements BarangRitel{
    private String judul;
    private String pengarang;
    private double hargaritel;

    public Buku(String judul, String pengarang, double hargaritel){
        this.judul = judul;
        this.pengarang = pengarang;
        this.hargaritel = hargaritel;
    }


    @Override
    public double getHargaRitel() {
        return hargaritel;
    }
    
    public String getJudul(){
        return judul;
    }
    
    public String getPengarang(){
        return pengarang;
    }
}
