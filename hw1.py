#Emily Crilley - CSCI 261 Assigment 1 
import time
#Question Five 
def fib(num):
    if num == 0: 
        return 0
    elif num == 1: 
        return 1 
    else: 
        return fib(num-1) + fib(num-2)

def fibItHelper(n, a, b):
    if n == 0: 
        return a
    elif n == 1: 
        return b 
    else: 
        return fibItHelper(n-1, b, a+b)
    
def fibIt(n):
    return fibItHelper(n, 0, 1)

def main(): 
    for i in range(1,500): 
        start = time.time()
        #fib(i)
        fibIt(i)
        end = time.time()
        print("Runtime for i = "+ str(i) + " is: " + str(end-start))

main()
