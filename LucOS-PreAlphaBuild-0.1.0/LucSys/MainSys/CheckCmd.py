#Imports all terminal commands
from TermCmd.BasicCmd import *
from TermCmd.SysAppCmd import *

#The list and lexicon used to identify terminal commands
CmdAttributes = {"echo": 1, "shutdown": 0, "clear": 0, "calculator": 0}
CmdLexicon = {"echo": echo, "shutdown": shutdown, "clear": clear, "calculator": calculator}
cmdList = ["echo", "shutdown", "clear", "calculator"]

#Checks if the inputted command exists and returns it if so
def checkCmd(cmdStr):
    if cmdStr in cmdList:

        #Returns the command name
        return CmdLexicon[cmdStr], CmdAttributes[cmdStr]
    
    else:
        
        if cmdStr == "":
            return CmdLexicon["echo"], CmdAttributes["echo"]
        #Prints that the command does not exist if the command is not in the list and lexicon
        else:
            return "PrintNotACommand", "PrintNotACommand"