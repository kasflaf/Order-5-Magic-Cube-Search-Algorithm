import obj as o
import cube as c
import random
import time as t

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
        print("cube: \n")
        c.printArray(population[i])
        print()
        print (f"objective function: {o.objective(population[i])}\n\n")

def generatePopulation(population: int):
    populationInit = [0]*population

    for i in range (0, population):
        populationInit[i] = c.getRandomCube()

    return populationInit


def genetic(population, arr, iterationCount ):
    iterationCount[:] = [iterationCount[0] + 1]

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

    #invert stateVal
    for i in range (0, population):
        stateVal[i] = 2522 + stateVal[i]

    # #check
    # print("state val: ")
    # print(stateVal)

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
                for k in range (0,population):
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
        chance = 0.3  # 50% chance
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

    #iteration tracker
    print(f"iterasi ke-{iterationCount[0]}")
    print("Objective Function: ")
    print(stateVal)
    print(f"Max: {max(stateVal)}")
    print(f"Avg: {sum(stateVal)/len(stateVal)}\n")

    newStateVal = [0]*population
    for i in range (0, population):
        newStateVal[i] = o.objective(populationNew[i])
    #invert stateVal
    for i in range (0, population):
        newStateVal[i] = 2522 + newStateVal[i]
    
    # if (sum(stateVal)/len(stateVal)) > (sum(newStateVal)/len(stateVal)):
    #     return populationInit
    # else:
    #     chancepop = 0.2 #20%
    #     if random.random() < chance:
    #         return populationInit
    #     else:
    #         return populationNew

    # if (sum(stateVal)/len(stateVal)) > (sum(newStateVal)/len(newStateVal)):
    if (max(stateVal)) > (max(newStateVal)):
        return populationInit
    else:
        return populationNew

    # return populationNew



def main():
    population: int = 10
    iteration: int = 300000
    itercount = [0]
    start_time = t.time()

    #state awal
    result = generatePopulation(population)
    temp = result

    result = genetic(population, result, itercount)

    #iterasi
    for i in range(0, iteration-1):
        result = genetic(population, result, itercount)

    #state awal print
    print("state awal: ")
    visualizePopulation(temp)

    #state akhir
    end_time = t.time()
    print("\n\nstate akhir: ")
    visualizePopulation(result)
    print(f"Duration: {end_time - start_time}")


    return


main()
    
            

