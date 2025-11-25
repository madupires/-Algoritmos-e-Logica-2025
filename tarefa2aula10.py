qtd_dias = int(input("Digite a quantidade de dias de vendas que serão analisados: "))
vendas_totais = 0.0
 
for i in range(qtd_dias):
    valor_venda = float(input(f"Digite o valor de vendas do dia {i+1}: R$ "))
    vendas_totais += valor_venda
 
media_diaria = vendas_totais / qtd_dias
 
if media_diaria > 1500:
    imposto_fixo = 200.0
else:
    imposto_fixo = 50.0
 
if vendas_totais > 10000:
    taxa_servico_percentual = 0.08
else:
    taxa_servico_percentual = 0.05
 
taxa_servico = vendas_totais * taxa_servico_percentual
 
valor_liquido = vendas_totais - taxa_servico - imposto_fixo
 
print("\n--- Resultado Final ---")
print(f"Valor Total das Vendas: R$ {vendas_totais:.2f}")
print(f"Média Diária de Vendas: R$ {media_diaria:.2f}")
print(f"Imposto Fixo Aplicado: R$ {imposto_fixo:.2f}")
print(f"Percentual da Taxa de Serviço: {taxa_servico_percentual*100:.0f}%")
print(f"Valor da Taxa de Serviço: R$ {taxa_servico:.2f}")
print(f"Valor Líquido Final: R$ {valor_liquido:.2f}")