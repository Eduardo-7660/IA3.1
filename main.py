import random as rand
import numpy as np

#gera a tabela pai:
def rng():
 for l in range(0, nLinhas):
     c = 0
     for c in range(0, tamanho):
         rRandom = rand.randint(1, tamanho)
         while (rRandom in matrixPai[l]):
             rRandom = rand.randint(1, tamanho)
         matrixPai[l][c] = rRandom

#cada par de filhos sera gerado aqui
def calculoPares():
 numMeio = int
 if tamanho % 2 == 1:
     numMeio = tamanho / 2 + 1
     numMeio = int(numMeio)
 else:
     numMeio = tamanho / 2
     numMeio = int(numMeio)

 # passa a primeira metade da lista á lista dos filhos
 for auxiliar in range(0, numMeio):
     listaFilho2.append(matrixPai[alcance - 1][auxiliar])
     listaFilho1.append(matrixPai[alcance][auxiliar])
 Auxi1 = []
 Auxi2 = []

 # segunda metade
 for auxiliar2 in range(numMeio, tamanho):
     Auxi2.append(matrixPai[alcance][auxiliar2])
     Auxi1.append(matrixPai[alcance+1][auxiliar2])

 for auxiliar3 in range(0, len(Auxi2)):

     if Auxi2[auxiliar3] in listaFilho2:
         rRandom = rand.randint(1, tamanho)
         while (rRandom in listaFilho2 or rRandom in Auxi2):
             rRandom = rand.randint(1, tamanho)
         listaFilho2.append(rRandom)

     else:
         listaFilho2.append(Auxi2[auxiliar3])

     if Auxi1[auxiliar3] in listaFilho1:
         rRandom = rand.randint(1, tamanho)
         while (rRandom in listaFilho1 or rRandom in Auxi1):
             rRandom = rand.randint(1, tamanho)
         listaFilho1.append(rRandom)

     else:
         listaFilho1.append(Auxi1[auxiliar3])

#calculo de distancia percorrida
def calcRoute1():
   somaTotal1 = 0

   for i in range(0, tamanho):
       if i >= tamanho-1:
           primeiro1 = listaFilho1[0]
           segundo1 = listaFilho1[-1]
       else:
           primeiro1 = listaFilho1[i]
           segundo1 = listaFilho1[i + 1]

       if matrixDistancia[primeiro1 - 1][segundo1 - 1] != 0:
           somaTotal1 += matrixDistancia[primeiro1 - 1][segundo1 - 1]
       else:
           somaTotal1 += matrixDistancia[segundo1 - 1][primeiro1 - 1]
   return somaTotal1

def calcRoute2():
   somaTotal2 = 0
   for k in range(0, tamanho):
       if k >= tamanho-1:
           primeiro2 = listaFilho2[0]
           segundo2 = listaFilho2[-1]
       else:
           primeiro2 = listaFilho2[k]
           segundo2 = listaFilho2[k + 1]

       if matrixDistancia[primeiro2 - 1][segundo2 - 1] != 0:
           somaTotal2 += matrixDistancia[primeiro2 - 1][segundo2 - 1]
       else:
           somaTotal2 += matrixDistancia[segundo2 - 1][primeiro2 - 1]
   return somaTotal2

def guardarFilhos():
   for l in range(ref2, ref3):
       for c in range(0, tamanho):
           if ref2 == nLinhas-2:
               matrixFilho[nLinhas-1][c] = listaFilho1.pop(0)
               matrixFilho[0][c] = listaFilho2.pop(0)

           else:
               matrixFilho[l + 1][c] = listaFilho1.pop(0)
               matrixFilho[l + 2][c] = listaFilho2.pop(0)

def mutacao():
    localMutante = rand.randint(0, tamanho-1)
    mutante = listaFilho1.pop(localMutante)
    listaFilho1.append(mutante)
    mutante = listaFilho2.pop(localMutante)
    listaFilho2.append(mutante)


def envelhecer():
   for l in range(0, nLinhas):
       for c in range(0, tamanho):
           matrixPai[l][c] = matrixFilho[l][c]


listaListaDistancia = []
arquivo = open("arquivoParaLer/distancia.txt", 'r')
for line in arquivo:
   line = line.strip()
   line = line.split(';')
   line.pop()
   line = list(map(int, line))
   listaListaDistancia.append(line)

# preenchimento da tabela distancia


nLinhas = 100

for variavel in range(0, len(listaListaDistancia)):
   listaDistancia = listaListaDistancia.pop(0)
   tamanho = listaDistancia.pop(0)
   #inicia matrizes
   matrixDistancia = np.zeros((tamanho, tamanho), dtype=int)
   matrixPai = np.zeros((nLinhas, tamanho), dtype=int)
   matrixFilho = np.zeros((nLinhas, tamanho), dtype=int)
   #inicia listas paternas
   listaPai1 = []
   listaPai2 = []
   #inicia listas dos filhos
   listaFilho1 = []
   listaFilho2 = []
   #demais variaveis globais
   somaTotal1 = 0
   somaTotal2 = 0
   verif = 0
   menorValorLista = 0
   menorRotaLista = []
   menorValor = 0
   menorRota = []
   ref2 = 0
   ref3 = 1
   ref0 = 0
   nLista = []
   for i in range(0, tamanho):
       for j in range(0, tamanho):
           if i == j or i > j:
               matrixDistancia[i][j] = 0
           else:
               matrixDistancia[i][j] = listaDistancia.pop(0)
# gero os pais primeiramente
   rng()
   print(matrixDistancia)
   while verif < 1000:
       tamPopulação = int(nLinhas/2)
       for alcance in range(0, tamPopulação):
           # CALCULA PARES
           calculoPares()
           #VALORES DAS ROTAS
           comparar1 = calcRoute1()
           comparar2 = calcRoute2()

           fazerMutacao = rand.randint(1, 100)
           if fazerMutacao <= 5: #taxa de mutação
               if verif == 1:
                   mutacao()


           # 1 rodada de graça
           if alcance == 0 and verif == 0:
               if comparar1 > comparar2:
                   menorRotaLista = listaFilho1.copy()
                   menorValorLista = comparar1
                   verif = 1
               else:
                   menorRotaLista = listaFilho2.copy()
                   menorValorLista = comparar2
                   verif = 1

           elif alcance != 0:
               if comparar1 < menorValorLista:
                   menorRotaLista = listaFilho1.copy()
                   menorValorLista = comparar1
                   verif = 1
               elif comparar2 < menorValorLista:
                   menorRotaLista = listaFilho2.copy()
                   menorValorLista = comparar2
                   verif = 1


           #guarda filhos
           guardarFilhos()
           ref0 += 2
           ref2 += 2
           ref3 += 2

           #escopo do for
       # escopo do verificar com a do pai
       if menorValor == 0:
           menorRota = menorRotaLista.copy()
           menorValor = menorValorLista
       elif menorValor != 0 and menorValorLista < menorValor:
            menorRota = menorRotaLista.copy()
            menorValor = menorValorLista
            verif = 1
       elif menorValorLista >= menorValor:
            verif += 1
       envelhecer()

       ref2 = 0
       ref3 = 1
       ref0 = 0
   print("\nMelhor rota: ", menorRota,"\nMelhorValor: ", menorValor, "\n")


