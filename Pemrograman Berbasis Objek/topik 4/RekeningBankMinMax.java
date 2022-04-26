public class RekeningMinMax extends RekeningBank{
    private double saldoMax;
    private double saldoMin;


    public RekeningMinMax(String nomorRekening, double saldo) {
        super(nomorRekening, saldo);
        this.saldoMax = 0;
        this.saldoMin = 0;
    }

    public double getSaldoMax() {
        return saldoMax;
    }
    public double getSaldoMin() {
        return saldoMin;
    }

    public void deposit(double jumlah) {
        super.deposit(jumlah);
        if (saldoMax == 0){
            saldoMax = super.getSaldo();
        }
        if (saldoMax < super.getSaldo()) {
            saldoMax = super.getSaldo();
        }
    }

    public void withdraw(double jumlah) {
        super.withdraw(jumlah);
        if (saldoMin == 0){
            saldoMin = super.getSaldo();
        }

        if (saldoMin > super.getSaldo()) {
            saldoMin = super.getSaldo();
        }
    }
}
