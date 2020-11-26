import sys
import os


from function.selection_function import selectionFunction, displayAllFilter
from function.log_function import dump_log
from function.createimg_function import createImgFunction
from function.readconfig_function import readConfigFunction,getResultat

readConfigFunction()
print(getResultat())
cmdExcute = sys.argv
for sleepLoop in range(0, len(cmdExcute)):
    inputCLI = cmdExcute[sleepLoop]

    if inputCLI == "-i":
        redirectory = cmdExcute[sleepLoop + 1]
    elif inputCLI == "-o":
        if sleepLoop + 1 < len(cmdExcute):
            output = cmdExcute[sleepLoop + 1]
            if not os.path.exists(output):
                os.mkdir(output)
            createImgFunction()
        else:
            print('test')
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


        else:
            print('test')


configResult=getResultat()
config
selectionFunction(configResult[2],configResult[1],configResult[0])

#dump_log()
#displayAllFilter()
