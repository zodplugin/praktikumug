public class RekeningBank {
    private String nomorRekening;
    private double saldo;

    public RekeningBank(String nomorRekening, double saldo)
    {
        this.nomorRekening = nomorRekening;
        this.saldo = saldo;
    }

    public String getNomorRekening()
    {
        return nomorRekening;
    }

    public double getSaldo()
    {
        return saldo;
    }

    // [1] Tambahkan method toString di bawah.

    public String toString()
    {
        return nomorRekening + ", " + saldo;
    }
    // [2] Tambahkan method equals di bawah.

    public boolean equals(Object obj)
    {
        if (obj instanceof RekeningBank)
        {
            RekeningBank rekening = (RekeningBank) obj;
            return nomorRekening.equals(rekening.getNomorRekening());
        }

        return false;
    }

}
