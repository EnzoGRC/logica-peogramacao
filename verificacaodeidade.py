ano_nascimento = int(input('digite o ano de nascimento: '))
ano_atual =2024
idade=ano_atual-ano_nascimento
if idade >=16:
    print('pode votar este ano')
else:
    print('não pode votar esse ano')