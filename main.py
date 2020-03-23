import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QGridLayout, QSlider, QHBoxLayout, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Wyliczanie pi"
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
        btn1.clicked.connect(self.oblicz)
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