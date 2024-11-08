import obj as o
import cube as c
import time as t
import matplotlib.pyplot as plt

objectiveResult = []

def steepest(arr) :
    current = [i for i in arr]
    print("state awal:" ,end="")
    print(o.objective(current))
    j=1
    while True:
        neighbor = c.neighbor(current)
        neighborObjective = o.objective(neighbor)
        print("iterasi " + str(j) +": ",end="")
        print(neighborObjective)
        j+=1
        if neighborObjective<=o.objective(current) :
            print("state akhir:" ,end="")
            print(o.objective(current))
            return current
        current = neighbor

        objectiveResult.append(neighborObjective)
        

def main() :
    arr = c.getRandomCube()

    c.printArray(arr)

    start = t.time()
    arr = steepest(arr)
    end = t.time()

    c.printArray(arr)
    elapsed = end-start
    print("duration: " + str(elapsed))   

    plt.plot(range(1, len(objectiveResult) + 1), objectiveResult, marker='o')
    plt.xlabel("Iteration")
    plt.ylabel("Neighbor Objective")
    plt.title("Steepest Ascent")
    plt.show() 

    return 0
main()