from CheckCmd import checkCmd

from TermCmd.BasicCmd import *
from TermCmd.SysAppCmd import *

while True:
    thing = input("> ")

    thing = thing.split(" ")

    cmd, cmdAttributes = checkCmd(thing[0])

    if cmd == "PrintNotACommand":
        print("That is not a recognised command!")
        continue

    if cmdAttributes != (len(thing) - 1):
        print("This function takes " + str(cmdAttributes) + " attributes, you gave " + str(len(thing) - 1))
        continue

    while len(thing) != 11:
        thing.append("Nan")
    
    if cmd:
        if len(thing) == 1:
            cmd()
        else:
            cmd(thing[1], thing[2], thing[3], thing[4], thing[5], thing[6], thing[7], thing[8], thing[9], thing[10])