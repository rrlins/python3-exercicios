# Desafio 021 - Faça um program em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('/home/ross/Downloads/ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
