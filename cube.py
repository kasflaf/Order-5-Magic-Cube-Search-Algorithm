import random as r
import obj as o

# cube
arr:int = [0]*125
for i in range(0,125) :
    arr[i]=i+1

def getCube() -> int:
    return arr

def CoorToIdx (x: int, y: int, z: int)->int :
    return (y-1)*5*5 + (z-1)*5 + (x-1)

def getRandomCube() -> int:
    r.shuffle(arr)
    return arr

def printArray(arr) : 
    for i in range(5) :
        for j in range((0+(i*25)),(i+1)*25) :
            if j!=0 and j%5==0 :
                print()
            print(str(arr[j]) + " ",end="")
            if arr[j]<10 :
                print(" ",end="")
            if arr[j]<100 :
                print(" ",end="")
        print()

def successor(arr,int1,int2) ->int :
    
    temp = arr[int1]
    arr[int1] = arr[int2]
    arr[int2] = temp
    return arr


def randomSuccessor (arr) -> int:
    a = r.randint(0,124)
    b = r.randint(0,124)
    if a==b :
        b=(b+2)//2
    successor(arr,a,b)
    return arr

def neighbor(arr) :
    #value that store the most relevant neighbor
    neighbor = any
    objNeighbor = -9999

    #value that will iterated
    successorTemp= [i for i in arr]

    # loop (7750 times)
    for i in range(0,124) :
        for j in range(i+1,125) :

            #test successor
            successorTemp = successor(successorTemp,i,j)

            #determine objective value of tempSucessor and neighbor candidate
            objSuccessorTemp = o.objective(successorTemp)

            # found better successor
            if objSuccessorTemp>= objNeighbor:
                neighbor = [i for i in successorTemp]
                objNeighbor = objSuccessorTemp
                
            successorTemp = successor(successorTemp,i,j)
    return neighbor
def sidewaysneighbor(arr):
    neighbor = any
    objNeighbor = -9999

    samearray = []

    for i in range(0, 124):
        for j in range(i + 1, 125):
            successorTemp = arr[:]
            successorTemp[i], successorTemp[j] = successorTemp[j], successorTemp[i]
            objSuccessorTemp = o.objective(successorTemp)

            if objSuccessorTemp > objNeighbor:
                neighbor = successorTemp[:]
                objNeighbor = objSuccessorTemp
                samearray.clear()
            elif objSuccessorTemp == objNeighbor:
                samearray.append(successorTemp[:])

    if objNeighbor == o.objective(arr) and samearray:
        neighbor = r.choice(samearray)

    return neighbor
