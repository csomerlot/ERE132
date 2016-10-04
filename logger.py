from datetime import datetime as dt

def log(message):
    print (message)
    with open(__file__+".log", 'a') as logfile:
        logfile.write("%s: %s" % (dt.now(), message))

