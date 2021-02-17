from tkinter import *

root = Tk()

def Add():
    Result = float(Number1.get()) + float(Number2.get())
    ResultLabel = Label(root, text="Result: " + str(Result))
    ResultLabel.grid(row = 1)

def Minus():
    Result = float(Number1.get()) - float(Number2.get())
    ResultLabel = Label(root, text="Result: " + str(Result))
    ResultLabel.grid(row = 1)

def Multiply():
    Result = float(Number1.get()) * float(Number2.get())
    ResultLabel = Label(root, text="Result: " + str(Result))
    ResultLabel.grid(row = 1)

def Divide():
    Result = float(Number1.get()) / float(Number2.get())
    ResultLabel = Label(root, text="Result: " + str(Result))
    ResultLabel.grid(row = 1)

def Input1():
    typee = False
    while typee == False:
        try:
            Number1 = float(input("Introduce 1st Number"))
            typee == True
            break
        except TypeError:
            Input2()
        else:
            Input2()
    return(Number1)

def Input2():
    typee = False
    while typee == False:
        try:
            Number2 = float(input("Introduce 2nd Number"))
            typee == True
            break
        except TypeError:
            Input2()
        else:
            Input2()
    return(Number2)

def Operation():

    operator = input("Input your operator").lower()
    if (operator == "+"):
        N1 = Input1()
        N2 = Input2()
        print(Add(N1, N2))
    elif (operator == "*" or operator == "x"):
        N1 = Input1()
        N2 = Input2()
        print(Multiply(N1, N2))
    elif (operator == "-"):
        N1 = Input1()
        N2 = Input2()
        print(Minus(N1, N2))
    elif (operator == "/"):
        N1 = Input1()
        N2 = Input2()
        print(Divide(N1, N2))
    else:
        Operation()


Number1 = Entry(root, width = 15, borderwidth = 5)
Number1.grid(row = 0)

Number2 = Entry(root, width = 15, borderwidth = 5)
Number2.grid(row = 2)

PlusButton = Button(root, text="+", padx = 15, pady = 15, bg="Light Grey", command=Add)
MinusButton = Button(root, text="-", padx = 15, pady = 15, bg="Light Grey", command=Minus)
MultiButton = Button(root, text="*", padx = 16, pady = 15, bg="Light Grey", command=Multiply)
DivButton = Button(root, text="/", padx = 15, pady = 15, bg="Light Grey", command=Divide)

PlusButton.grid(row = 3, column = 0)
MinusButton.grid(row = 3, column = 1)
MultiButton.grid(row = 4, column = 0)
DivButton.grid(row = 4, column = 1)

root.mainloop()

Number1 = 0
Number2 = 0
Result = 0
