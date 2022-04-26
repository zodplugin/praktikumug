public class Manager extends Pegawai
{
    private double bonus;

    public Manager(String nama, double gajiPokok, double bonus)
    {
        super(nama, gajiPokok);
        this.bonus = bonus;
    }

    public double getGaji()
    {
        return super.getGaji() + bonus;
    }
}
