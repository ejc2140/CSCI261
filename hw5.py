#Homework 5 - Emily Crilley 

#Question 3 
def fibDyn(n):
    a = []
    if n < 2:
        a[n] = n
        return n

    if n-2 in a:
        f2 = a[n-2]
    else:
        a[n-2] = fibDyn(n-2)
        f2 = a[n-2]

    if n-1 in a:
        f1 = a[n-1]
        return f1 + f2
    else:
        a[n-1] = fibDyn(n-1)
        f1 = a[n-1]
        return f1+f2

#Question 4b 
def knapsack(I, W):
    n = len(I)
    c = [[0 for x in range(W)] for y in range(n)]
    for i in range(0, n):
        for w in range(1, W):
            if I[i][1] <= w:
                cc = c[i-1][w]
                tmp = I[i][0] + c[i-1][w-I[i][1]]
                if tmp > cc:
                    cc = tmp
                c[i][w] = cc
    return c[n-1][W-1]

#Question 4c
def knapsackContents(I, W):
    iLen = len(I)
    c = [[0 for x in range(W)] for y in range(iLen)] 
    ks = []
    for i in range(0, iLen):
        for w in range(1, W):
            if I[i][1] <= w:
                champ = c[i - 1][w]
                temp = I[i][0] + c[i - 1][w - I[i][1]]
                if temp > champ:
                    champ = temp
                c[i][w] = champ
    for i in range(1, iLen):
        if c[i][W-1] != 0:
            ks.append(I[i])
    return c[iLen - 1][W - 1], ks