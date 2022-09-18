import sys
from typing import KeysView
import pygame
import tkinter
from tkinter import font
import random
import time
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
    salir = miFuente.render('Presione: "Enter" para salir',True,(50,70,80))
    wordsCorrectAcum=0
    texto = ""
    z=""
    playerAnswer = ""
    mostrar = True
    screen.fill(white) #Background
    screen.blit(Titulo,(330,50))
    screen.blit(correctas,(330,80))
    screen.blit(creditos,(10,570))
    while True:
        while countLevel <= 2:
            screen.blit(nivel,(330,110))
            if mostrar:
                z = words(a,b)
                palabra = miFuente.render("palabra a digitar: "+repr(z),False,(50,70,80))
                screen.blit(palabra,(330,140))
                mostrar = False
                pygame.display.update() 
                pygame.display.flip()
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
                        mostrar = True
                        texto=""
                        if playerAnswer == z:
                            wordsCorrect+=1
                            wordsCorrectAcum+=1
                            correctas = miFuente.render("Palabras correctas: "+repr(wordsCorrect),True,(50,70,80))
                            screen.fill(white) #Background
                            screen.blit(correctas,(330,80))
                            screen.blit(Titulo,(330,50))
                            screen.blit(correctas,(330,80))
                            screen.blit(creditos,(10,570))
                            if wordsCorrect == 3:
                                a+=1
                                b+=1
                                wordsCorrect=0
                                correctas = miFuente.render("Palabras correctas: "+repr(wordsCorrect),True,(50,70,80))
                                screen.blit(correctas,(330,80))
                                countLevel+=1
                                nivel = miFuente.render("Nivel: "+repr(countLevel),True,(50,70,80))
                                screen.blit(nivel,(330,110))
                        else:
                            perder = miFuente.render("The game is over, you lose :(, palabras correctas: "+repr(wordsCorrectAcum),True,(50,70,80))
                            screen.blit(perder,(200,400))
                            screen.blit(salir,(200,500))
                            pygame.display.flip()   

                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT: 
                                        pygame.quit()
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_RETURN:
                                            pygame.quit()
                if countLevel == 3:
                    ganar = miFuente.render("The game is over, you win :D, palabras correctas: "+repr(wordsCorrectAcum),True,(50,70,80))
                    screen.blit(ganar,(200,400))
                    screen.blit(salir,(200,500))
                    pygame.display.flip()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT: 
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    pygame.quit()
            user_txt = miFuente.render(texto,True,(50,70,80))
            screen.blit(user_txt,(330,200))
            pygame.display.flip()
play()
