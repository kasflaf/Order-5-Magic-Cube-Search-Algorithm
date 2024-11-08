import obj as o
import cube as c
import time as t
import matplotlib.pyplot as plt


def steepest(arr) :
    current = [i for i in arr]
    objectiveResult= [] 
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
            objectiveResult.append(o.objective(neighbor))
            print("state akhir:" ,end="")
            print(o.objective(current))
            return current, objectiveResult
        current = neighbor

def main() :
    arr = c.getRandomCube()
    numRestart = 0
    maxRestart = 5
    start=t.time()
    maxarr = arr
    all_objectiveResult = []

    while (o.objective(arr) < 0 and numRestart <= maxRestart):
        print("Restart ke-" + str(numRestart+1))

        arr = c.getRandomCube()
        c.printArray(arr)
        arr = steepest(arr)
        c.printArray(arr)
        o.diagnostic(arr)
        if (o.objective(arr) >= o.objective(maxarr)): maxarr = arr
        numRestart += 1
        all_objectiveResult.append(objectiveResult)

    end=t.time()
    elapsed = end - start
    print("duration: " + str(elapsed))
    print("highest value:\n")
    c.printArray(maxarr)
    print("value: " + str(o.objective(maxarr)))
    o.diagnostic(maxarr)

    for objectiveResult in all_objectiveResult:
        plt.plot(range(1, len(objectiveResult) + 1), objectiveResult, color='purple')

    plt.xlabel("Iteration")
    plt.ylabel("Neighbor Objective")
    plt.title("Random Restart")
    plt.ylim(min(min(all_objective_values)) - 100, 0) 
    plt.show()
    return 0

main()