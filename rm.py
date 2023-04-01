# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:06:19 2023

@author: marti
"""

import pygame

# Inicializar pygame
pygame.init()

# Cargar archivo mp3
pygame.mixer.music.load('pollito.mp3')

# Reproducir archivo mp3
pygame.mixer.music.play()

# Esperar a que termine la canción
while pygame.mixer.music.get_busy():
    continue

# Detener pygame
pygame.quit()



# Detener pygame
pygame.quit()