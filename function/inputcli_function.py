import os

from function.createimg_function import createImgFunction
from function.readconfig_function import getResultat
from function.selection_function import selectionFunction

def inputOutput(cmdExcute, sleepLoop):
    if sleepLoop + 1 < len(cmdExcute):
        output = cmdExcute[sleepLoop + 1]
        if not os.path.exists(output):
            os.mkdir(output)
        createImgFunction()
def inputFilter(cmdExcute, sleepLoop):
    redirectory = cmdExcute[2]
    output = cmdExcute[4]
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
def inputConfig():
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
        selectionFunction(redirectory, output, finalFilter, finalParamFilter)

