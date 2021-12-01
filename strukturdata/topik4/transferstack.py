from linkedliststack import Stack

def transferStack(stackSumber, stackTujuan):
    # Tuliskan kode implementasi fungsi transferStack Anda di bawah!
    for i in range(0, len(stackSumber)):
        n = stackSumber
        stackTujuan.push(stackSumber.pop())
        