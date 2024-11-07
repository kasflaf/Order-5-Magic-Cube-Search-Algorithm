import obj as o
import cube as c
import random

#check duplicate, true if duplicate
def isDuplicate(arr, num: int) -> bool:
    dupe = False
    for i in range(0, len(arr)):
        if arr[i] == num :
            dupe = True
            break
    return dupe

def visualizePopulation(population):
    for i in range(len(population)):
        c.printArray(population[i])
        print (o.objective(population[i]))
        o.diagnostic(population[i])

def generatePopulation(population: int):
    populationInit = [0]*population

    for i in range (0, population):
        populationInit[i] = c.getRandomCube()

    return populationInit


def genetic(population, arr):
    population:int = 10
    populationInit = arr
    stateVal = [0]*population
    fitnessVal = [0]*population

    #count state Val
    for i in range (0, population):
        stateVal[i] = o.objective(populationInit[i])

    # #check
    # print("test population count and stateval: ")
    # print(len(populationInit))
    # print(stateVal)
    # c.printArray(populationInit[2])
    # c.printArray(populationInit[9])

    #assign fitnessVal
    for i in range (0, population):
        fitnessVal[i] = (stateVal[i]/sum(stateVal))*100

    #check
    # print("test fitness: ")
    # print(fitnessVal)

    #start loop
    populationNew = [0]*population
    for l in range (0, population):
        #pick parrent
        parrIdx = [0]*2
        for i in range (0, population):
            for j in range (0,2):
                random_number = random.randint(1, 100)
                temp = 0
                for k in range (0,10):
                    temp += fitnessVal[k] 
                    if random_number <= temp:
                        parrIdx[j] = k
                        break
        #check
        # print("test parrent idx: ")
        # print(parrIdx)

        #cross-over
        if stateVal[parrIdx[0]] >= stateVal [parrIdx[1]]:
            temp = populationInit[parrIdx[0]][0:63] + [-1]*(125-63) #partisi 1
            for i in range (63, 125): #partisi 2 non duplicate
                if not isDuplicate(temp, populationInit[parrIdx[1]][i]):
                    temp[i] = populationInit[parrIdx[1]][i]
            

            #fill duplicate
            for i in range (63, 125):
                if temp[i] == -1:
                    for j in range (0, 63):
                        if not isDuplicate(temp, populationInit[parrIdx[1]][j]):
                            temp[i] = populationInit[parrIdx[1]][j]
                            break
        else:
            temp = populationInit[parrIdx[1]][0:63] + [-1]*(125-63) #partisi 1
            for i in range (63, 125): #partisi 2 non duplicate
                if not isDuplicate(temp, populationInit[parrIdx[0]][i]):
                    temp[i] = populationInit[parrIdx[0]][i]
            
            #fill duplicate
            for i in range (63, 125):
                if temp[i] == -1:
                    for j in range (0, 63):
                        if not isDuplicate(temp, populationInit[parrIdx[0]][j]):
                            temp[i] = populationInit[parrIdx[0]][j]
                            break

        #check
        # print("test child: ")
        # c.printArray(temp)

        #mutasi
        chance = 0.5  # 10% chance
        # Check if the event occurs
        if random.random() < chance:
            idx1 = random.randint(0,124)
            idx2 = random.randint(0,124)

            # #check
            # print(temp[idx1])
            # print(temp[idx2])

            tempVal = temp[idx1]
            temp[idx1] = temp[idx2]
            temp[idx2] = tempVal

            # #check
            # print(temp[idx1])
            # print(temp[idx2])


        populationNew[l] = temp
        
        # #check
        # print("test new populaiton: ")
        # c.printArray(populationNew[l])

    return populationNew



def main():
    population: int = 10
    iteration: int = 5

    result = generatePopulation(population)
    result = genetic(population, result)
    # visualizePopulation(result)
    return


main()
    
            

