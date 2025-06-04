def converter_dolar_para_real():
    cotacao_dolar = 5.64 #Taxa de cambio fixa para exemplo
    dolares = float(input("Digite p valor em dólares (USD): "))
    reais = dolares * cotacao_dolar
    print("------------------------------------------------")
    print(f" {dolares} USD esquivale a R$ {reais: .2f}")

def coonverter_real_para_dolar():
    cotacao_dolar = 5.64
    reais = float(input("Digite o valor em reais (BRL): "))
    dolares = reais / cotacao_dolar
    print("------------------------------------------------")
    print(f" {reais} BRL equivale a US$ {dolares: .2f}")

def menu():
    while True:
        print("\nConversor de Moedas")
        print("[1] Converter Dólar para Real")
        print("[2] Converter Real para Dólar")
        print("[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            converter_dolar_para_real()
        elif opcao == '2':
            coonverter_real_para_dolar()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("!!! Opção inválida. tente novamente. !!!")

#Chamada funcao
menu()



#Conversor de Dólar para Real<

#Este projeto é um simples conversor de moeda que transforma valores em dólar (USD) para real brasileiro (BRL).

 #Funcionalidades

#Converte um valor em dólar para real com base na cotação atual ou uma cotação fixa definida no código.

#Fácil de usar e entender.

#Pode ser adaptado para outras moedas.
