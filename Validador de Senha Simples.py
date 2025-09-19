senha = 1234

s1 = int(input("Digite a senha: "))

while s1 != senha:
    print ("Senha incorreta! Tente novamente")
    s1 = int(input("Digite a senha: "))
print ("Acesso permitido!")