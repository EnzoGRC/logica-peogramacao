numero1 = float(input('Informe o número aqui: '))
operacao = str(input('operacao :'))
numero2 = float(input('Informe o outro número aqui: '))
resultado = 0

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2

print(resultado)