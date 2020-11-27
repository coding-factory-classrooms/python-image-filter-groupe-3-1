import os
import sys
from function.selection_function import selectionFunction
from function.createimg_function import createImgFunction
from function.readconfig_function import getResultat, checkErrorCli, checkErrorConfig

finalFilter = ""
finalParamFilter = ""

def callCheckError():
    cmdExcute = sys.argv
    saveResultat = getResultat()
    if cmdExcute[1] == '--config':
        checkErrorConfig(saveResultat)
    else:
        checkErrorCli(cmdExcute)


def callCli(saveResultat):
    cmdExcute = sys.argv
    global finalFilter
    global finalParamFilter

    for sleepLoop in range(0, len(cmdExcute)):
        inputCLI = cmdExcute[sleepLoop]
        inputCLIConfig = cmdExcute[1]

        if inputCLI == "-i":
            redirectory = cmdExcute[sleepLoop + 1]
        elif inputCLI == "-o":
            if sleepLoop + 1 < len(cmdExcute):
                output = cmdExcute[sleepLoop + 1]
                if not os.path.exists(output):
                    os.mkdir(output)
                createImgFunction()

        elif inputCLI == "-f":
            if sleepLoop + 1 < len(cmdExcute):
                filter = cmdExcute[sleepLoop + 1]
                if not filter == "grey":
                    paramFilter = filter.split(':')
                    finalFilter = paramFilter[0]
                    finalParamFilter = paramFilter[1]
                else:
                    finalFilter = "grey"
                    finalParamFilter = 0
                selectionFunction(redirectory, output, finalFilter, finalParamFilter)

            if sleepLoop + 2 < len(cmdExcute):
                filter2 = cmdExcute[sleepLoop + 2]
                if not filter2 == "grey":
                    paramFilter = filter2.split(':')
                    finalFilter = paramFilter[0]
                    finalParamFilter = paramFilter[1]
                else:
                    finalFilter = "grey"
                    finalParamFilter = 0
                selectionFunction(redirectory, output, finalFilter, finalParamFilter)

                if sleepLoop + 3 < len(cmdExcute):
                    filter3 = cmdExcute[sleepLoop + 3]
                    if not filter3 == "grey":
                        paramFilter = filter3.split(':')
                        finalFilter = paramFilter[0]
                        finalParamFilter = paramFilter[1]
                    else:
                        finalFilter = "grey"
                        finalParamFilter = 0
                    selectionFunction(redirectory, output, finalFilter, finalParamFilter)
        elif inputCLIConfig == "--config":
            saveResultat = getResultat()
            redirectory = saveResultat[2]
            output = saveResultat[1]

            if not os.path.exists(output):
                os.mkdir(output)
            createImgFunction()

            paramResultatConfig = saveResultat[0].split(' ')

            for loopFilter in range(0, len(paramResultatConfig)):
                if not paramResultatConfig[loopFilter] == "grey":
                    paramResultatConfigFinal = paramResultatConfig[loopFilter].split(':')

                    finalFilter = paramResultatConfigFinal[0]
                    finalParamFilter = paramResultatConfigFinal[1]
                else:
                    finalFilter = "grey"
                    finalParamFilter = 0
                print(redirectory, output, finalFilter, finalParamFilter)
                selectionFunction(redirectory, output, finalFilter, finalParamFilter)
