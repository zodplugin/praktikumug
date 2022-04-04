// [1] Tulis definisi method firstDigit di bawah.
public static int firstDigit(int digit){
    String digitx = Integer.toString(digit);
    int[] digitArr = new int[digitx.length()];
    for (int i = 0; i < digitArr.length;i++){
        digitArr[i] = Character.getNumericValue(digitx.charAt(i));
    }
    
    return digitArr[0];
}



// [2] Tulis definisi method lastDigit di bawah.
public static int lastDigit(int digit){
    String digitx = Integer.toString(digit);
    int[] digitArr = new int[digitx.length()];
    for (int i = 0; i < digitArr.length;i++){
        digitArr[i] = Character.getNumericValue(digitx.charAt(i));
    }
    
    return digitArr[digitArr.length-1];
}





// [3] Tulis definisi method banyakDigit di bawah.

public static int banyakDigit(int digit){
    String digitx = Integer.toString(digit);
    int[] digitArr = new int[digitx.length()];
    for (int i = 0; i < digitArr.length;i++){
        digitArr[i] = Character.getNumericValue(digitx.charAt(i));
    }
    
    return digitArr.length;
}

