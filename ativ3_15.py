#Quantidade de provas aplicadas
NUM_PROVAS = 3

#Quantidade total de alunos
NUM_ALUNOS = 5

#Lista que armazenará todas as notas (será uma matriz 3x5)
matriz_notas = []

#Mensagem inicial explicando o que será inserido
print(f"--- Entrada de Notas para 3 Provas de 5 Alunos ({NUM_PROVAS}x{NUM_ALUNOS}) ---")

#Loop externo percorre cada prova
for i in range(NUM_PROVAS):
    linha_provas = []   #Lista que guardará notas dos 5 alunos nesta prova
    print(f"\n[ PROVA {i + 1} ]")   #Exibe qual prova está sendo preenchida

    #Loop interno: percorre cada aluno
    for j in range(NUM_ALUNOS):
        #Pede a nota do aluno j+1 e converte para float(nota pode ser decimal) 
            nota = float(input(f"  Digite a nota do Aluno {j + 1} (Posição [{i}][{j}]): "))
            linha_provas.append(nota)   #Adiciona a nota na linha da prova

    matriz_notas.append(linha_provas)   #Salva a linha de notas na matriz principal

#Finalizou o preenchimento
print("\n--- Matriz de Notas Registrada ---")

#Exibe título explicando formato da organização
print("Organização: [Prova] [Aluno]")

#Impressão da matriz organizada
for i in range(NUM_PROVAS):     #Loop peklas provas (linhas)
    print(f"Prova {i + 1}: ", end="")   #Escreve qual prova esta sendo exibida

    for j in range(NUM_ALUNOS):     #Loop pelos alunos (colunas)
        #Imprime a nota formatada com 2 casas decimais
        print(f"{matriz_notas[i][j]:.2f}", end="\t")
    print()     #Quebra de linha após cada prova