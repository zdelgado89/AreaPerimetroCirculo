import math

# input
r= input("Ingrese al radio: ")
r= int(r)

# processing
a = math.pi * r**2
p= 2 * math.pi * r

# output
print("El area es: " + str(a))
print("El perimetro es: " + str(p))
