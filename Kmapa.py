
###Rodou###

from random import randint

tab = [['0', '0', '0', '0'], ['0', '0', '0', '0']]


def gerarUns():
   qntUns = randint(1, 8)
   while qntUns > 0:
       linha = randint(0, 1)
       col = randint(0, 3)

       # verificar se a linha já está ocupada
       if tab[linha][col] == '0':
           tab[linha][col] = '1'
       qntUns -= 1


def inicializar():
   tab = [['0', '0', '0', '0'], ['0', '0', '0', '0']]
   gerarUns()


# imprimir o mapa
def imprimir():
   print('Mapa de Karnaugh')
   for linha in tab:
       print('\n---------------')
       for coluna in linha:
           print(coluna, end=' | ')
   print('\n---------------')


# verificar a quantidade de grupos fornecidos pelo usuário
def verificar():
   usuario = int(input('Quanto(s) grupo(s) tem o mapa acima? '))

   posicoes = set()  # variável que armazena as posições dos '1'.


   # posições dos agrupamentos
   ###Grupo com 8###
   ABCabc = {(0, 0), (0, 1), (1, 0), (1, 1), (0, 2), (1, 2), (0, 3), (1, 3)}
   
   ###Grupos com 4###
   abcBC = {(0, 0), (0, 1), (0, 2), (0, 3)}
   AbcBC = {(1, 0), (1, 1), (1, 2), (1, 3)}
   AabcC = {(0, 0), (0, 1), (1, 0), (1, 1)}
   AabBC = {(0, 1), (0, 2), (1, 1), (1, 2)}
   AaBCc = {(0, 2), (0, 3), (1, 2), (1, 3)}
   AabBc = {(0, 0), (1, 0), (0, 3), (1, 3)}

   ###Grupos com 2###
   abcC = {(0, 0), (0, 1)}#1
   abBC = {(0, 1), (0, 2)}#2
   aBCc = {(0, 2), (0, 3)}#3
   abcB = {(0, 0), (0, 3)}#4
   AbcC = {(1, 0), (1, 1)}#5
   AbBC = {(1, 1), (1, 2)}#6
   ABCc = {(1, 2), (1, 3)}#7
   AbBc = {(1, 0), (1, 3)}#8
   Aabc = {(0, 0), (1, 0)}#9
   AabC = {(0, 1), (1, 1)}#10
   AaBC = {(0, 2), (1, 2)}#11
   AaBc = {(0, 3), (1, 3)}#12

   ###Grupos com 1###
   abc = {(0, 0)}
   abC = {(0, 1)}
   aBC = {(0, 2)}
   aBc = {(0, 3)}
   Abc = {(1, 0)}
   AbC = {(1, 1)}
   ABC = {(1, 2)}
   ABc = {(1, 3)}



   pos_achado = set()    

   i = 0
   while i < 2: #i = linha
      j = 0
      while j < 4: #j = coluna
         if tab[i][j] == '1':
            posicoes.add((i, j))
         j += 1
      i += 1

       # verificar qual é a combinação feita.#
       #issubset = se um conjunto é subconjunto de outro#
       #issuperset = se um conjunto é superconjunto de outro#
          
      cont = 0
          
          ###Grupo com 8###
      if posicoes.issuperset(ABCabc) and pos_achado.issuperset(ABCabc) == True:
         pos_achado.update(ABCabc)#ABCabc
         cont += 1
              
              
          ###Grupos com 4###
      if posicoes.issuperset(abcBC) and pos_achado.issuperset(abcBC) == True:
         pos_achado.update(abcBC)#abcBC
         cont += 1          
      if posicoes.issuperset(AbcBC) and pos_achado.issuperset(AbcBC) == True:
         pos_achado.update(AbcBC)#AbcBC
         cont += 1
      if posicoes.issuperset(AabcC) and pos_achado.issuperset(AabcC) == True:
         pos_achado.update(AabcC)#AabcC
         cont += 1
      if posicoes.issuperset(AabBC) and pos_achado.issuperset(AabBC) == True:
         pos_achado.update(AabBC)#AabBC
         cont += 1
      if posicoes.issuperset(AaBCc) and pos_achado.issuperset(AaBCc) == True:
         pos_achado.update(AaBCc)#AaBCc
         cont += 1
      if posicoes.issuperset(AabBc) and pos_achado.issuperset(AabBc) == True:
         pos_achado.update(AabBc)#AabBc
         cont += 1
              
          ###Grupos com 2###
      if posicoes.issuperset(abcC) and pos_achado.issuperset(abcC) == True:
         pos_achado.update(abcC)#abcC 1
         cont += 1
      if posicoes.issuperset(abBC) and pos_achado.issuperset(abBC) == True:
         pos_achado.update(abBC)#abBC 2
         cont += 1
      if posicoes.issuperset(aBCc) and pos_achado.issuperset(aBCc) == True:
         pos_achado.update(aBCc)#aBCc 3
         cont += 1
      if posicoes.issuperset(abcB) and pos_achado.issuperset(abcB) == True:
         pos_achado.update(abcB)#abcB 4
         cont += 1
      if posicoes.issuperset(AbcC) and pos_achado.issuperset(AbcC) == True:
         pos_achado.update(AbcC)#AbcC 5
         cont += 1
      if posicoes.issuperset(AbBC) and pos_achado.issuperset(AbBC) == True:
         pos_achado.update(AbBC)#AbBC 6
         cont += 1
      if posicoes.issuperset(ABCc) and pos_achado.issuperset(ABCc) == True:
         pos_achado.update(ABCc)#ABCc 7
         cont += 1
      if posicoes.issuperset(AbBc) and pos_achado.issuperset(AbBc) == True:
         pos_achado.update(AbBc)#AbBc 8
         cont += 1
      if posicoes.issuperset(Aabc) and pos_achado.issuperset(Aabc) == True:
         pos_achado.update(Aabc)#Aabc 9
         cont += 1
      if posicoes.issuperset(AabC) and pos_achado.issuperset(AabC) == True:
         pos_achado.update(AabC)#AabC 10
         cont += 1
      if posicoes.issuperset(AaBC) and pos_achado.issuperset(AaBC) == True:
         pos_achado.update(AaBC)#AaBC 11
         cont += 1
      if posicoes.issuperset(AaBc) and pos_achado.issuperset(AaBc) == True:
         pos_achado.update(AaBc)#AaBc 12
         cont += 1
              
          ###Grupos com 1###
      if posicoes.issuperset(abc) and pos_achado.isdisjoint(abc) == True:
         pos_achado.update(abc)#1
         cont += 1
      if posicoes.issuperset(abC) and pos_achado.isdisjoint(abC) == True:
         pos_achado.update(abC)#2
         cont += 1
      if posicoes.issuperset(aBC) and pos_achado.isdisjoint(aBC) == True:
         pos_achado.update(aBC)#3
         cont += 1
      if posicoes.issuperset(aBc) and pos_achado.isdisjoint(aBc) == True:
         pos_achado.update(aBc)#4
         cont += 1
      if posicoes.issuperset(Abc) and pos_achado.isdisjoint(Abc) == True:
         pos_achado.update(Abc)#5
         cont += 1
      if posicoes.issuperset(AbC) and pos_achado.isdisjoint(AbC) == True:
         pos_achado.update(AbC)#6
         cont += 1
      if posicoes.issuperset(ABC) and pos_achado.isdisjoint(ABC) == True:
         pos_achado.update(ABC)#7
         cont += 1
      if posicoes.issuperset(ABc) and pos_achado.isdisjoint(ABc) == True:
         pos_achado.update(ABc)#8
         cont += 1
         
   print (f'grupo de 8 - 1  {posicoes.issuperset(ABCabc)}{pos_achado.issuperset(ABCabc)}')        
   print (f'grupos de 4 - 1  {posicoes.issuperset(abcBC)}{pos_achado.issuperset(abcBC)}')
   print (f'grupos de 4 - 2  {posicoes.issuperset(AbcBC)}{pos_achado.issuperset(AbcBC)}')
   print (f'grupos de 4 - 3  {posicoes.issuperset(AabcC)}{pos_achado.issuperset(AabcC)}')
   print (f'grupos de 4 - 4  {posicoes.issuperset(AabBC)}{pos_achado.issuperset(AabBC)}')
   print (f'grupos de 4 - 5  {posicoes.issuperset(AaBCc)}{pos_achado.issuperset(AaBCc)}')
   print (f'grupos de 4 - 6  {posicoes.issuperset(AabBc)}{pos_achado.issuperset(AabBc)}')
   print (f'grupos de 2 - 1  {posicoes.issuperset(abcC)}{pos_achado.issuperset(abcC)}')
   print (f'grupos de 2 - 2  {posicoes.issuperset(abBC)}{pos_achado.issuperset(abBC)}')
   print (f'grupos de 2 - 3  {posicoes.issuperset(aBCc)}{pos_achado.issuperset(aBCc)}')
   print (f'grupos de 2 - 4  {posicoes.issuperset(abcB)}{pos_achado.issuperset(abcB)}')
   print (f'grupos de 2 - 5  {posicoes.issuperset(AbcC)}{pos_achado.issuperset(AbcC)}')
   print (f'grupos de 2 - 6  {posicoes.issuperset(AbBC)}{pos_achado.issuperset(AbBC)}')
   print (f'grupos de 2 - 7  {posicoes.issuperset(ABCc)}{pos_achado.issuperset(ABCc)}')
   print (f'grupos de 2 - 8  {posicoes.issuperset(AbBc)}{pos_achado.issuperset(AbBc)}')
   print (f'grupos de 2 - 9  {posicoes.issuperset(Aabc)}{pos_achado.issuperset(Aabc)}')
   print (f'grupos de 2 - 10 {posicoes.issuperset(AabC)}{pos_achado.issuperset(AabC)}')
   print (f'grupos de 2 - 11 {posicoes.issuperset(AaBC)}{pos_achado.issuperset(AaBC)}')
   print (f'grupos de 2 - 12 {posicoes.issuperset(AaBc)}{pos_achado.issuperset(AaBc)}')
   print (f'grupos de 1 - 1  {posicoes.issuperset(abc)}{pos_achado.isdisjoint(abc)}')
   print (f'grupos de 1 - 2  {posicoes.issuperset(abC)}{pos_achado.isdisjoint(abC)}')
   print (f'grupos de 1 - 3  {posicoes.issuperset(aBC)}{pos_achado.isdisjoint(aBC)}')
   print (f'grupos de 1 - 4  {posicoes.issuperset(aBc)}{pos_achado.isdisjoint(aBc)}')
   print (f'grupos de 1 - 5  {posicoes.issuperset(Abc)}{pos_achado.isdisjoint(Abc)}')
   print (f'grupos de 1 - 6  {posicoes.issuperset(AbC)}{pos_achado.isdisjoint(AbC)}')
   print (f'grupos de 1 - 7  {posicoes.issuperset(ABC)}{pos_achado.isdisjoint(ABC)}')
   print (f'grupos de 1 - 8  {posicoes.issuperset(ABc)}{pos_achado.isdisjoint(ABc)}')



   print (f'posições = {posicoes}')
   print (f'Quantidade de grupos achados = {cont}')
   print (f'Grupos achados = {pos_achado}')
   if usuario == cont:
       print (f'Acertou.')
   else:
       print ('Errou, tente novamente.')
       return verificar()

# programa principal
if __name__ == '__main__':
   inicializar()
   imprimir()
   verificar()

