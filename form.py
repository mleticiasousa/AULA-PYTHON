def obter_nome():
    nome = input("Digite seu nome: ")
    return nome

def feedback_personalizado(nome):
    return f"Cadastro realizado com sucesso, {nome}!"

def main():
    nome_usuario = obter_nome()
    feedback = feedback_personalizado(nome_usuario)
    print(feedback)

name = str(input("Digite seu nome: "))
age = int(input("Idade: "))
nome = str(input("E-mail: "))
nome = int(input("Telefone: "))
nome = str(input("Deixe aqui sua sugestão: "))

if __name__ == "__main__":
    main()
