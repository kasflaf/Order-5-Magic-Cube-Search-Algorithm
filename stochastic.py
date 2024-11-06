import obj as o
import cube as c

def stochastic(arr)->int :
        # copy content of arr
    current = [i for i in arr]

    neighbor = [i for i in arr]
    # output
    print("state awal:" ,end="")
    print(o.objective(current))

    for i in range(100000) :
        neighbor = c.randomSuccessor(neighbor)

        if  o.objective(neighbor) > o.objective(current): 
            current = [i for i in neighbor]

        neighbor= [i for i in current]

        print("iterasi " + str(i+1) +": ",end="")
        print(o.objective(current))

    return current


def main() :
    arr = c.getRandomCube()

    c.printArray(arr)

    arr = stochastic(arr)

    c.printArray(arr)

    return 0
main()