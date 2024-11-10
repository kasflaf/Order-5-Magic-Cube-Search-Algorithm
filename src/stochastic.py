import obj as o
import cube as c
import time as t
import matplotlib.pyplot as plt

objectiveResult = []


def stochastic(arr)->int :
        # copy content of arr
    current = [i for i in arr]

    neighbor = [i for i in arr]
    # output
    print("state awal:" ,end="")
    print(o.objective(current))

    for i in range(78000) :
        neighbor = c.randomSuccessor(neighbor)

        if  o.objective(neighbor) > o.objective(current): 
            current = [i for i in neighbor]

        neighbor= [i for i in current]

        print("iterasi " + str(i+1) +": ",end="")
        print(o.objective(current))
        objectiveResult.append(o.objective(current))

    return current


def main() :
    arr = c.getRandomCube()

    c.printArray(arr)

    start = t.time()

    arr = stochastic(arr)

    end = t.time()
    c.printArray(arr)

    elapsed = end-start

    print("duration: " + str(elapsed))  

    plt.plot(range(1, len(objectiveResult) + 1), objectiveResult, color='purple')
    plt.xlabel("Iteration")
    plt.ylabel("Neighbor Objective")
    plt.title("Stochastic")
    plt.ylim(min(objectiveResult) - 100 , 0)
    plt.show()   

    return 0
main()