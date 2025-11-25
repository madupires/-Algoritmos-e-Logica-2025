qtd_notas = int(input("Digite a quantidade de notas fiscais: "))
soma_das_notas = 0.0

for i in range(qtd_notas):
    valor_nota = float(input(f"Digite o valor da nota {i+1}: R$ "))
    soma_das_notas += valor_nota
 
if soma_das_notas <= 100.0:
    aliquota = 0.05
elif soma_das_notas <= 4999.99:
    aliquota = 0.09
elif soma_das_notas <= 14999.99:
    aliquota = 0.12
else:
    aliquota = 0.16
 
valor_imposto = soma_das_notas * aliquota
 
print("\n--- Resultado ---")
print(f"Valor total das notas: R$ {soma_das_notas:.2f}")
print(f"Alíquota aplicada: {aliquota*100:.0f}%")
print(f"Valor total do imposto: R$ {valor_imposto:.2f}")