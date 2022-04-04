public static double readDouble(String prompt)
{
    double cek;
    // Tuliskan kode method readDouble di bawah comment ini.
    Scanner inpot = new Scanner(System.in);
    System.out.print(prompt+" ");
    cek = inpot.nextDouble();
    return cek;
    
}
