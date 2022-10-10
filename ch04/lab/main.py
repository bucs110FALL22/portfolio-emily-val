import pygame
import random

pygame.init()
screen = pygame.display.set_mode()
width, height = pygame.display.get_window_size()

pygame.draw.line(screen, (255, 255, 255), (0, height/2), (width, height/2))
pygame.draw.line(screen, (255, 255, 255), (width/2, 0), (width/2, height))
pygame.draw.circle(screen, (255, 255, 255), (0, 0), height/2)
