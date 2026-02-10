from func import *

saldo = 1000
def main():
    global saldo
    rodando = True
    bem_vindo = True
    while rodando:
        if bem_vindo == True:
            acao=int(input("Bem-vindo ao Danbank. Por favor, insira a sua ação.:\n1 para ver seu saldo \n2 para sacar\n3 para depositar\n4 para sair\n Selecione a ação: "))

        else:
            acao=int(input("Por favor, insira a sua próxima ação.:\n1 para ver seu saldo \n2 para sacar\n3 para depositar\n4 para sair\n Selecione a ação: "))

        match acao:
            case 1:                
                mostrar_saldo(saldo)
                bem_vindo = False
                print("**************************")
                
            case 2:
                bem_vindo = False
                saldo -= sacar(saldo)
                print("**************************")
                
            case 3:
                bem_vindo = False
                saldo += depositar(saldo)
                print("**************************")
                
            case 4:
                print("Obrigado por utilizar o Danbank! Até a proxima :) ")
                rodando=False

if __name__=="__main__":
    main()
    