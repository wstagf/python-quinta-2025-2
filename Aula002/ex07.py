ladoA = int(input("Digite o lado a"))
ladoB = int(input("Digite o lado b"))
ladoC = int(input("Digite o lado c"))


if(ladoA == ladoB and ladoA == ladoC ):
    print("equilatero")
else:
    if(ladoA == ladoB and ladoA != ladoC ):
        print("isceles")
    else:
        print("escaleno")