alunos = []
for i in range(3):
    nome = input("Nome: ")
    idade = input("idade: ")
    nota  = input("Nota: ")
    aluno = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(aluno)
    print("---------------------------")

for aluno in aluno:
    print(f"nome: {aluno["nome"]},idade: {aluno["idade"]},nota: {aluno["nota"]}")