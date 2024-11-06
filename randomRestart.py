import obj as o
import cube as c

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

def main() :
    arr = c.getRandomCube()
    

    while (o.objective(arr) < 0):
        arr = c.getRandomCube()

        c.printArray(arr)

        arr = steepest(arr)

        c.printArray(arr)

        o.diagnostic(arr)

    return 0

main()