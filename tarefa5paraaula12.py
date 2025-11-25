numero_total_de_pecas = int(input("Digite o número total de peças a serem inspecionadas: "))

tolerancia = 0.5      
tamanho_ideal = 15.0  
 
soma_dos_tamanhos = 0.0
pecas_fora_tolerancia = 0
 
for i in range(1, numero_total_de_pecas + 1):
    tamanho_medido = float(input(f"Digite o tamanho medido da peça {i} (cm): "))
    soma_dos_tamanhos += tamanho_medido
 
    desvio = abs(tamanho_medido - tamanho_ideal)
    if desvio > tolerancia:
        pecas_fora_tolerancia += 1
 
media_tamanho = soma_dos_tamanhos / numero_total_de_pecas
 
if pecas_fora_tolerancia == 0:
    classificacao = "Lote Aprovado: Qualidade Perfeita (0 peças fora da tolerância)."
elif pecas_fora_tolerancia <= 2:
    classificacao = "Lote Aceitável: Pequena correção necessária."
else:
    classificacao = "Lote Reprovado: Alta taxa de defeito."
 
print("\n--- RESULTADOS FINAIS ---")
print(f"Média de Tamanho das Peças: {media_tamanho:.2f} cm")
print(f"Peças Fora da Tolerância: {pecas_fora_tolerancia}")
print(classificacao)