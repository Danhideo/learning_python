from back import *

def main():
    saldo = 100
    while saldo > 0:
        
        action = int(input("O que você gostaria de fazer? 1 para Jogar/2 para ver credito e 3 para Sacar e Parar : "))

        match action:
            case 1:
                saldo = saldo - 10
                ponto = 0
                resultado,possibilidade = girar()
                for i in range(3):
                    print(resultado[i])
                print("-------------------------------")      


                ponto = verificar(possibilidade)
                print(ponto)
                if ponto == 0:
                    print("Você perdeu! ")
                    print(saldo)
                    if saldo == 10:
                        print("Acabou seu crédito, Bye Bye")
                else:
                    print("Você venceu!")
                    saldo = saldo + 20*ponto
                    print(saldo)     
            case 2:
                print(saldo())
            case 3:
                break    

if __name__ == "__main__":
    main()