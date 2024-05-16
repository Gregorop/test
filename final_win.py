from PyQt5.QtWidgets import *

from instr import *


class FinalWin(QWidget):
    def __init__(self, answ1, answ2, answ3):
        super().__init__()
        self.answ = self.calc_res(answ1, answ2, answ3)
        self.set_appear()
        self.set_ui()


    
        
    def calc_res(self, answ1,answ2,answ3):
        return (answ1+answ2+answ3)

    def set_appear(self):
        self.setStyleSheet('font-size:38px;')
        if self.health == 'низкое':
            self.setStyleSheet('font-size:38px; background:pink')
        if self.health == 'высокое':
            self.setStyleSheet('font-size:38px; background:lightgreen')    
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    def set_ui(self):
        index = QLabel('Ваш индекс Руфье: ' + str(self.index))
        health = QLabel('Ваше здоровье: ' + self.health)
        
        line = QVBoxLayout()
        line.addWidget(index)
        line.addWidget(health)

        self.setLayout(line)




