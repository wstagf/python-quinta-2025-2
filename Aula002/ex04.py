# Tendo como dado de entrada a altura (h) de uma pessoa e seu sexo, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


altura = float(input("Digite sua altura em metros ex. 1.75: "))
sexo = input("M para masculino e F para feminino: ")

if (sexo == "M" or sexo == "m"):
    pesoideal =  (72.7*altura) - 58
    print(f"Seu peso ideal é {pesoideal:.2f}")
else:
    pesoideal =  (62.1*altura) - 44.7
    print(f"Seu peso ideal é {pesoideal:.2f}")