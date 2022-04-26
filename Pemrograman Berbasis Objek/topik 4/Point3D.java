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
public class Point3D extends Point2D{
    private int z;
    
    public void setZ(int z){
        this.z = z;
    }
    
    public int getZ(){
        return z;
    }
    
    public Point3D(){
       super();
       this.z = 0;
    }
    
    public Point3D(int x, int y, int z){
        super.setX(x);
        super.setY(y);
        this.z = z;
    }
}
