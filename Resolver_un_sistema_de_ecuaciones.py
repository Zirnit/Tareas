#Sistema de Ecuaciones

def res_ecuaciones(a, b, c, d, e, f):
    determinante = a*e - d*b
    deter_x = c*e - f*b
    deter_y = f*a - c*d 
    y = deter_y/determinante
    x = deter_x/determinante
    print("x=" + str(round(x,1)) + " y=" + str(round(y,1)))

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
res_ecuaciones(a, b, c, d, e, f)
