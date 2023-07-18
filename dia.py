fim_de_semana = True
semana = False

numero = int(input("Digite um número: "))

if numero >= 1 and numero <= 5:
    if semana:
        print("A variável 'semana' é verdadeira (True).")
    else:
        print("A variável 'semana' é falsa (False).")
elif numero == 6 or numero == 7:
    if fim_de_semana:
        print("A variável 'fim_de_semana' é verdadeira (True).")
    else:
        print("A variável 'fim_de_semana' é falsa (False).")
else:
    print("Número inválido. Por favor, digite um número de 1 a 7.")