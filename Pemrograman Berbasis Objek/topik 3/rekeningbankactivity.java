/*
    Class RekeningBank mensimulasikan sebuah rekening bank.
*/
public class RekeningBank 
{
    private double saldo;                      // Saldo rekening.
    
    // [1] Tambahkan field instance nomorRekening dan field static noRekTerakhir.
    private int nomorRekening;
    private static int noRekTerakhir = 1000;
    


    /*
        Constructor ini menetapkan saldo awal
        ke 0.0.
    */
    public RekeningBank()
    {
        // [2] Modifikasi constructor ini sehingga menetapkan field nomorRekening
        // dengan noRekTerakhir + 1.
        saldo = 0.0;
        nomorRekening = noRekTerakhir + 1;
        noRekTerakhir++;


    }    

    /*
        Constructor ini menetapkan saldo awal 
        ke nilai yang diberikan sebagai argument.
        @param saldoAwal Saldo awal.
    */
    public RekeningBank(double saldoAwal)
    {
        // [3] Modifikasi constructor ini sehingga menetapkan field nomorRekening
        // dengan noRekTerakhir + 1.
        saldo = saldoAwal;
        nomorRekening = noRekTerakhir + 1;
        noRekTerakhir++;

    }

    /*
        Method deposit menaruh sejumlah uang
        ke rekening.
        @param jumlah Jumlah yang ditambahkan ke
                      field saldo.
    */
    public void deposit(double jumlah)
    {
        saldo = saldo + jumlah;
    }

    /*
        Method withdraw menarik sejumlah uang
        dari rekening.
        @param jumlah Jumlah yang dikurangi dari
                      field saldo.
    */
    public void withdraw(double jumlah)
    {
        if (saldo >= jumlah)
        {
            saldo = saldo - jumlah;
        } 
        else
        {
            System.out.println("Dana tidak mencukupi.");
        }
    }

    /*
        Method setSaldo menetapkan saldo dari rekening.
        @param b Nilai untuk disimpan ke field saldo.

    */
    public void setSaldo(double s)
    {
        saldo = s;
    }

    /*
        Method getSaldo mengembalikan saldo rekening.
        @return Nilai dalam field saldo.
    */
    public double getSaldo()
    {
        return saldo;
    }
    
    // [4] Tambahkan method instance getNomorRekening
    // yang mengembalikan nomor rekening.
    
    public int getNomorRekening(){
        return nomorRekening;
    }






}
