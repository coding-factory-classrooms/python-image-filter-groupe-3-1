import sys
import os


from function.readconfig_function import readConfigFunction,getResultat,readConfig
from function.cli_function import callFunction
finalVar = []
readConfigFunction()
getResultat()


callFunction()

