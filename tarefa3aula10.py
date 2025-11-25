qtd_dias = int(input("Quantidade de dias da viagem: "))
 
total_km_percorridos = 0.0
 
for i in range(qtd_dias):
    km_dia = float(input(f"KM percorridos no dia {i+1}: "))
    total_km_percorridos += km_dia

KM_POR_LITRO = 12.0      
PRECO_LITRO  = 4.80      
 
total_litros = total_km_percorridos / KM_POR_LITRO
custo_total  = total_litros * PRECO_LITRO
 
if custo_total > 500.0:
    classificacao = "Alerta de Gastos: O custo total com combustível foi alto (Acima de R$ 500,00)."
else:
    classificacao = "Gastos sob controle: O custo total com combustível foi baixo ou moderado."
 
print("\n--- Resultado ---")
print(f"Total de KM percorridos: {total_km_percorridos:.2f} km")
print(f"Total de litros consumidos: {total_litros:.2f} L")
print(f"Custo total com combustível: R$ {custo_total:.2f}")
print(classificacao)