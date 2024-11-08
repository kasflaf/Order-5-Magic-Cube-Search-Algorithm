import obj as o
import cube as c
import math as m
import random as r
import time as t
import matplotlib.pyplot as plt
import numpy as np 

objectiveResult = []
expResult = []

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
        if t <= 0.000000000000000000001  or o.objective(current)==0 : return current,stuck
        next = c.randomSuccessor(next)
        deltaE = o.objective(next) - o.objective(current)

        a = r.random()
        expValue = np.exp(deltaE / t)
        # expResult.append(expValue)

        if deltaE >= 0 : 
            current = [i for i in next]
            stuck=0
        elif  deltaE < 0 and a <= m.exp(deltaE/t) : 
            current = [i for i in next]
            stuck=0
            expResult.append(expValue)
        
        stuck+=1
        

        next = [i for i in current]

        print("iterasi " + str(j) +": ",end="")
        print(o.objective(current))
        objectiveResult.append(o.objective(current))

def schedule(a) :
    t=100000.0
    coolingRate = 0.9995
    T =  t * m.pow(coolingRate,a)
    return T


def main() :

    
    start=t.time()
    arr = c.getRandomCube()
    temp = arr

    arr,stuck = simulatedAnnealing(arr)

    print("\n\nstate awal: ")
    c.printArray(temp)
    print(f"State Awal: {o.objective(temp)}")

    print("\n\nstate akhir: ")
    c.printArray(arr)
    print(f"State Akhir: {o.objective(arr)}")

    end = t.time()
    print("stuck: ",end="")
    print(stuck)
    elapsed = end - start
    
    print("duration: " + str(elapsed))
    
    plt.plot(range(1, len(objectiveResult) + 1), objectiveResult, color='purple')
    plt.xlabel("Iteration")
    plt.ylabel("Neighbor Objective")
    plt.title("Simulated Annealing")
    plt.ylim(min(objectiveResult) - 100 , 0)
    plt.show()  

    plt.plot(range(1, len(expResult) + 1), expResult, color='blue')
    plt.xlabel("Iteration")
    plt.ylabel("e^(ΔE/T)")
    plt.title("Simulated Annealing - e^(ΔE/T) Over Iterations")
    plt.show()
    return 0
main()