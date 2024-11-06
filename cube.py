import random as r
# import function as f
# import time as t
# import numpy as np
# import steepest as st
import obj as o
# import sideways as sid

# cube
arr:int = [0]*125
for i in range(0,125) :
    arr[i]=i+1

def getCube() :
    return arr

def CoorToIdx (x: int, y: int, z: int)->int :
    return (y-1)*5*5 + (z-1)*5 + (x-1)

def getRandomCube() :
    r.shuffle(arr)
    return arr

def printArray(arr) : 
    for i in range(5) :
        for j in range((0+(i*25)),(i+1)*25) :
            if j!=0 and j%5==0 :
                print()
            print(str(arr[j]) + " ",end="")
            if arr[j]<10 :
                print(" ",end="")
            if arr[j]<100 :
                print(" ",end="")
        print()

def successor(arr,int1,int2) :
    
    temp = arr[int1]
    arr[int1] = arr[int2]
    arr[int2] = temp
    return arr

def neighbor(arr) :
    #value that store the most relevant neighbor
    neighbor = [i for i in arr]

    #value that will iterated
    successorTemp= [i for i in arr]

    # neighbor must be successor of current, for first value 
    # that have same objective value as current
    firstChange = True

    # loop (7750 times)
    for i in range(0,124) :
        for j in range(i+1,125) :

            #test successor
            successorTemp = successor(successorTemp,i,j)
            #determine objective value of tempSucessor and neighbor candidate
            objSuccessorTemp = o.objective(successorTemp)
            objNeighbor = o.objective(neighbor)

            # found better successor
            if objSuccessorTemp> objNeighbor:
                firstChange==False
                neighbor = successor(neighbor,i,j)
                
            # first successor that have similar value
            # elif objSuccessorTemp==objNeighbor and firstChange==True  :
            #     firstChange = False
            #     neighbor = successor(neighbor,i,j)
                
            successorTemp = successor(successorTemp,i,j)
    return neighbor

