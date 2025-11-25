salario_base = 800.00
limite_falhas = 1

soma_produtividade = 0
falhas = 0

for dia in range(1, 6):
    produtividade = float(input(f"Digite a pontuação de produtividade do dia {dia} (0 a 100): "))
    soma_produtividade += produtividade

    if produtividade < 60:
        falhas += 1

produtividade_media = soma_produtividade / 5

if produtividade_media > 80 and falhas <= limite_falhas:
    print("\nPagamento Máximo: Bônus de 10% aplicado.")
    pagamento_final = salario_base * 1.10
elif 60 <= produtividade_media <= 80 or falhas > limite_falhas:
    print("\nPagamento Padrão: Penalidade de 5% aplicada (Devido a falhas).")
    pagamento_final = salario_base * 0.95
else:
    print("\nPenalidade Severa: Pagamento reduzido em 25%.")
    pagamento_final = salario_base * 0.75

print("\n--- RESULTADOS FINAIS ---")
print(f"Produtividade Média: {produtividade_media:.2f}")
print(f"Contagem de Falhas: {falhas}")
print(f"Pagamento Final: R$ {pagamento_final:.2f}")
 