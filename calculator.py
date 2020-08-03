import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Simple Calculator 2.0")
root.resizable(0, 0)

nextOperand = False
secondNumTurn = False
firstNum = 0
secondNum = 0
operator = ""
outputVar = tkinter.StringVar()
outputVar.set("0")

def buttonClick(buttonText):
    global nextOperand

    if nextOperand:
        outputVar.set(buttonText)
        nextOperand = False
    else:
        if outputVar.get() != "0":
            outputVar.set(outputVar.get() + buttonText)
        else:
            outputVar.set(buttonText)

def addition():
    global nextOperand
    global operator
    global firstNum

    operator = "+"
    firstNum = int(outputVar.get())
    nextOperand = True

def substraction():
    global nextOperand
    global operator
    global firstNum

    operator = "-"
    firstNum = int(outputVar.get())
    nextOperand = True

def equals():
    global nextOperand
    global firstNum
    global secondNum
    global operator

    if operator == "+" and nextOperand == False:
        secondNum = int(outputVar.get())
        total = firstNum + secondNum
        outputVar.set(str(total))
        firstNum = total
        nextOperand = True

    elif operator == "-" and nextOperand == False:
        secondNum = int(outputVar.get())
        total = firstNum - secondNum
        outputVar.set(str(total))
        firstNum = total
        nextOperand = True

def clearAll():
    global nextOperand
    global firstNum
    global secondNum
    global operator

    outputVar.set("0")
    nextOperand = False
    firstNum = 0
    secondNum = 0
    operator = ""

def clear():
    outputVar.set("0")



button0 = ttk.Button(root, text="0", command=lambda: buttonClick("0"))
button1 = ttk.Button(root, text="1", command=lambda: buttonClick("1"))
button2 = ttk.Button(root, text="2", command=lambda: buttonClick("2"))
button3 = ttk.Button(root, text="3", command=lambda: buttonClick("3"))
button4 = ttk.Button(root, text="4", command=lambda: buttonClick("4"))
button5 = ttk.Button(root, text="5", command=lambda: buttonClick("5"))
button6 = ttk.Button(root, text="6", command=lambda: buttonClick("6"))
button7 = ttk.Button(root, text="7", command=lambda: buttonClick("7"))
button8 = ttk.Button(root, text="8", command=lambda: buttonClick("8"))
button9 = ttk.Button(root, text="9", command=lambda: buttonClick("9"))

buttonAdd = ttk.Button(root, text="+", command=addition)
buttonSub = ttk.Button(root, text="-", command=substraction)
buttonEquals = ttk.Button(root, text="=", command=equals)
buttonClearAll = ttk.Button(root, text="AC", command=clearAll)
buttonClear = ttk.Button(root, text="Clear", command=clear)
output = tkinter.Label(root, textvariable=outputVar, justify="left", wraplength=300)



button1.grid(row=2, column=1) # 1
button2.grid(row=2, column=2) # 2
button3.grid(row=2, column=3) # 3

button4.grid(row=3, column=1) # 4
button5.grid(row=3, column=2) # 5
button6.grid(row=3, column=3) # 6

button7.grid(row=4, column=1) # 7
button8.grid(row=4, column=2) # 8
button9.grid(row=4, column=3) # 9

button0.grid(row=5, column=1)   # 0
buttonAdd.grid(row=5, column=2)
buttonSub.grid(row=5,column=3)

output.grid(row=1, column=3, columnspan=3)

buttonClearAll.grid(row=6, column=1)
buttonClear.grid(row=6, column=2)
buttonEquals.grid(row=6, column=3)



root.mainloop()
