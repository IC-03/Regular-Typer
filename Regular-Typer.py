import sys
from typing import KeysView
import pygame
import tkinter
from tkinter import font
import random
pygame.init()

#def mainMenu():

#def tutorial();

def words(x,y):
  n = random.randint(x,y)
  m = random.randint(x,y)
  o = random.randint(x,y)
  p = random.randint(x,y)

  w = ('r' * n ) + ('l' * m ) + ('r' * o ) + ('l' * p)
  return w.upper()

def play():
    countLevel = 1
    wordsCorrect = 0
    #lifePlayer = 3
    PlayerAnswer = ''
    a = 0
    b = 2
    pygame.display.set_caption("Regular-Typer")
    size = 1000,600
    screen = pygame.display.set_mode(size)
    white = 255,255,255 
    miFuente = pygame.font.Font('Pixel_Font.ttf',25)
    Titulo = miFuente.render("{Regular-Typer}",True,(50,70,80))
    correctas = miFuente.render("Palabras correctas: "+repr(wordsCorrect),True,(50,70,80))
    nivel = miFuente.render("Nivel: "+repr(countLevel),True,(50,70,80))
    creditos = miFuente.render("Creado por Isabella Callejas, Angel Ortega y Juan Sepulveda",True,(50,70,80))
    texto = ""
    playerAnswer = ""
    screen.fill(white) #Background
    screen.blit(Titulo,(330,50))
    screen.blit(correctas,(330,80))
    screen.blit(creditos,(10,570))
    while True:
        while countLevel <= 2:
            screen.blit(nivel,(330,110))
            z=""
            z = words(a,b)
            z = z[ : 2]
            palabra = miFuente.render("palabra a digitar: "+repr(z),False,(50,70,80))
            screen.blit(palabra,(330,140))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        texto += "L"
                    if event.key == pygame.K_RIGHT:
                        texto += "R"
                    if event.key == pygame.K_RETURN: #Para enviar palabra
                        playerAnswer= texto
                        if playerAnswer == z:
                            wordsCorrect+=1
                            correctas = miFuente.render("Palabras correctas: "+repr(wordsCorrect),True,(50,70,80))
                            screen.blit(correctas,(330,80))
                            if wordsCorrect == 3:
                                a+=1
                                b+=1
                                wordsCorrect=0
                                countLevel+=1
                        else:
                            perder = miFuente.render("The game is over, you lose :(, palabras correctas: "+repr(wordsCorrect),True,(50,70,80))
                            screen.blit(perder,(330,400))
                            countLevel = 5
                        texto = ""
                    if event.key == pygame.K_BACKSPACE: #Para borrar
                        texto = texto[:-1]
                    '''if event.key == pygame.K_ESCAPE:
                        mainMenu()'''
                if countLevel == 4:
                    ganar = miFuente.render("The game is over, you win :D, palabras correctas: "+repr(wordsCorrect),True,(50,70,80))
                    screen.blit(ganar,(330,400))
            user_txt = miFuente.render(texto,True,(50,70,80))
            screen.blit(user_txt,(330,200))
            pygame.display.flip()


play()


#Para pasar de nivel necesitas escribir bien consecutivamente 3 palabras!
def niveles():
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
