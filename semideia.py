nome_aluno = str(input("Digite o nome do aluno: "))
nome_disciplina = str(input("digite o nome da disciplina: "))
quantidade_notas = int(input("Digite a quantidade de notas: "))
soma_notas = 0

for i in range (1, quantidade_notas + 1):
    nota = float(input(f"digite a nota {i}: "))
    soma_notas =soma_notas + nota

media = soma_notas/ quantidade_notas
print("nome do aluno: ", nome_aluno)
print("nome da disciplina", nome_disciplina)
print(f"a média das notas é {media:.2f}.")

if media >= 7:
    print("Aluno reprovado")
else:
    print("aluno aprovado")