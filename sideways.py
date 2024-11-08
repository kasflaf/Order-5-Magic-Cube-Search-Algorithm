import obj as o
import cube as c
import time as t
import matplotlib.pyplot as plt

objectiveResult = []

def sideways(arr) :
    current = [i for i in arr]
    print("state awal:" ,end="")
    print(o.objective(current))
    j=1
    countsidestep = 0
    while True:
        neighbor = c.sidewaysneighbor(current)
        neighborObjective = o.objective(neighbor)
        print("iterasi " + str(j) +": ",end="")
        print(neighborObjective)
        j+=1
        if neighborObjective<o.objective(current) or countsidestep==50 :

            print("state akhir:" ,end="")
            print(o.objective(current))
            return current

        if neighborObjective == o.objective(current) :
            countsidestep+=1
        else :
            countsidestep = 0

        current = neighbor
        objectiveResult.append(o.objective(neighbor))

def main() :
    arr = c.getRandomCube()

    c.printArray(arr)

    start = t.time()
    arr = sideways(arr)
    end = t.time()

    c.printArray(arr)
    elapsed = end - start
    print("duration: " + str(elapsed))

    plt.plot(range(1, len(objectiveResult) + 1), objectiveResult, color='purple')
    plt.xlabel("Iteration")
    plt.ylabel("Neighbor Objective")
    plt.title("HC with Sideways Move")
    plt.ylim(min(objectiveResult) - 100 , 0)
    plt.show()

    return 0
main()