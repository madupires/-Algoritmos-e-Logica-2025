numero_dias = int(input("Digite o número de dias da análise (ex: 5): "))

producao_total = 0
dias_acima_da_meta = 0
 
meta_diaria = 50
 
for dia in range(1, numero_dias + 1):
    producao = int(input(f"Digite a produção do dia {dia}: "))
    producao_total += producao
 

    if producao >= meta_diaria:
        dias_acima_da_meta += 1
 
media_diaria = producao_total / numero_dias
 

if media_diaria > 60 and dias_acima_da_meta >= 4:
    print("\nBÔNUS MÁXIMO! (15% sobre a produção total).")
    bonus = producao_total * 0.15
elif media_diaria > 50 or dias_acima_da_meta >= 3:
    print("\nBÔNUS PARCIAL! (5% sobre a produção total).")
    bonus = producao_total * 0.05
else:
    print("\nSem bônus. Metas de produtividade não foram atingidas.")
    bonus = 0.0
 
print("\n--- RESULTADOS FINAIS ---")
print(f"Média Diária de Produção: {media_diaria:.2f}")
print(f"Dias Acima da Meta: {dias_acima_da_meta}")
print(f"Valor Final do Bônus: R$ {bonus:.2f}")
 