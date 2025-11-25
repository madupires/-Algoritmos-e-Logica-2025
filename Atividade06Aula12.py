numero = int(input("Digite um número inteiro para ver sua tabuada: "))
 
contador = 1
 
print(f"\n--- Tabuada do {numero} ---")

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1 
    
print("\nTabuada completa.")