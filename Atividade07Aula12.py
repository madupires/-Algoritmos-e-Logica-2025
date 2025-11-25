simbolo = input("Digite um caractere ou símbolo (ex: *, #, @, -): ")
 
repetir = "sim"
 
while repetir.lower() == "sim":
    print(simbolo * 20)
    repetir = input("Deseja ver outra linha? (Digite SIM para continuar): ").lower()
    
print("\nGerador encerrado. Obrigado!")