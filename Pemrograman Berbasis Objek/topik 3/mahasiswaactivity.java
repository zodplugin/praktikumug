public class Mahasiswa
{
    private String nama;
    private int skor;
    private double banyaknyaskor;
    
    public Mahasiswa(String nama){
        this.nama = nama;
    }
    public void addSkor(int skor){
        this.skor = this.skor + skor;
        banyaknyaskor++;
    }
    public String getNama(){
        return nama;
    }
    public int getTotalSkor(){
        return skor;
    }
    public double getAverageSkor(){
        return skor/banyaknyaskor;
    }
}
