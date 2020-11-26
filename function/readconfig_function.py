def readConfigFunction():
    finalVar = open("config.ini","r")
    finalVar = finalVar.read()
    finalVar = finalVar.endswith("=")
    print(finalVar)
