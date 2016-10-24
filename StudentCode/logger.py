from datetime import datetime as dt

newline = "\n"

def log(*messages):
    text = ""
    for m in messages: text += "%s\t" % m
    print (text)
    with open(__file__+".log", 'a') as logfile:
        logfile.write("%.19s:\t%s\n" % (dt.now(), text))

