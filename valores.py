saldo = 2000
valor = int(input("Informe o valor que deseja sacar: "))

if valor == saldo:
    print("O valor coicide com o saldo atual.")
    resposta = str(input("Deseja continuar?! Digite S para Sim ou N para Não: "))
    if resposta == "S":
       print("Processando pagamento...")
    elif resposta == "N":
         print("Operação finalizada!")

elif valor > saldo:
    print("Saldo insuficiente!")
else:
    print("Processando pagamento...")



