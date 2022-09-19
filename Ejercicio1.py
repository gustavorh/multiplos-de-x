# Se desea mostrar todos los múltiplos de 6 entre 6 y 150 ambos inclusive.

numero = 1
for numero in range (6,151):
  if numero % 6 == 0:
    esMultiplo = numero
    print("%d es multiplo de 6" % (esMultiplo))