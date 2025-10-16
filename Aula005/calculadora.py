
# Termine a caluladora 

# Você recebeu essa calculadora e esta faltando partes. 
# Termine-a

# 1. Menus
# 2. Soma / Subtrcao / Divisao / Multiplicacao
# 3. Potenciacao / raiz / porcentagem
# 4. Histórico de cálculos
# 5. Mostrar as últimas operações realizadas e permitir repetir alguma delas.
# 6. Tratamento avançado de erros
# 7. Entrada inválida (ex: abc)
# 8. Tatar Divisão por zero 



def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def divisao(n1, n2):
    try:
        return n1 / n2
    except:
        print("Não é possivel dividir por zero")
    



def main():
    print("Esse sera a nossa calculadora, por enquanto ela so faz soma de dois numeros")
    n1 = float(input("Digite o valor 1: "))
    n2 = float(input("Digite o valor 2: "))
    total = soma(n1, n2)
    print(total)



if __name__ == "__main__":
    main()