cidades = []
 
NUMERO_CIDADES = 5
 
print("\n--- Cadastro de Cidades ---")
 
for i in range(NUMERO_CIDADES):
   nome_cidade = input(f"Digite o nome da Cidade {i + 1}: ")
cidades.append(nome_cidade)
 
print("\n--- Lista de Cidades em Maiúsculo ---")
 
for i in range(len(cidades)):
    cidade_atual = cidades[i]
 
    cidade_maiuscula = cidade_atual.upper()
 
print(f"Cidade {i + 1}: {cidade_maiuscula}")