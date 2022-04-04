double minimum(double[] nilai){
    double minx = nilai[0];
    for (int i = 0; i < nilai.length;i++){
        if(nilai[i] < minx){
            minx = nilai[i];
        }
    }
    return minx;
}
