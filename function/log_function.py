import os
from datetime import datetime

if not os.path.exists('log'):
    os.mkdir('log')

globalLog = 'log/log_applications.log'


def logFunction(message):
    timeNow = datetime.now()
    timeStamp = timeNow.strftime('%Y/%m/%d %H:%M:%S')
    resultatMessage = f'{timeStamp} - {message}'

    with open(globalLog, 'a') as f:
        f.write(resultatMessage + '\n')

def dump_log():
    with open(globalLog, 'r') as f:
        print(f.read())