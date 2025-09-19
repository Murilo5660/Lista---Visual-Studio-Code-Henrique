numero = int(input("Digite um número para saber a tabuada: "))

print (f"\n--- Tabuada do número {numero} ---")
for multiplicador in range (1,11):
    resultado = numero * multiplicador
    print (f"{numero} x {multiplicador} = {resultado}")