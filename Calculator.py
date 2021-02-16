from tkinter import *

root = Tk()

Number1 = 0
Number2 = 0
Result = 0

def Add(N1, N2):
    Result = N1 + N2
    return(Result)

def Minus(N1, N2):
    Result = N1 - N2
    return(Result)

def Multiply(N1, N2):
    Result = N1 * N2
    return(Result)

def Divide(N1, N2):
    Result = N1 / N2
    return(Result)

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

Operation()

