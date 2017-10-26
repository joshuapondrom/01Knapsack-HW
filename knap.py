from random import randint
import numpy as np

def Knapsack(weightcap, weights, values, n):
    #Initializes our List with 0's when at 0 weight
    V = [[0 for x in range(weightcap+1)] for x in range(n+1)]
    print(np.matrix(V))
    #Main loop to find what will be in the knapsack
    for i in range(n+1):
        for j  in range(weightcap+1):
            #If we are at weight at zero
            if i == 0 or j == 0:
                V[i][j] = 0
            #If we have room for the weight, we will take the max
            # of either having that weight or having the other
            # elements that will fit ( the array index above it )
            elif weights[i-1] <= j:
                V[i][j] = max(values[i-1] + V[i-1][j-weights[i-1]],
                              V[i-1][j])
            #If it will not fit, it will be equal to the previously
            # calculated max with not having the current item
            else:
                V[i][j] = V[i-1][j]
    print(np.matrix(V))
    return V[n][weightcap]

def KnapsackGreedy(weightcap, weights, values, n):
    V = zip(weights, values)
    V = sorted(V)
    print(V)
    #Invariant to check that our list is sorted by weight ascending
    assert(V == sorted(zip(weights, values)))
    currentweight = 0
    currentvalue = 0
    currentitem = 0
    for item in V:
        if(item[0] + currentweight > weightcap):
            #Invariant to make sure the item can not fit
            assert(weightcap > item[0])
            break
        else:
            currentweight = currentweight + item[0]
            currentvalue = currentvalue + item[1]
            #Invariant to check that the item is added
            assert(currentweight > 0 and currentvalue > 0)
            currentitem = currentitem + 1
    print(currentitem)
    print(V[:currentitem])
    return currentvalue

a,b = 1, 50

def fillarray(array):
    return[randint(a,b) for i in range(len(array))]

value = fillarray([0]*5)
weight = fillarray([0]*5)
total = 250
n = len(value)
print(Knapsack(total, weight, value, n))
