from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QGridLayout
import sys
import pygame


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Rectangle"
        self.top = 100
        self.left = 100
        self.width = 380
        self.height = 100
        self.mass = 100
        self.running = True

        
 
        self.InitWindow()
    
    def set_mass(self):
        self.mass = 1000

    def pyg(self):
        b1_pos = [100,400]
        b2_pos = [300,400]
        b1_vel = 0
        b2_vel = -1
        b1_mass = 1
        b2_mass = self.mass
        print(b2_mass)
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((800,600))

        while True:
            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            
            #Collisions
            b1_pos[0]+=b1_vel
            b2_pos[0]+=b2_vel
            
            if b1_pos[0]+100 == b2_pos[0]:
                b1_vel =- 1
                b2_vel = 0
            #Drawing
            screen.fill((48, 48, 48))
            pygame.draw.line(screen, (20,20,20), (0,505), (800,505), 5)
            pygame.draw.rect(screen, (100,100,255), (b1_pos[0], b1_pos[1], 100, 100))
            pygame.draw.rect(screen, (100,255,100), (b2_pos[0], b2_pos[1], 100, 100))
            
            pygame.display.update()
            clock.tick(60)    
    
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