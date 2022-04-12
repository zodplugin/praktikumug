public static Mahasiswa buatMahasiswa(){
    Scanner scan = new Scanner(System.in);
    String nama,email;
    
    System.out.print("Masukkan nama: ");
    nama = scan.nextLine();
    
    System.out.print("Masukkan email: ");
    email = scan.nextLine();
    
    return new Mahasiswa(nama, email);
}