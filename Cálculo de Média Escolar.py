a = float(input("Digite a 1° nota: "))
b = float(input("Digite a 2° nota: "))
c = float(input("Digite a 3° nota: "))

media = (a + b +c) / 3

print(f"\nMédia final: {media}")

if media >=7.0:
    print ("Aprovado!")
elif media >=5.0:
    print ("Recuperação")
else:
    print ("Reprovado!")