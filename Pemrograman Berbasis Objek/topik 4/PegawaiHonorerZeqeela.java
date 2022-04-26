public class PegawaiHonorer extends Pegawai{

    private double honorPerJam;
    private double jamKerja;

    public PegawaiHonorer(String nama,double honorPerJam, double jamKerja)
    {
        super(nama,0);
        this.honorPerJam = honorPerJam;
        this.jamKerja = jamKerja;
    }


    public double getGaji(){
        return (honorPerJam * jamKerja);
    }

    
}
