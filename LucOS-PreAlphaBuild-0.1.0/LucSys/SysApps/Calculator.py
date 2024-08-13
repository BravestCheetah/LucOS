from tkinter import *
root=Tk()
root.title("Temporary calculator")


def Click(num):
  current_value=entry_box.get()
  entry_box.delete(0, END)
  entry_box.insert(0, str(current_value)+str(num)) 
def Clear():
  entry_box.delete(0,END)

def add():
  firstnumber = entry_box.get()
  global f_num
  global math
  math = "addition"
  f_num = int(firstnumber)
  entry_box.delete(0, END)

def subtract():
  firstnumber = entry_box.get()
  global f_num
  global math
  math = "subtraction"
  f_num = int(firstnumber)
  entry_box.delete(0, END)

def multiply():
  firstnumber = entry_box.get()
  global f_num
  global math
  math = "multiplication"
  f_num = int(firstnumber)
  entry_box.delete(0, END)

def divide():
  firstnumber = entry_box.get()
  global f_num
  global math
  math = "division"
  f_num = int(firstnumber)
  entry_box.delete(0, END)

def equals_button():
  secondnumber=entry_box.get()
  entry_box.delete(0, END)
  if math == "addition":
    entry_box.insert(0, f_num + int(secondnumber))
  elif math == "subtraction":
    entry_box.insert(0, f_num - int(secondnumber))
  elif math == "multiplication":
    entry_box.insert(0, f_num * int(secondnumber))
  else:
    entry_box.insert(0, f_num / int(secondnumber))



myFrame = LabelFrame(root, padx=20, pady=20, borderwidth=7)
myFrame.grid(padx=10, pady=10)

entry_box=Entry(myFrame,width=25, borderwidth=5)
entry_box.grid(row=0, columnspan=4, padx=30,pady=10)

button1 = Button(myFrame, text="1",padx=40, pady=20, command= lambda:Click(1))
button2 = Button(myFrame, text="2", padx=40, pady=20, command= lambda:Click(2))
button3 = Button(myFrame, text="3", padx=40, pady=20, command= lambda:Click(3))
button4 = Button(myFrame, text="4", padx=40, pady=20, command= lambda:Click(4))
button5 = Button(myFrame, text="5", padx=40, pady=20, command= lambda:Click(5))
button6 = Button(myFrame, text="6", padx=40, pady=20, command= lambda:Click(6))
button7 = Button(myFrame, text="7", padx=40, pady=20, command= lambda:Click(7))
button8 = Button(myFrame, text="8", padx=40, pady=20, command= lambda:Click(8))
button9 = Button(myFrame, text="9", padx=40, pady=20, command= lambda:Click(9))
button0 = Button(myFrame, text="0", padx=40, pady=20, command= lambda:Click(0))

addbutton=Button(myFrame, text="+", padx=40, pady=20, command= add)
subtractbutton=Button(myFrame, text="-", padx=40, pady=20,command=subtract)
multiplybutton=Button(myFrame, text="x", padx=40, pady=20,command=multiply)
dividebutton=Button(myFrame, text="÷", padx=40, pady=20, command=divide)

equalsbutton=Button(myFrame, text="=", padx=87, pady=20, command= equals_button)
clearbutton=Button(myFrame, text="CLEAR", padx=10, pady=10, width=25, fg="red", command=Clear)
exitbutton=Button(myFrame, text="EXIT", padx=25, pady=10, bg="red", fg="white", command=root.quit)


button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button0.grid(row=5, column=0)

addbutton.grid(row=2, column=3)
subtractbutton.grid(row=3, column=3)
multiplybutton.grid(row=4, column=3)
dividebutton.grid(row=5, column=3)
exitbutton.grid(row=1, column=3)

clearbutton.grid(row=1, column=0, columnspan=3)
equalsbutton.grid(row=5, column=1, columnspan=2)


root.mainloop()