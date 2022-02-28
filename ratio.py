from fractions import Fraction


x = Fraction(input('Введите первое число: '))
z = input('Знак: ')
y = Fraction(input('Введите второе чилсо: '))

def sum(a,b):
    return a+b
def mult(c,f):
    return c*f
def sub(g,h):
    return g-h
def div(s,d):
    return s//d


if z == '+':
    print(sum(x,y))
elif z == '-':
    print(sub(x,y))
elif z == '/':
    print(div(x,y))
elif z == '*':
    print(mult(x,y))

