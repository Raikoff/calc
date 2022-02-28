

first1 = int(input('введите: '))
first2 = int(input('Введите: '))
x = complex(first1,first2)

second1 = int(input('введите: '))
second2 = int(input('Введите: '))
y = complex(second1,second2)

z = input('Действие: ')
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
