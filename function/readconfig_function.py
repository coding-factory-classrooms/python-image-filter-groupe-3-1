import configparser

resultatVar = []
finalResultatVar = []


def readConfigFunction():
    global filterWanted
    finalVar = open("config.ini","r")
    finalVar = finalVar.read()
    finalVar = finalVar.split("\n")
    for sleepLoop in range(0,3):
        filterTemp = finalVar[sleepLoop].split("=")
        filterWanted = filterTemp[1]
        resultatVar.insert(0, filterWanted)

def getResultat():
    print(resultatVar)
    return resultatVar


def readConfig():
    conf = configparser.ConfigParser()
    conf.read('config2.ini')
    redirectory = conf['config']['redirectoryInputImage']
    print(redirectory)