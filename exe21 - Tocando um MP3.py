#Faça um prog que abra e reproduza o áudio de um aquivo MP3
import pygame

pygame.init()
pygame.mixer.music.load('exe21.mp3')
pygame.mixer.music.play()
pygame.event.wait()


