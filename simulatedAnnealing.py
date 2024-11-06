import obj as o
import cube as c
import math as m
import random as r
import time as t

def simulatedAnnealing(arr) :

    # copy content of arr
    current = [i for i in arr]

    next = [i for i in arr]
    # output
    print("state awal:" ,end="")
    print(o.objective(current))

    # temperature
    j=0
    stuck = 0
    while True:
        j+=1
        t = schedule(j)
        if t <= 0.0000000001  or o.objective(current)==0: return current,stuck
        next = c.randomSuccessor(next)
        deltaE = o.objective(next) - o.objective(current)

        if deltaE > 0 : 
            current = [i for i in next]
            stuck=0

        elif  deltaE <= 0 and r.random() <= m.exp(deltaE/t) : 
            current = [i for i in next]
            stuck=0
        
        stuck+=1

        next = [i for i in current]

        print("iterasi " + str(j) +": ",end="")
        print(o.objective(current))

def schedule(a) :
    t=100000.0
    coolingRate = 0.9995
    T =  t * m.pow(coolingRate,a)
    return T


def main() :

    
    start=t.time()
    arr = c.getRandomCube()

    c.printArray(arr)

    arr,stuck = simulatedAnnealing(arr)

    c.printArray(arr)

    end = t.time()
    print("stuck: ",end="")
    print(stuck)
    elapsed = end - start
    
    print("duration: " + str(elapsed))

    return 0
main()