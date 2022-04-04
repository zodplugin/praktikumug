//first,last, totalDigits babyy

// [1] Tulis definisi method firstDigit di bawah.
static int firstDigit(int a){
    int banyakDigit = (int) Math.log10(a);
    return (int)(a/(int) Math.pow(10,banyakDigit));
}


// [2] Tulis definisi method lastDigit di bawah.
static int lastDigit(int a){
    return a % 10;
}


// [3] Tulis definisi method banyakDigit di bawah.
static int banyakDigit(int a){
    return (int) Math.log10(a)+1;
}