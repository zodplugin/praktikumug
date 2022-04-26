/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Praktikum;

/**
 *
 * @author RizkyBagaskara
 */
public class MobilListrik extends Mobil{
    private int lamaRecharge;
    
    public void setLamaRecharge(int lamaRecharge){
        this.lamaRecharge = lamaRecharge;
    }
    
    public int getLamaRecharge(){
        return lamaRecharge;
    }
    
    public MobilListrik(){
       super();
       this.lamaRecharge = 0;
    }
    
    public MobilListrik(String pabrikan, String model, String warna, int kecepatanMax, int lamaRecharge){
        super.setPabrikan(pabrikan);
        super.setModel(model);
        super.setWarna(warna);
        super.setKecepatanMax(kecepatanMax);
        this.lamaRecharge = lamaRecharge;
    }
}
