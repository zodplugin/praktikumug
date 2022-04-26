/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 *
 * @author RizkyBagaskara
 */
public class KapalPesiar extends Kapal {
    private int maksPenumpang;
    
    public KapalPesiar(String nama, int tahunPembuatan, int maksPenumpang){
        super(nama, tahunPembuatan);
        this.maksPenumpang = maksPenumpang;
    }
    
    public int getMaksPenumpang(){
        return this.maksPenumpang;
    }
    
    @Override
    public String toString(){
        return String.format("Nama: %s\nMaks. Penumpang: %d", super.getNama(), this.maksPenumpang);
    }
}
