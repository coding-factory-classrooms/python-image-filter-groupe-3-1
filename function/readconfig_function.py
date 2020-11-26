def readConfigFunction():
    resultatVar = []

    finalVar = open("config.ini","r")
    finalVar = finalVar.read()
    finalVar = finalVar.split("\n")

    print(finalVar)

    for sleepLoop in range(0,1):
        finalVar = finalVar[sleepLoop].split("=")
        finalVar = finalVar[1]
        resultatVar.insert(0, finalVar)

    print(resultatVar)
