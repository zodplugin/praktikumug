

public class Dog
{
    private String nama;

    public Dog(String nama)
    {
        this.nama = nama;
    }

    public boolean equals(Object objectLain) {
        Dog dogLain = (Dog) objectLain;
        return nama.equals(dogLain.nama);
    }

    public static void main(String[] args)
    {
        Dog d1 = new Dog("Rufus");
        Dog d2 = new Dog("Sally");
        Dog d3 = new Dog("Rufus");
        Dog d4 = d3;
        System.out.println(d1.equals(d2));
        System.out.println(d2.equals(d3));
        System.out.println(d1.equals(d3));
        System.out.println(d3.equals(d4));
    }
}
