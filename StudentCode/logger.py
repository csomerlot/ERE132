from datetime import datetime as dt

newline = "\n"

def log(message):
    print (message)
    with open(__file__+".log", 'a') as logfile:
        logfile.write("\t%s\t%s" % (dt.now(), message))

