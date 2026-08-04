senha = "1234"
tentativa = ""

# Enquanto a tentativa for diferente da senha correta, o loop continua
while tentativa != senha:
    tentativa = input("Digite sua senha: ")
    
    if tentativa != senha:
        print("Senha incorreta! Tente novamente.")

print("Acesso liberado!")

