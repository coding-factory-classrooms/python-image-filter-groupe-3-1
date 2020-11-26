resultatVar = []


def readConfigFunction():
    global resultatVar
    finalVar = open("config.ini","r")
    finalVar = finalVar.read()
    finalVar = finalVar.split("\n")
    for sleepLoop in range(0,3):
        filterTemp = finalVar[sleepLoop].split("=")
        filterWanted = filterTemp[1]
        resultatVar.insert(0, filterWanted)
    return resultatVar

def getResultat():
    return resultatVar
