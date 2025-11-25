quantidade_prod= int(input("Digite a quantidade de produtos diferentes que irá comprar: "))
total_da_compra= 0.0
for i in range(1, quantidade_prod +1):
    preco = float(input(f"Digite o preço do produto {i}: R$ "))
    total_da_compra = total_da_compra + preco
print(f"O total a pagar é: R${total_da_compra:.2f}") 