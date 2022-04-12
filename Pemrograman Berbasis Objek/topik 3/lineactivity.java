public class Line
{
    Point p1,p2;
    public Line(Point p1,Point p2){
        this.p1 = p1;
        this.p2 = p2;
    }
    
    public Point getP1(){
        return p1;
    }
    
    public Point getP2(){
        return p2;
    }
    public String toString(){
        String a = "["+p1+", "+p2+"]";
        return a;
    }
    
    public double getSlope(){
        double result = ((double)p2.getY() - (double)p1.getY()) / ((double)p2.getX() - (double)p1.getX());
        return result;
    }
    
}
