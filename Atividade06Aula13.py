lista_notas= []
Numero_notas = 5
for i in range (Numero_notas):
    nota= float(input(f"Digite a nota do aluno {i +1}: "))
    lista_notas.append(nota)
print("\n Listagem de notas: ")
for i in range (len(lista_notas)):
    print(f"Anota da posição {i} é: {lista_notas}")