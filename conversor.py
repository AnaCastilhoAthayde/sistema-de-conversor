num_dolar = float(input("Digite o valor em dólar: "))
num_real = float(input("Digite o valor em real: "))

conversao_real = num_dolar * 5.64
conversao_dolar = num_real / 5.64

print(f"seu dólar convertido para real é: {conversao_real}R$")
print(f"Seu real convertido para dólar é: {conversao_dolar}$")