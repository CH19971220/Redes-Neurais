import numpy as np
from random import uniform, randint
arq = open("iris.txt", "r")

dados = []
classe = []
dados = [val.split(",")[0:-1] for val in arq]
dados = [[float(x) for x in line] for line in dados]
arq.seek(0)
classe = [val.rstrip('\n')[-1] for val in arq]
classe = [int(val) for val in classe]
alfa = 0.4
quant_Treinamento = 500
peso = [uniform(-1,1) for x in range(5)]
print("Pesos Iniciais: ", peso)
for i in range(len(classe)):    
    if(classe[i] != 1):        
        classe[i] = -1

for t in range(quant_Treinamento):
        c = randint(0, 149)
        y=0
        entrada = [dados[c][e] for e in range(4)]
        entrada.append(1)
        se = classe[c]

        for i in range(len(peso)):
                y += entrada[i] * peso[i]
        #Função degrau
        if y >= 0:
                sr = 1
        else:
                sr = -1
        if sr != se:
                peso = [peso[x] + alfa * (se - sr) * entrada[x] for x in range(len(peso))]
                
        

# Fim

acerto = 0
for c in range(150):
        y=0
        entrada = [dados[c][e] for e in range(4)]
        entrada.append(1)
        se = classe[c]

        for i in range(len(peso)):
                y += entrada[i] * peso[i]
        #Função degrau
        if y >= 0:
                sr = 1
        else:
                sr = -1
        if sr == se:
               acerto += 1            

print("\nPesos Finais: ", peso)
print("\nTaxa de Acerto: ", 100*acerto/150)
print("\nQuantidade de Treinamentos:", quant_Treinamento)


