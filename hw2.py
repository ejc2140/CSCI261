#Emily Crilley - CSCI 261 Assigment 2 Project 
class L: 
    def __init__(self, a, b):
        self.a = a
        self.b = b 

def fibPow(n):
    x = L(0,1) 
    y = Pow(x,n)

    return y.b 

def Pow(k, n): 
    length = range(n)
    for i in length: 
        sum = k.a + k.b 
        k.a = k.b 
        k.b = sum 
    return k 

def main(): 
    for i in range(0,100): 
        print(fibPow(i))

main()