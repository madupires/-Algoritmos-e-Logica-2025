# Vetores / Listas em Python
 
# 1. CRIAÇÃO DO VETOR (LISTA)
# Aqui criei uma variável chamada "lista_frutas". É tipo uma caixinha que guarda várias coisas juntas. Cada fruta é um item da lista.
lista_frutas = ["Maçã", "Banana", "Uva", "Pêra", "Manga"]
 
print("--- Análise da Lista ---")  # Aqui serve como um "título bonitinho" pra organizar a saída
 
# 2. EXIBIÇÃO TOTAL
# Aqui eu peço pro Python mostrar a lista inteira, do jeito que ela foi criada, com todos os elementos.
print("Lista completa:", lista_frutas)
 
# 3. ACESSO AO PRIMEIRO ELEMENTO (ÍNDICE 0)
# Detalhe importante: em Python a contagem começa em 0, não em 1.
# Então:
#   posição 0 = primeiro item, posição 1 = segundo item e por aí vai...

# Aqui eu pego o primeiro elemento da lista (posição 0) e guardo na variável "primeiro".
primeiro = lista_frutas[0]
# E aqui eu mostro qual é esse primeiro elemento.
print("1. Primeiro elemento (índice 0):", primeiro)
 
# 4. ACESSO AO TERCEIRO ELEMENTO (ÍNDICE 2)
# Seguindo a mesma lógica: posição 2 = terceiro item da lista. Ou seja, nesse caso, deve ser a "Uva".

# Aqui eu pego o elemento da posição 2 e guardo na variável "terceiro".
terceiro = lista_frutas[2]
# E mostro esse valor pra confirmar.
print("2. Terceiro elemento (índice 2):", terceiro)
 
# 5. ACESSO AO ÚLTIMO ELEMENTO (ÍNDICE -1)
# Agora vem o "truquezinho" de Python:
# quando usamos índice negativo, ele começa a contar do final.
#   -1 = último item
#   -2 = penúltimo
#   -3 = antepenúltimo...
# Então, aqui eu pego o último elemento da lista usando [-1].
ultimo = lista_frutas[-1]
# E mostro qual fruta é a última da lista.
print("3. Último elemento (índice -1):", ultimo)