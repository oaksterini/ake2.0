import sys, os

a = int(input("Välj ett tal:\n"))
h = float(input("Välj ett h:\n"))


def f(x):
    b = int(input("Välj en funktion:\n"))
    return b

def f_prim(a):
    return (f(a+h) - f(a)) / h





print("f'(4) är ungefär", f_prim(a))



