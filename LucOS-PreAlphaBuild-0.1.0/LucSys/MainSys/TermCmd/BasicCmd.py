import os

#Echo's a string (repeats it)
def echo(str, *_):
    print(str)

#Shuts down the system
def shutdown(*_):
    print("Shutting down...")
    quit()

#clears the terminal
def clear(*_):
    os.system("cls")