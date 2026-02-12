import random
def girar():
    
    simbolo = ('1','2','3')
    linhas = [
        [],[],[]
        ]
    colunas = [[],[],[]]
    possibilidade = [linhas,colunas]
    for linha in range(3):
        for coluna in range(3):
            linhas[linha].append(random.choice(simbolo))
              
    for linha in range(3):
        for coluna in range(3):
            colunas[linha].append(linhas[coluna][linha])


    return linhas,possibilidade        

def verificar(possibilidade):
    ponto = 0
    for i in range(len(possibilidade)):            
            
        if len(set(possibilidade[i][0])) == 1:
            ponto += 1
        if len(set(possibilidade[i][1])) == 1:
            ponto += 1
        if len(set(possibilidade[i][2])) == 1:    
            ponto += 1
    return ponto

#possibilidade = [linhas = [[],[],[]],colunas = [[],[],[]]]