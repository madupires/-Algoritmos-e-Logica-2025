# Vetores / Listas em Python com INPUT
 
# Aqui eu defino quantos nomes o meu vetor vai ter. É como se eu dissesse: "quero guardar exatamente 5 nomes".
TAMANHO_VETOR = 5
 
# Aqui eu crio a lista já com o tamanho fixo.
# Coloco 5 strings vazias ("") só pra reservar o espaço na memória.
# Depois eu vou trocando essas posições vazias pelos nomes digitados.
vetor_nomes = [""] * TAMANHO_VETOR  # minha listinha de nomes
 
print("\n--- Entrada de Nomes (5 Posições Fixas) ---")
 
# PRIMEIRO FOR: onde eu PEGO os nomes do teclado e guardo no vetor
for i in range(TAMANHO_VETOR):
    # 'i' é o índice da lista (começa em 0 e vai até 4).
    # Aqui eu peço pro usuário digitar o nome do aluno.
    # Uso f-string pra mostrar o número do aluno (i + 1) e a posição real no vetor [i].
    nome = input(f"Digite o nome do Aluno {i + 1} (Posição [{i}]): ")
 
    # Aqui eu pego o nome que a pessoa digitou e guardo dentro do vetor, exatamente na posição i.
    vetor_nomes[i] = nome
 
print("\n--- Processamento dos Dados ---")
print("Os nomes registrados, acessados por índice:")
 
# SEGUNDO FOR: onde eu LEIO o que foi guardado e mostro na tela
for i in range(TAMANHO_VETOR):
    # Aqui eu pego o nome que está guardado na posição i e jogo pra variável 'nome_atual' só pra ficar mais legível.
    nome_atual = vetor_nomes[i]
 
    # E aqui eu mostro o nome na tela.
    # Poderia usar 'print(nome_atual)', mas vou imprimir direto do vetor também.
    print(nome_atual)