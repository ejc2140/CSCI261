"""
Emily Crilley
CSCI 261 - Homework 0
"""

"""
Question 3, reverse the order of a list 
"""
def r(x=[]):
    if not x:
        return x
    return x[-1:] + r(x[:-1])

"""Question 4"""
def prod(m,n):
    if m == 0:
        return
    else:
        return n + prod(m-1, n)

"""Question 5"""
def fastPow(b,k):
    if k == 0:
        return 1
    elif k == 1:
        return b
    else:
        return b * fastPow(b, k-1)

"""Question 6"""
def prodAccum(m,n,a):
    a = 0
    if m == 0:
        return a
    else:
        m = m -1
        return prodAccum(m,n,a+n)

"""Question 7"""
def min(a,b):   #gets minimum number and returns it, failure = none
    if a == None:
        return b
    elif b == None:
        return b
    elif a>b:
        return b
    else:
        return a

def add(a,b):   #adds numbers together, but modified to account for "failure"
    if a == None or b == None:
        return None
    else:
        return a+b

def minChange(a,ds):
    if a == 0:
        return 0
    elif ds == []:
        return None
    else:
        d = ds.pop(0)
        if(a<d):
            return minChange(a, ds)
        else:
            added = add(1, minChange(a-d, ds))
            return min(added,minChange(a, ds))

"""Question 8"""
def greedyMinChange(a,ds):
    if a == 0:
        return 0
    elif ds == []:
        return None
    else:
        d = ds.pop(0)
        if(a<d):
            return greedyMinChange(a, ds)
        else:
            div = a//d
            rem = a % d
            return add(div, greedyMinChange(rem, ds))

"""Question 9"""
def powIt(b,e):
    accum = 1
    if e == 0:
        return accum
    elif e == 1:
        return b
    else:
        accum = accum*b
        return powIt(b, e-1)
