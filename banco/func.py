def mostrar_saldo(saldo):
    print(f"O seu saldo é de {saldo:.2f}")

def sacar(saldo):
    try: 
        saque = float(input("Quanto você gostaria de sacar?: "))
    except ValueError:
        print("O valor que você colocou não é um número! ")
        return 0 
    
    if saque>saldo:
        print("Você não tem saldo o suficiente! ")
        return 0
    elif saque<0:
        print("o valor nao pode ser negativo! ")
        return 0
    else:
        print(f"você sacou o valor de R${saque:.2f}, seu saldo atual é de {saldo - saque = :.2f} ")
        return saque
    

def depositar(saldo):
    try:
        deposito = float(input("Insira quanto você gostaria de depositar: "))
    except ValueError:
        print("O valor que você colocou não é um número! ")
        return 0
    if deposito<0:
        print("o valor nao pode ser negativo! ")
        return 0
    else:
        final = saldo+deposito
        print(f"Você depositou {deposito:.2f} e o valor do seu saldo final é de {final:.2f} ")
        return deposito
    