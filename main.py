import sys
import pygame
from pygame.locals import QUIT

pygame.font.init()
font36 = pygame.font.SysFont("Arial", 36)
font18 = pygame.font.SysFont("Arial", 18)

class Oblicz(object):
    def __init__(self, mass):
        self.b1 = pygame.Rect(200, 400, 100, 100)
        self.b2 = pygame.Rect(500, 400, 100, 100)
        self.b1_vel = 0.0
        self.temp1 = 200
        self.temp2 = 500
        self.b2_vel = -1
        
        self.b1_mass = 1.0
        self.b2_mass = mass
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800,600))
        self.collision_counter = 0
    
    def oblicz(self):
        while True:
            #Events
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
            
            # Sprawdzanie kolizji
            if self.b1.colliderect(self.b2) or self.b1.x >= self.b2.x+100:
                if self.b2_mass == 1:
                    self.b1_vel, self.b2_vel = self.b2_vel, self.b1_vel
                else:
                    self.b2_vel = self.b2_vel*(self.b2_mass - self.b1_mass)/(self.b2_mass + self.b1_mass) + self.b1_vel*2*self.b1_mass/(self.b2_mass+self.b1_mass)
                    self.b1_vel = self.b2_vel*2*self.b2_mass/(self.b2_mass+self.b1_mass) + self.b1_vel*(self.b1_mass-self.b2_mass)/(self.b1_mass+self.b2_mass)
                
                # Przesunięcie po odbiciu
                if self.b2_mass <1000:
                    self.temp2 += 1
                else:
                    # W celu przyspieszenia oraz większej dokładności całości dałem mniejsze przesunięcie
                    self.temp2 += 0.1
                self.collision_counter +=1
            
            # Kolizja ze ścianą
            if self.b1.collidepoint((0,450)) or self.b1.x <0:
                self.b1_vel = -1*self.b1_vel
                self.collision_counter +=1
                self.temp1 +=0.1

            print(self.b2.x)
            # Ruch # Bez użycia pomocniczych zmiennych pygame wariował
            self.temp1 += self.b1_vel
            self.temp2 += self.b2_vel
            self.b1.x = self.temp1
            self.b2.x = self.temp2

            # Wyświetlanie
            self.screen.fill((48, 48, 48))
            pygame.draw.line(self.screen, (20,20,20), (0,505), (800,505), 5)
            pygame.draw.rect(self.screen, (100,100,255), self.b1)
            pygame.draw.rect(self.screen, (100,255,100), self.b2)

            if self.b1.x >800:
                tri1 = (self.b1.x - 800)//100
                pygame.draw.polygon(self.screen, (100, 100, 255), [(800, 500-tri1), (750, 475-tri1), (750, 525-tri1)])
            if self.b2.x > 800:
                tri2 = (self.b2.x - 800)//100
                pygame.draw.polygon(self.screen, (100, 255, 100), [(800, 500-tri2), (750, 475-tri2), (750, 525-tri2)])
            
            self.screen.blit(font36.render(str(self.collision_counter), False, (255, 255, 255)), (600, 50))
            self.screen.blit(font18.render("Prędkość 1: %.4f" %self.b1_vel , False, (100, 100, 255)), (20, 50))
            self.screen.blit(font18.render("Prędkość 2: %.4f" %self.b2_vel, False, (100, 255, 100)), (20,80))
            pygame.display.update()  
            self.clock.tick()