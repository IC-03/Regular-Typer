import random
def words(x,y):
  n = random.randint(x,y)
  m = random.randint(x,y)
  o = random.randint(x,y)
  p = random.randint(x,y)

  w = ('r' * n ) + ('l' * m ) + ('r' * o ) + ('l' * p)
  return w.upper()


#Para pasar de nivel necesitas escribir bien consecutivamente 3 palabras!
def niveles():
  countLevel = 1
  wordsCorrect = 0
  #lifePlayer = 3
  PlayerAnswer = ''
  a = 0
  b = 2
  print(f'Palabras correctas: {wordsCorrect}')
  
  while (countLevel <= 2):
    print('----------------------------------------------')
    #print(f'Rango random de las palabras a: {a}, b: {b}')
    print(f'Nivel: {countLevel}')

    z = words(a,b)
    print(f'Palabra a digitar: {z}')

    PlayerAnswer = input()

    #Verificamos que w jugador sea igual a w máquina para avanzar
    if (PlayerAnswer == z):
      wordsCorrect = wordsCorrect+1
  
      print(f'Palabras correctas: {wordsCorrect}') #1,2,3 -> 1,2,3

      #Tres palabras correctas -> Subes de nivel
      if (wordsCorrect == 3):
        a=a+1
        b=b+1
        wordsCorrect = 0
        countLevel=countLevel+1

    else:
      #El usuario se equivoca, por ende pierde y se debe salir del while
      print(f'The game is over, you lose :(, palabras correctas: {(countLevel - 1) * 3 + wordsCorrect}')
      #Cuenta las palabras correctas del nivel antes de equivocarse y añade las palabras correctas que hizo en el nivel
      countLevel = 4 #Para romper el while
  
  #Cuando terminas todos los niveles   
  print(f'The game is over, you win! /n Palabras escritas: {(countLevel - 1) * 3 + wordsCorrect}')