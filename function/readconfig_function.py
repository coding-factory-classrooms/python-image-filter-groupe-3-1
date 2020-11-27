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

def checkErrorConfig(saveResultat):
    separeFilter = saveResultat[0].split(" ")
    for loopFilter in range(0, len(separeFilter)):
        if not separeFilter[loopFilter] == "grey":
            separeFilterDoubleParam = separeFilter[loopFilter].split(':')
            finalFilter = separeFilterDoubleParam[0]
            finalParamFilter = separeFilterDoubleParam[1]
            print(finalFilter + finalParamFilter)
        else:
            finalFilter = "grey"
            finalParamFilter = 0

def checkErrorCli(saveResultat):
    separeFilter = saveResultat[0].split(" ")
    for loopFilter in range(0, len(separeFilter)):
        if not separeFilter[loopFilter] == "grey":
            separeFilterDoubleParam = separeFilter[loopFilter].split(':')
            finalFilter = separeFilterDoubleParam[0]
            finalParamFilter = separeFilterDoubleParam[1]
            print(finalFilter + finalParamFilter)
        else:
            finalFilter = "grey"
            finalParamFilter = 0

def getResultat():
    return resultatVar


def readConfig():
    conf = configparser.ConfigParser()
    conf.read('config2.ini')
    redirectory = conf['config']['redirectoryInputImage']