package Praktikum;

/**
 *
 * @author RizkyBagaskara
 */

class Digits{
// [1] Tulis definisi method firstDigit di bawah.
public static int firstDigit(int digit1){
      while (digit1 >= 10){
            digit1 /= 10;
     
        // return the first digit
      }    
      return digit1;
}

// [2] Tulis definisi method lastDigit di bawah.
public static int lastDigit(int digit3){
   return (digit3 % 10);
}

// [3] Tulis definisi method banyakDigit di bawah.
public static int banyakDigit(int n){
   int count = 0;
   while (n != 0){
       n /= 10;
       ++count;
    }
   return count;
    }
}