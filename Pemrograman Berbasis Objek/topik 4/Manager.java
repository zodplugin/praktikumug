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
public class Manager extends Pegawai{
    private double bonus;
    
    public Manager(String nama, double gajiPokok, double bonus){
        super(nama, gajiPokok);
        this.bonus = bonus;
    }

    @Override
    public double getGaji(){
        return(super.getGaji() + bonus);
    }
}