import obj as o
import function as f


def sideways(arr) :
    current = [i for i in arr]
    print("state awal:" ,end="")
    print(o.objective(current))
    j=1
    countsidestep = 0
    while True:
        neighbor = f.neighbor(current)
        neighborObjective = o.objective(neighbor)
        print("iterasi " + str(j) +": ",end="")
        print(neighborObjective)
        j+=1
        if neighborObjective==current :
            countsidestep+=1
        if neighborObjective<o.objective(current) or countsidestep==50 :

            print("state akhir:" ,end="")
            print(o.objective(current))
            return current
        current = neighbor
