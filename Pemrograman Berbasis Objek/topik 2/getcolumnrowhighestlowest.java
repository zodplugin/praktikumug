public static double getTotal(double[][] arr){
        double total = 0;
        for(int x = 0; x < arr.length; x++){
            for(int y = 0; y < arr[0].length; y++){
                total += arr[x][y];
            }
        }
        return total;
    }

    public static double getAverage(double[][] arr){
        return getTotal(arr)/(arr.length*arr[0].length);
    }

    public static double getRowTotal(double[][] arr, int row){
        double total = 0;
        for(int x = 0; x < arr[0].length; x++){
            total += arr[row][x];
        }
        return total;
    }

    public static double getColumnTotal(double[][] arr, int col){
        double total = 0;
        for(int x = 0; x < arr.length; x++){
            total += arr[x][col];
        }
        return total;
    }

    public static double getHighestInRow(double[][] arr, int row){
        double highest = 0;
        for(int x = 0; x < arr[0].length; x++){
            if(x == 0){
                highest = arr[row][x];
                continue;
            }
            else if(highest < arr[row][x]){
                highest = arr[row][x];
            }
        }
        return highest;
    }

    public static double getLowestInRow(double[][] arr, int row){
        double lowest = 0;
        for(int x = 0; x < arr[0].length; x++){
            if(x == 0){
                lowest = arr[row][x];
                continue;
            }
            else if(lowest > arr[row][x]){
                lowest = arr[row][x];
            }
        }
        return lowest;
    }
