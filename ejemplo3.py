# abrir un fichero .txt y ver si se existe un error al extraerlo
# en este caso si se puede leer el archivo numeros.txt

try:
    fichero = open("numeros.txt", "r")
    lines = fichero.readlines()
    print(lines)
except IOError:
    print("No encuentro el fichero o no puedo leerlo")
else:
    print("He leido el fichero sin problemas. Lo cierro y termino.")
    fichero.close()