#ALOG Homework 3 - Emily Crilley
#Question 1
import math
def search(a,v,l,h): 
    m = l + math.floor((h-l)/2)
    while h >= l: 
        if v == a[m]:
            return True
        elif v < a[m]:
            return search(a,v,l,m-1)
        else:
            return search(a,v, m+1, h)
    return False
    
#Question 5
def sortedHasSum(S,x):
    low = 0
    high = len(S)-1

    while True:
        if low > high:
            return False
        sum = S[low] + S[high]
        if sum == x:
            return True
        elif sum > x:
            high -= 1
        else:
            low += 1    
   
def hasSum(S,x):
    S.sort()
    low = 0 
    high = len(S) - 1 

    while high > low:
        if S[high] + S[low] == x: 
            return True
        elif S[high] + S[low] > x: 
            high = high-1
        else: 
            low = low+1
    return False

#Question 6
def quick_sort(L):
   if L == []:
       return []
   else:
       pivot = L[0]
       (less, same, more) = partition(pivot, L)
       return quick_sort(less) + same + quick_sort(more)
 
def partition(pivot, L):
   (less, same, more) = ([], [], [])
   for e in L:
       if e < pivot:
           less.append(e)
       elif e > pivot:
           more.append(e)
       else:
           same.append(e)
   return (less, same, more)