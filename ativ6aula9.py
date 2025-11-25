quant_alun = int(input("Digite a quantidade de alunos na turma: "))
soma_das_notas = 0
 
for i in range(1, quant_alun + 1):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    soma_das_notas = soma_das_notas + nota
 
media = soma_das_notas / quant_alun
 
print(f"A média da turma é: {media}")