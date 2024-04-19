contador = 0

numero = int(input("informe ate que numero contar..: "))
elevado= int(input("informe o numero elevado..:"))
while contador < numero:
    contador = contador + elevado
    print("contador", int(contador))