public class Essay extends AktivitasBernilai
{
    private int grammar;
    private int pengejaan;
    private int panjangEssay;
    private int konten;

    public Essay(int grammar, int pengejaan, int panjangEssay, int konten){
        this.grammar = grammar;
        this.pengejaan = pengejaan;
        this.panjangEssay = panjangEssay;
        this.konten = konten;
        super.setSkor(grammar + pengejaan + panjangEssay + konten);
    }




}
