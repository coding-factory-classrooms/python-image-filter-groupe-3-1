import os
import sys

from function.inputcli_function import inputOutput, inputFilter, inputConfig
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
    for sleepLoop in range(0, len(cmdExcute)):
        inputCLI = cmdExcute[sleepLoop]
        inputCLIConfig = cmdExcute[1]
        if inputCLI == "-i":
            redirectory = cmdExcute[sleepLoop + 1]
        elif inputCLI == "-o":
            inputOutput(cmdExcute, sleepLoop)
        elif inputCLI == "-f":
            inputFilter(cmdExcute, sleepLoop)
        elif inputCLIConfig == "--config":
            inputConfig()
