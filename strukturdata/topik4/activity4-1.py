from linkedliststack import Stack

def transferStack(stackSumber, stackTujuan):
    # Tuliskan kode implementasi fungsi transferStack Anda di bawah!
    for i in range(len(stackSumber)):
        stackTujuan.push(stackSumber.peek()) 
        stackSumber.pop()
        
    
