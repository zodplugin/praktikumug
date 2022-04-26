/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 *
 * @author RizkyBagaskara
 */
public class KapalKargo extends Kapal{
     private int kapasitasAngkut;
    
    public KapalKargo(String nama, int tahunPembuatan, int kapasitasAngkut){
        super(nama, tahunPembuatan);
        this.kapasitasAngkut = kapasitasAngkut;
    }
    
    public int getKapasitasAngkut(){
        return this.kapasitasAngkut;
    }
    
    @Override
    public String toString(){
        return String.format("Nama: %s\nKapasitas Angkut: %d", super.getNama(), this.kapasitasAngkut);
    }
}
