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
public class Lingkaran extends Bangun{
    private double radius;
    
    public void setRadius(double radius){
        this.radius = radius;
        super.setLuas(Math.PI*radius*radius);
    }
    
    public double getRadius(){
        return this.radius;
    }
}
