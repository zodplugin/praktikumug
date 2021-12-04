from linkedliststack import Stack

# Fungsi precendence menerima string (karakter) operator
# dan mengembalikan level precedence dari operator tersebut.
def precedence(operator):
    if (operator == '*' or operator == '/'):
        return 2
    elif (operator == '+' or operator == '-'):
        return 1

# Fungsi infix_to_postfix menerima string berupa ekspresi aritmatika
# dalam notasi infix, dan mengembalikan sebuah string berupa ekspresi
# aritmatika dalam notasi postfix yang ekuivalen dengan argument.
def infix_to_postfix(infix):
    opStack = Stack()
    postfix = ''
    operand = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Scan karakter per karakter dari string infix
    for token in infix:
        # Kasus 1: Jika token adalah operand (A s.d Z), konkatenasi ke akhir postfix.
        if token in operand:
            postfix += token
        # Kasus 2: Jika token sama dengan '(', push ke opStack.
        elif token == "(":
            opStack.push(token)
        # Kasus 3: Jika token sama dengan ')', selama opStack tidak kosong dan top tidak sama dengan '(',
        # pop isi opStack dan konkatenasi ke string postfix.
        # Lalu, pop '(' dari stack.
        elif token == ")":
            while not opStack.isEmpty() and opStack.peek() != "(":
                postfix += opStack.pop()
            opStack.pop()

        # Kasus 4: Jika token adalah operator, selama stack tidak kosong
        # dan top dari opStack tidak sama dengan `(` dan precedence top >= precendence token,
        # pop operator pada opStack dan konkatenasi ke akhir string postfix.
        # Lalu, push token ke stack.
        elif precedence(token) == 1 or precedence(token) == 2:
            while not opStack.isEmpty() and opStack.peek() != "(" and precedence(opStack.peek()) >= precedence(token) :
                postfix += opStack.pop()
            opStack.push(token)

    # Pop semua yang tersisa dalam stack dan konkatenasi ke akhir string postfix.
    while not opStack.isEmpty():
        postfix += opStack.pop()

    # Kembalikan string postfix.
    return postfix
