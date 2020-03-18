import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QGridLayout
import pygame

pygame.font.init()
font36 = pygame.font.SysFont("Arial", 36)
font18 = pygame.font.SysFont("Arial", 18)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Rectangle"
        self.top = 100
        self.left = 100
        self.width = 380
        self.height = 100
        self.mass = 100.0
        self.running = True

        self.InitWindow()
    
    def set_mass(self):
        self.mass = 1000

    def pyg(self):
        b1 = pygame.Rect(200, 400, 100, 100)
        b2 = pygame.Rect(500, 400, 100, 100)
        b1_vel = 0.0
        temp1 = 200
        temp2 = 500
        temp3 = 0
        b2_vel = -1
        b1_mass = 1.0
        b2_mass = self.mass
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((800,600))
        collision_counter = 0

        while True:
            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            

            if b1.colliderect(b2): #or b1.x >= b2.x+100:
                if self.mass == 1:
                    # temp3 = b1_vel
                    # b1_vel = b2_vel
                    # b2_vel = temp3
                    b1_vel, b2_vel = b2_vel, b1_vel

                else:
                    b2_vel = b2_vel*(b2_mass - b1_mass)/(b2_mass + b1_mass) + b1_vel*2*b1_mass/(b2_mass+b1_mass)
                    b1_vel = b2_vel*2*b2_mass/(b2_mass+b1_mass) + b1_vel*(b1_mass-b2_mass)/(b1_mass+b2_mass)
                
                temp2 +=0.1
                collision_counter +=1
            if b1.collidepoint((0,450)):
                b1_vel = -1*b1_vel
                collision_counter +=1
                temp1 +=0.1

            # if b2.collidepoint((100,450))or b2.x <100:
            #     temp2 +=0.01

            #Drawing
            #Collisions
            temp1 += b1_vel
            temp2 += b2_vel
            b1.x = temp1
            b2.x = temp2
            screen.fill((48, 48, 48))
            pygame.draw.line(screen, (20,20,20), (0,505), (800,505), 5)
            pygame.draw.rect(screen, (100,100,255), b1)
            pygame.draw.rect(screen, (100,255,100), b2)



            screen.blit(font36.render(str(collision_counter), False, (255, 255, 255)), (600, 50))
            screen.blit(font18.render("Prędkość 1: %.4f" %b1_vel , False, (100, 100, 255)), (20, 50))
            screen.blit(font18.render("Prędkość 2: %.4f" %b2_vel, False, (100, 255, 100)), (20,80))
            pygame.display.update()  
            clock.tick()
    
    def InitWindow(self):
        # etykiety
        etykieta1 = QLabel("Liczba 1:", self)
        etykieta2 = QLabel("Liczba 2:", self)
        etykieta3 = QLabel("Wynik:", self)
        Btn = QPushButton("Start", self)
        Btn.clicked.connect(self.pyg)
        Btn2 = QPushButton("masa", self)
        Btn2.clicked.connect(self.set_mass)
        # przypisanie widgetów do układu tabelarycznego
        uklad1 = QGridLayout()
        uklad1.addWidget(etykieta1, 0,0)
        uklad1.addWidget(etykieta2, 0, 1)
        uklad1.addWidget(etykieta3, 0, 2)
        uklad1.addWidget(Btn, 1,0)
        uklad1.addWidget(Btn2, 1,2)

        # przypisanie utworzonego układu do okna
        self.setLayout(uklad1)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        
        


        self.show()
 

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())