#Ordenar tres números

from statistics import median

numero1 = int(input("Ingresar numero 1\n"))
numero2 = int(input("Ingresar numero 2\n"))
numero3 = int(input("Ingresar numero 3\n"))

mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)
medio = median([numero1, numero2, numero3])
  
print(str(menor) + ", " + str(medio) + ", " + str(mayor))
