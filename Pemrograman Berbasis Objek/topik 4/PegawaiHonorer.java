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
public class PegawaiHonorer extends Pegawai{
    private double honorPerJam;
    private double jamKerja;
    
    public PegawaiHonorer(String nama, double honorPerJam, double jamKerja){
        super(nama, honorPerJam);
        this.honorPerJam = honorPerJam;
        this.jamKerja = jamKerja;
    }
    
    @Override
    public double getGaji(){
        return (honorPerJam * jamKerja);
    }
}