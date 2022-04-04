int alternatingSum(int[] angka){
    int result = 0;
    for (int i = 0; i < angka.length;i++){
        if (i%2 == 0){
            result += angka[i];
        }else{
            result -= angka[i];
        }
    }
    
    return result;
}
