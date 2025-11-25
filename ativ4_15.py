#Quantidade de itens que o cardápio vai ter
NUM_ITENS = 3

#Lista  vazia que vai armazenar todos os itens do cardápio
cardapio = []

#Mensagem inicial para o usuário
print("--- Entrada de Dados para Cardápio (3 Itens) ---")

#Loop para coletar os dados de cada item do cardápio
for i in range(NUM_ITENS):  #Repete 3 vezes, uma para cada item
    print(f"\n[ Item {i + 1} ]")    #Exibe qual item está sendo preenchido

    #Pede o nome do item
    nome = input("  Digite o nome do item: ")
    
    #Pede o preço do item (convertido para float)
    preco = float(input("  Digite o preço do item: R$ "))
   
   #Cria uma lista com nome e preço do item
    item_completo = [nome, preco]
   
   #Adiciona esse item dentro da lista principal 'cardápio'
    cardapio.append(item_completo)


print("\n--- Acessando Elementos Específicos ---")

#Acessa o preço do item 2 (linha 1, coluna 1)
preco_item2 = cardapio[1][1]
print(f"O preço do Item 2 (posição [1][1]) é: R$ {preco_item2:.2f}")

#Acessa o nome do item 3 (linha 2, coluna 0)
nome_item3 = cardapio[2][0]
print(f"O nome do Item 3 (posição [2][0]) é: {nome_item3}")

print("\n--- Exibição do Cardápio Completo ---")
for item in cardapio:
    #Item[0] -> nome / item [1] -> preço
    print(f"Nome: {item[0]} | Preço: R$ {item[1]:.2f}")