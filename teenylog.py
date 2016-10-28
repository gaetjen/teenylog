#!/usr/bin/python3
# I miss my family! I miss my laptop! I masturbated to an extra curvy piece of driftwood the other day!
# make file executable, execute with a filename as argument, when stuff happens, write it down and press enter
import sys
import datetime

if len(sys.argv) < 2:
    print("Provide file name!")
else:
    f = sys.argv[1]
    print("Now writing to", f)
    with open(f, "a") as logfile:
        for line in sys.stdin:
            if line[0:2] == ":q":
                print("quit")
                break
            else:
                logfile.write(datetime.datetime.now().strftime("%d.%m.%Y %H:%M: ")+line)
