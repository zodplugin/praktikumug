public class Karyawan
{
    private String nama,departemen,posisi;
    private int nomorId;
    public Karyawan(){
        
    }
    
    public Karyawan(String nama,int nomorId){
        this.nama = nama;
        this.nomorId = nomorId;
    }
    public Karyawan(String nama,int nomorId,String departemen,String posisi){
        this.nama = nama;
        this.nomorId = nomorId;
        this.departemen = departemen;
        this.posisi = posisi;
    }
    
    public void setNama(String nama){
        this.nama = nama;
    }
    public void setNomorId(int noId){
        this.nomorId = noId;
    }
    public void setDepartemen(String dept){
        this.departemen = dept;
    }
    public void setPosisi(String pos){
        this.posisi = pos;
    }
    public String getNama(){
        return nama;
    }
    public int getNomorId(){
        return nomorId;
    }
    public String getDepartemen(){
        return departemen;
    }
    public String getPosisi(){
        return posisi;
    }
 	
 	
}
