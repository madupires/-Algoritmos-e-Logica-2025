# Listas – cálculo de média de notas
 
# 1. DEFININDO O TAMANHO DO VETOR
# Aqui eu defino o tamanho fixo da lista (vetor) com 5 posições. É como se eu dissesse: “meu programa vai guardar 5 notas”.
TAMANHO_VETOR = 5
 
# 2. PRÉ-ALOCAÇÃO DO VETOR
# Aqui eu crio a lista já com 5 espaços reservados, todos começando em 0.0.
# Isso é uma simulação da “alocação de memória”, tipo o que a gente faz em C.
vetor_notas = [0.0] * TAMANHO_VETOR
 
# Variáveis auxiliares:
# 'soma_notas' vai acumular todas as notas somadas,
# e 'media' vai guardar o resultado da média final.
soma_notas = 0.0
media = 0.0
 
print("\n--- Entrada de 5 Notas ---")
 
# 3. PRIMEIRO FOR: LEITURA E ARMAZENAMENTO
# Esse laço for vai repetir 5 vezes (de 0 até 4), pedindo uma nota a cada volta.
for i in range(TAMANHO_VETOR):
    # Aqui eu peço pro usuário digitar a nota.
    # Uso o i+1 só pra deixar o número bonitinho (começando do 1, e não do 0).
    nota = float(input(f"Digite a Nota {i + 1} (Posição [{i}]): "))
 
    # Aqui eu guardo a nota digitada na posição correspondente da lista.
    vetor_notas[i] = nota
 
print("\n--- Processamento dos Dados ---")
 
# 4. SEGUNDO FOR: SOMA E ACÚMULO
# Agora eu vou percorrer novamente o vetor, somando todas as notas dentro dele.
for i in range(TAMANHO_VETOR):
    # Aqui pego o valor da nota que está na posição i e somo ao total.
    soma_notas = soma_notas + vetor_notas[i]
 
# 5. CÁLCULO DA MÉDIA
# Aqui eu faço a média simples: soma de todas as notas dividida pela quantidade.
# Faço uma checagem só pra garantir que o vetor não está vazio.
if TAMANHO_VETOR > 0:
    media = soma_notas / TAMANHO_VETOR
 
# 6. EXIBIÇÃO DOS RESULTADOS
# Agora mostro tudo no final de forma organizada.
print(f"\nVetor de Notas Registrado: {vetor_notas}")
print(f"Soma Total das Notas: {soma_notas:.2f}")
print(f"Média Final da Turma: {media:.2f}")