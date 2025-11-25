SENHA_CORRETA = "python123"
tentativas_erradas = 0
senha_digitada = ""  

print("\n--- Sistema de Login ---")

while senha_digitada != SENHA_CORRETA:
    senha_digitada = input("Digite a senha: ")

    if senha_digitada == SENHA_CORRETA:
        print(f"\nSenha válida! Acesso concedido.")       
    else:
        tentativas_erradas += 1
        print("Senha incorreta. Tente novamente.")

print ("Total de entradas erradas", tentativas_erradas)

#A variavel começa vazia para que a pessoa possa digitar a mensagem que quiser.