double getAverage(int[] arr){
    double total = 0;
    for ( int i = 0; i < arr.length; i++){
        total = total +  arr[i];
    }
    total = total/arr.length;
    return total;
}
