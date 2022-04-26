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
public class RekeningMinMax extends RekeningBank{
    private double saldoMax, saldoMin;
    
    public RekeningMinMax(String nomorRekening, double saldo){
        super(nomorRekening, saldo);
        this.saldoMax = 0;
        this.saldoMin = 0;
        
    }
    
    public double getSaldoMax(){
        return this.saldoMax;
    }
    
    public double getSaldoMin(){
        return this.saldoMin;
    }
    
    @Override
    public void deposit(double jumlah){
        super.deposit(jumlah);
        saldoMax = saldoMax == 0 ? super.getSaldo() : saldoMax;
        if (super.getSaldo() > saldoMax){
            this.saldoMax = super.getSaldo();
        }
    }
    
    @Override
    public void withdraw(double jumlah){
        super.withdraw(jumlah);
        saldoMin = saldoMin == 0 ? super.getSaldo() : saldoMin;
        if (super.getSaldo() < saldoMin){
            this.saldoMin = super.getSaldo();
        }
    }
}