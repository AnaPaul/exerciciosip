from math import sqrt
a = float(input("Entre com o valor de a: ")
b = float(input("Entre com o valor de b: ")
c = float(input("Entre com o valor de c: ")
delta = b**2-4*a*c
print("Delta é igual a {}".format(delta))
raizd = sqrt(delta)
print("A raiz de delta é igual a {}".format(raizd))
x1 = (-b+raizd)/(2*a)
x2 = (-b-raizd)/(2*a)
print("x1 vale {} e x2 vale {}".format(x1,x2))
