public class KapalPesiar extends Kapal {
    private int maksPenumpang;
    public KapalPesiar(String nama, int tahunPembuatan, int maksPenumpang) {
        super(nama, tahunPembuatan);
        this.maksPenumpang = maksPenumpang;
    }

    public int getMaksPenumpang() {
        return maksPenumpang;
    }

    public String toString() {
        return "Nama: "+ super.getNama() + "\nMaks. Penumpang: " + maksPenumpang;
    }

}
