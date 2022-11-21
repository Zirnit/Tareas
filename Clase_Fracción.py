"""
Clase Fracción
Completa la clase Fracción con los métodos necesarios para que se pueden sumar, restar y dividir fracciones.
"""

class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
        return r

    def __repr__(self):
        entero=self.num//self.den
        if entero>0:
            resto=self.num%self.den
            if resto>0:
                return "{0} {1}/{2}".format(entero,resto,self.den)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.num,self.den)

    def a_numero(self):
        return self.num/self.den

    def __add__(self, other):
        r=Fraccion(0,0)
        r.num=self.num*other.den+self.den*other.num
        r.den=self.den*other.den
        return r

    def __sub__(self, other):
        r=Fraccion(0,0)
        r.num=self.num*other.den-self.den*other.num
        r.den=self.den*other.den
        return r

    def __truediv__(self, other):
        r=Fraccion(0,0)
        r.num=self.num*other.den
        r.den=self.den*other.num
        return r

if __name__ == "__main__":
    f=input("Ingresa la primera fraccion [a/b]: ")
    f=f.split("/")
    f1=Fraccion(int(f[0]),int(f[1]))
    f=input("Ingresa la segunda fraccion [c/d]: ")
    f=f.split("/")
    f2=Fraccion(int(f[0]),int(f[1]))
    print("La suma es ",f1+f2)
    print("La resta es ",f1-f2)
    print("La multiplicación es ",f1*f2)
    print("La división es ",f1/f2)
         
