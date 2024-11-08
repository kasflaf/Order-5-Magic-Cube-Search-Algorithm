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
        objectiveResult.append(o.objective(neighbor))

def main() :
    arr = c.getRandomCube()
    numRestart = 0
    maxRestart = 5
    start=t.time()
    maxarr = arr

    while (o.objective(arr) < 0 and numRestart < maxRestart):
        print("Restart ke-" + str(numRestart+1))

        arr = c.getRandomCube()
        c.printArray(arr)
        arr = steepest(arr)
        c.printArray(arr)
        o.diagnostic(arr)
        if (o.objective(arr) >= o.objective(maxarr)): maxarr = [i for i in arr]
        numRestart += 1

    end=t.time()
    elapsed = end - start
    print("duration: " + str(elapsed))
    print("highest value:\n")
    c.printArray(maxarr)
    print("value: " + str(o.objective(maxarr)))
    o.diagnostic(maxarr)


    plt.plot(range(1, len(objectiveResult) + 1), objectiveResult, color='purple')

    plt.xlabel("Iteration")
    plt.ylabel("Neighbor Objective")
    plt.title("Random Restart")
    plt.ylim(min(objectiveResult) - 100 , 0)
    plt.show()
    return 0

main()