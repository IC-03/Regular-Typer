import sys
from typing import KeysView
import pygame
import tkinter
from tkinter import font
import random
pygame.init()

#def mainMenu():

#def tutorial();

def play():
    pygame.display.set_caption("Regular-Typer")

    size = 800,600
    screen = pygame.display.set_mode(size)
    white = 255,255,255 
    miFuente = pygame.font.Font('Pixel_Font.ttf',25)
    Titulo = miFuente.render("{Regular-Typer}",True,(50,70,80))
    creditos = miFuente.render("Creado por Isabella Callejas, Angel Ortega y Juan Sepulveda",True,(50,70,80))
    texto = ""
    
    while True:
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
                    texto = ""
                if event.key == pygame.K_BACKSPACE: #Para borrar
                    texto = texto[:-1]
                '''if event.key == pygame.K_ESCAPE:
                    mainMenu()'''

        screen.fill(white) #Background
        screen.blit(Titulo,(330,50))
        screen.blit(creditos,(10,570))
        user_txt = miFuente.render(texto,True,(50,70,80))
        screen.blit(user_txt,(330,100))
        pygame.display.flip()

play()