# Tkinter Implementation

import pygame
from math import *
import numpy as np
import random
pygame.init()

# CONSTANTS
R1 = 6
R2 = 10
K2 = 5
SCREEN_HEIGHT, SCREEN_WIDTH = (500, 500)
K1 = SCREEN_WIDTH*K2*3/(8*(R1+R2))
CENTER = (SCREEN_HEIGHT//2, SCREEN_WIDTH//2)
A = 0
B = 0

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

def draw(x, y):
    screen.fill("White", ((x, y), (1, 1)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear screen
    screen.fill((0, 0, 0))

    # Keeping A and B bounded
    if A != 2:
        A += 0.01
        B += 0.005
    else:
        A = 0
        B = 0

    # Precompute Common Expressions
    cosA, sinA = cos(A), sin(A)
    cosB, sinB = cos(B), sin(B)
    # Main Loop
    for theta in range(0, 360, 5):
        for phi in range(0, 720, 5):
            x = (R2+R1*cos(theta))*(cosB*cos(phi)+sinA*sinB*sin(phi))-R1*cosA*sinB*sin(theta)
            y = (R2+R1*cos(theta))*(cos(phi)*sinB-cosB*sinA*sin(phi))+R1*cosA*cosB*sin(theta)
            z = cosA*(R2+R1*cos(theta))*sin(phi)+R1*sinA*sin(theta) 
            x, y = x*K1/K2+z, y*K1/K2+z
            draw(x+CENTER[0], y+CENTER[1])

    pygame.display.update()

