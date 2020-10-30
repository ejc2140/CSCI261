#HW 4 - Emily Crilley

#Question 1 
def max2(num1,num2):
    return (num1+num2+(abs(num1-num2)))/2

#Question 2 
def fSelect(lis, index):
    for i in range(0, index): 
        minInd = i 
        minValue = lis[i]
        for j in range(i+1, len(lis)):
            if minValue > lis[j]: 
                minInd = j 
                minValue = lis[j]
                lis[i], lis[minInd] = lis[minInd], lis[i]
    return lis[index] 

#Question 3 
def partition(a, l, h):
   x = a[h]
   i = l - 1
   j = l
   while j < h:
       if a[j] <= x:
           i += 1
           a[i], a[j] = a[j], a[i]
       j += 1
   a[i+1], a[h] = a[h], a[i+1]
   return i + 1 
 
def iSelectHelper(arr, index, l, h):
   if index >= 0 and index <= h - l + 1:
       i = partition(arr, l, h)
       if i - 1 == index:
           return arr[index]
       elif i - l > index:
           return iSelectHelper(arr, index, l, i-1)
       else:
           return iSelectHelper(arr, index - i + l, i + 1, h)
   else:
       return 0       

def iSelect(arr, index):
    return iSelect(arr, index, 0, len(arr) - 1) 