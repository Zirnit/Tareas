#Realiza un programa para preguntar al usuario cuatro notas:

#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion
#Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP
#Imprime el resultado redondeado a un decimal.

PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examen: "))
PP = float(input("Ingrese la nota de Presentacion: "))

Nota_final = PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1
print(round(Nota_final, 1))
