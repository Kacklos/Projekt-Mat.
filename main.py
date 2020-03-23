import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QGridLayout, QSlider, QHBoxLayout, QVBoxLayout
import pygame
from pygame.locals import QUIT

pygame.font.init()
font36 = pygame.font.SysFont("Arial", 36)
font18 = pygame.font.SysFont("Arial", 18)
'''
    def pyg(self):
        b1 = pygame.Rect(200, 400, 100, 100)
        b2 = pygame.Rect(500, 400, 100, 100)
        b1_vel = 0.0
        temp1 = 200
        temp2 = 500
        b2_vel = -1
        
        b1_mass = 1.0
        b2_mass = self.mass
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((800,600))
        collision_counter = 0

        while True:
            #Events
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
            
            # Sprawdzanie kolizji
            if b1.colliderect(b2) or b1.x >= b2.x+100:
                if self.mass == 1:
                    b1_vel, b2_vel = b2_vel, b1_vel
                else:
                    b2_vel = b2_vel*(b2_mass - b1_mass)/(b2_mass + b1_mass) + b1_vel*2*b1_mass/(b2_mass+b1_mass)
                    b1_vel = b2_vel*2*b2_mass/(b2_mass+b1_mass) + b1_vel*(b1_mass-b2_mass)/(b1_mass+b2_mass)
                
                # Przesunięcie po odbiciu
                if self.mass <1000:
                    temp2 += 1
                else:
                    # W celu przyspieszenia oraz większej dokładności całości dałem mniejsze przesunięcie
                    temp2 += 0.1
                collision_counter +=1
            
            # Kolizja ze ścianą
            if b1.collidepoint((0,450)) or b1.x <0:
                b1_vel = -1*b1_vel
                collision_counter +=1
                temp1 +=0.1

            print(b2.x)
            # Ruch # Bez użycia pomocniczych zmiennych pygame wariował
            temp1 += b1_vel
            temp2 += b2_vel
            b1.x = temp1
            b2.x = temp2

            # Wyświetlanie
            screen.fill((48, 48, 48))
            pygame.draw.line(screen, (20,20,20), (0,505), (800,505), 5)
            pygame.draw.rect(screen, (100,100,255), b1)
            pygame.draw.rect(screen, (100,255,100), b2)

            if b1.x >800:
                tri1 = (b1.x - 800)//100
                pygame.draw.polygon(screen, (100, 100, 255), [(800, 500-tri1), (750, 475-tri1), (750, 525-tri1)])
            if b2.x > 800:
                tri2 = (b2.x - 800)//100
                pygame.draw.polygon(screen, (100, 255, 100), [(800, 500-tri2), (750, 475-tri2), (750, 525-tri2)])
            
            screen.blit(font36.render(str(collision_counter), False, (255, 255, 255)), (600, 50))
            screen.blit(font18.render("Prędkość 1: %.4f" %b1_vel , False, (100, 100, 255)), (20, 50))
            screen.blit(font18.render("Prędkość 2: %.4f" %b2_vel, False, (100, 255, 100)), (20,80))
            pygame.display.update()  
            clock.tick()
'''
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Slider"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 200
        self.mass = 0
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(4)
        self.slider.valueChanged.connect(self.set_mass)
        
        self.l1 = QLabel("0")
        self.l1.setFont(QtGui.QFont("Sanserif", 12))

        btn1 = QPushButton("Oblicz")
        l2 = QLabel("Masa 1:")
        l2.setFont(QtGui.QFont("Sanserif", 12))
        l3 = QLabel("Masa 2:")
        l3.setFont(QtGui.QFont("Sanserif", 12))
        l4 = QLabel("1")
        l4.setFont(QtGui.QFont("Sanserif", 12))
        
        hb1 = QHBoxLayout()
        hb1.addWidget(l2)
        hb1.addWidget(l4)
        hb2 = QHBoxLayout()
        hb2.addWidget(l3)
        hb2.addWidget(self.l1)

        vb = QVBoxLayout()
        vb.addLayout(hb1)
        vb.addLayout(hb2)
        vb.addWidget(self.slider)
        vb.addWidget(btn1)
        
        self.setLayout(vb)
        self.show()
 
    def set_mass(self):
        self.mass = pow(100, self.slider.value())
        self.l1.setText(str(self.mass))
 
    def oblicz(self):
        pass

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())