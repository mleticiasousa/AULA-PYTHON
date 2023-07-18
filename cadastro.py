name = str(input("Digite seu nome: "))
nome = str(input("Digite seu sobrenome: "))
age = int(input("Idade: "))
nome = str(input("E-mail: "))
nome = int(input("Telefone: "))
nome = str(input("Deixe aqui sua sugestão: "))

def obter_nome():
    nome = input("Digite seu nome: ")
    return nome

def feedback_personalizado(name):
    return f"Olá, {name}! Obrigado por preencher o formulário."

def main():
    nome_usuario = obter_nome()
    feedback = feedback_personalizado(nome_usuario)
    print(feedback)

if __name__ == "__main__":
    main()

print( )
print("Cadastro realzizado com sucesso!")