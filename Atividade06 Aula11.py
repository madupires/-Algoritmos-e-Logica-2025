custo_fixo = 5500.0
custo_materia_prima = float(input("Digite o custo da matéria-prima por item: R$ "))
quantidade_itens = 100
 
custo_variavel_total = 0.0
 
for i in range(quantidade_itens):

    desperdicio = custo_materia_prima * 0.05
    custo_total_item = custo_materia_prima + desperdicio
    custo_variavel_total += custo_total_item

custo_total = custo_fixo + custo_variavel_total

if custo_total < 3500:
    margem = 0.35
elif custo_total <= 5000:
    margem = 0.20
else:
    margem = 0.15

preco_minimo = (custo_total / quantidade_itens) * (1 + margem)

print("\n--- RESULTADOS ---")
print(f"Custo Fixo: R$ {custo_fixo:.2f}")
print(f"Custo Variável Total: R$ {custo_variavel_total:.2f}")
print(f"Custo Total de Produção: R$ {custo_total:.2f}")
print(f"Margem de Lucro Aplicada: {margem * 100:.0f}%")
print(f"Preço Mínimo de Venda por Item: R$ {preco_minimo:.2f}")
 