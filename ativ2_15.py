#Define a quantidade de linhas da matriz
NUM_LINHAS = 3

#Define a quantidade de colunas da matriz
NUM_COLUNAS = 3

#Cria uma lista vazia que vai representar a matriz
matriz = []

#Cria as linhas da matriz preenchidas com zeros
for i in range(NUM_LINHAS):     #Loop para criar cada linha
    matriz.append([0] * NUM_COLUNAS)    #adiciona uma lista com N zeros

#Preenchimento da matriz com valores digitados pelo usuário
for i in range(NUM_LINHAS): # Loop para as linhas (i)
    for j in range(NUM_COLUNAS): # Loop para as colunas (j)
        #Solicita um valor para a posição correspondente da matriz
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        matriz[i][j] = valor    #Armazena o valor na posição correta

#Impressão da matriz
for i in range(NUM_LINHAS): #Loop para cada linha 
    for j in range(NUM_COLUNAS):    #Loop para cada coluna
        print(matriz[i][j], end="\t")   #Imprime os valores da linha separados por TAB
        
    print() # Pula linha após cada linha da matriz