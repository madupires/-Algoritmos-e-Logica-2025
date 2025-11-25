v_base= float(input("Digite o Valor Base do Bõnus (R$): "))
p_ind=float(input("Digite a Pontuação da Performance Individual (0 a 100): "))
p_equipe=float(input("Digite a Pontuação de Performance da Equipe (0 a 100):"))
if p_ind>90:
    fap=1.25
elif p_ind>70:
    fap=1.00
else:
    fap=0.90
   
b_ajustado = v_base * fap
 

if p_equipe > 85:
    if p_ind > 95 or b_ajustado > 5000:
        print("\nBônus Máximo (30% Extra).")
        b_final = b_ajustado * 1.30
    else:
        print("\nBônus Padrão (10% Extra).")
        b_final = b_ajustado * 1.10
elif 60 <= p_equipe <= 85:
    if p_ind < 60:
        print("\nPenalidade por Desempenho Individual (15% de Redução).")
        b_final = b_ajustado * 0.85
    else:
        print("\nSem Alteração Adicional.")
        b_final = b_ajustado
else:
    print("\nPenalidade Severa (25% de Redução).")
    b_final = b_ajustado * 0.75
 
print("\n--- RESULTADOS FINAIS ---")
print(f"Valor Base do Bônus: R$ {v_base:.2f}")
print(f"Fator de Ajuste Aplicado (FAP): {fap}")
print(f"Bônus Ajustado: R$ {b_ajustado:.2f}")
print(f"Bônus Final: R$ {b_final:.2f}")
 