package Praktikum;

/**
 *
 * @author RizkyBagaskara
 */
import java.lang.Math;
public class VolumeBola {
    public static void main(String[] args) {
        double r = 7.5; // Jari-jari bola
        double volume;  // Untuk menyimpan hasil penghitungan volume bola
    
        // [1] Hitung volume bola
        volume = (4.0 / 3) * Math.PI * Math.pow(r, 3);

        // [2] Tampilkan volume bola
        System.out.println("Volume bola = "+ volume);
    }
}
