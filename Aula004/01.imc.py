# IMC = peso * (altua * altura)
# 
# 18.50 – 24.99: Peso Normal.
# 25.00 – 29.99: Pré-Obesidade.
# 30.00 – 34.99: Obesidade Grau I.
# 35.00 – 39.99: Obesidade Grau II.
# ≥40.00: Obesidade Grau III.

peso = float(input("Digite seu peso em kg: "))

altura = float(input("Digite seu altura em metros: "))

imc = peso / (altura * altura)


if imc < 18.5:
    print("Magro demais")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Pre Obesidade")
elif imc >= 30 and imc < 35:
    print("Obesidade grau 1")
elif imc >= 35 and imc < 40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")

print(imc)