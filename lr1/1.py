a = float(input('input a: '))
b = float(input('input b: '))
c = float(input('input c: '))
try:
    z = abs(1-a*b**c-a*(b**2-c**2)+(b-c+a)*(12+b)/(c-a))
    print (z)
except ZeroDivisionError:
    print('zero division not implimented')
