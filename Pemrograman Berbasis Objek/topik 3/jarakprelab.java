// Tuliskan definisi method static jarak di bawah!
// Hanya tuliskan definisi method. Jangan tuliskan program lengkap.
double jarak(Point p1,Point p2){
    double jarakresult;
    jarakresult = Math.sqrt(Math.pow(p2.getX() - p1.getX(),2) + Math.pow(p2.getY() - p1.getY(),2));
    return jarakresult;
}
