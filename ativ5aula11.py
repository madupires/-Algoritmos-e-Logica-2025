quantidade = int(input("Digite a quantidade de notas fiscais: "))
soma_das_notas = 0.0
for i in range(quantidade):
    valor_nota = float(input(f"Digite o valor da nota {i+1}: R$ "))
    soma_das_notas += valor_nota
 
if soma_das_notas <= 1000:
    aliquota = 0.05
elif soma_das_notas <= 4999.99:
    aliquota = 0.09
elif soma_das_notas <= 14999.99:
    aliquota = 0.12
else:
    aliquota = 0.16

valor_imposto = soma_das_notas * aliquota

print("\n--- Resultado ---")
print(f"Total das notas: R$ {soma_das_notas:.2f}")
print(f"Alíquota aplicada: {aliquota * 100:.0f}%")
print(f"Valor total do imposto a ser pago: R$ {valor_imposto:.2f}")