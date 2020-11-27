import configparser
import os
import sys

import function.cli_function
from function.selection_function import displayAllFilter

resultatVar = []
finalResultatVar = []


def readConfigFunction():
    global filterWanted
    try:
        cmdExcute = sys.argv
        finalVar = open(cmdExcute[2], "r")
        finalVar = finalVar.read()
        finalVar = finalVar.split("\n")
        for sleepLoop in range(0, 3):
            filterTemp = finalVar[sleepLoop].split("=")
            filterWanted = filterTemp[1]
            resultatVar.insert(0, filterWanted)
    except:
        print("Votre configuration n'existe pas.")


def checkErrorConfig(saveResultat):
    separeFilter = saveResultat[0].split(" ")
    if 'grey' in separeFilter:
        separeFilter = separeFilter
    else:
        paramResultatConfigFinal = separeFilter[0].split(':')
    if not os.path.exists(saveResultat[2]):  # check if input document possible create
        os.mkdir(saveResultat[2])
    if not os.path.exists(saveResultat[1]):  # check if output document possible create
        os.mkdir(saveResultat[1])
    try:
        if 'grey' in separeFilter or \
                'blur' in paramResultatConfigFinal[0] and paramResultatConfigFinal[1].isdigit() or \
                'dilate' in paramResultatConfigFinal[0] and paramResultatConfigFinal[1].isdigit():
            function.cli_function.callCli()
        else:
            print("\nVous n'utilisez pas les filtres disponible")
            displayAllFilter()
    except IndexError:
        print("\nVous n'utilisez pas les filtres disponible")
        displayAllFilter()




def checkErrorCli(saveResultat):
    separeFilter = saveResultat[6].split(" ")
    if not os.path.exists(saveResultat[2]):  # check if input document possible create
        os.mkdir(saveResultat[2])
    if not os.path.exists(saveResultat[4]):  # check if output document possible create
        os.mkdir(saveResultat[4])

    if 'grey' in separeFilter:
        separeFilter = separeFilter
    else:
        paramResultatConfigFinal = separeFilter[0].split(':')
    try:
        if 'grey' in separeFilter or \
                'blur' in paramResultatConfigFinal[0] and paramResultatConfigFinal[1].isdigit() or \
                'dilate' in paramResultatConfigFinal[0] and paramResultatConfigFinal[1].isdigit():
            function.cli_function.callCli()
        else:
            print("\nVous n'utilisez pas les filtres disponible")
            displayAllFilter()
    except IndexError:
        print("\nVous n'utilisez pas les filtres disponible")
        displayAllFilter()


def getResultat():
    return resultatVar


def readConfig():
    conf = configparser.ConfigParser()
    conf.read('config2.ini')
    redirectory = conf['config']['redirectoryInputImage']
