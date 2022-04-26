public class MobilListrik extends Mobil{

    private int lamaRecharge ;

    public MobilListrik(String pabrikan, String model, String warna, int kecepatanMaxm, int lamaRecharge)
    {
        super.setPabrikan(pabrikan);
        super.setModel(model);
        super.setWarna(warna);
        super.setKecepatanMax(kecepatanMaxm);
        this.lamaRecharge = lamaRecharge;
    }

    public MobilListrik()
    {
        super();
    }

    public void setLamaRecharge(int kecepatan)
    {
        lamaRecharge  = lamaRecharge + kecepatan;
    }

    public int getLamaRecharge()
    {
        return lamaRecharge ;
    }



}
