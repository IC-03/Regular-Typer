
import sys
from typing import KeysView
import pygame
import tkinter
from tkinter import font
pygame.init()

size = 800,600
screen = pygame.display.set_mode(size)
white = 255,255,255 
pygame.display.set_caption("Regular-Typer")
miFuente = pygame.font.Font(None,30)
miTexto = miFuente.render("Regular-Typer",True,(50,70,80))
creditos = miFuente.render("Creado por Isabella Callejas, Angel Ortega y Juan Sepulveda",True,(50,70,80))
texto = ""
run= True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                texto += "I"
            if event.key == pygame.K_RIGHT:
                texto += "R"
            if event.key == pygame.K_RETURN:
                texto = ""

    screen.fill(white)
    screen.blit(miTexto,(330,50))
    screen.blit(creditos,(0,575))
    miletra = miFuente.render(texto,True,(50,70,80))
    screen.blit(miletra,(330,100))
    pygame.display.flip()
pygame.quit()