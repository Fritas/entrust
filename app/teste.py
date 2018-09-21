entrada = 1
while entrada != 0:
    try:
        entrada = int(input("Entre com um número: "))
    except ValueError as error:
        print(error)
    else:
        print("É um número: ", entrada)
