a = int(input())
b = int(input())
c = int(input())
D = b*b-4*a*c
if D>0:
    print('x1','=',(-b+D**0.5)/2*a)
    print('x2','=',(-b-D**0.5)/2*a)
elif D==0:
    print('x1','=',(-b+D**0.5)/2*a)
if D<0:
    print('Нет корней')
