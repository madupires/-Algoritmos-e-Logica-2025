qtd_dias = int(input("Digite a quantidade de dias analisados: "))
 
soma_das_temperaturas = 0.0
 
for i in range(qtd_dias):
    temp = float(input(f"Digite a temperatura do dia {i+1} (°C): "))
    soma_das_temperaturas += temp
 
media_temp = soma_das_temperaturas / qtd_dias
 
if media_temp > 28:
    classificacao = "Média de temperatura: Clima Quente."
elif 18 <= media_temp <= 28:
    classificacao = "Média de temperatura: Clima Agradável."
else:
    classificacao = "Média de temperatura: Clima Frio."
 
print("\n--- Resultado ---")
print(f"Média final da temperatura: {media_temp:.2f} °C")
print(classificacao)
 