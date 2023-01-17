import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#utilizando a biblioteca pygame é possivel reproduzir musicas e/ou imagens.
#para o pygame é necessario iniciar o mixer e o pygame

import playsound
playsound.playsound('/home/guilherme/Documentos/ex21.mp3')
playsound.playsound.stop

#é possivel utilizar ainda a biblioteca playsound
