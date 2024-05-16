from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import QPixmap

from final_win import *

from instr import *

class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.set_ui()
        #self.connects()

    def set_appear(self):
        self.setStyleSheet('font-size:24px; margin:10px')
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)



    def show_final_win(self):
        self.win = FinalWin(p1 = int(self.answ1_input.text()),
                            p2 = int(self.answ2_input.text()),
                            p3 = int(self.answ3_input.text()))
                            
        self.win.show()
        self.hide()

    def set_ui(self):

        fio_label = QLabel(txt_name)
        fio_input = QLineEdit()

        instr1 = QLabel(txt_test)
        pic_label = QLabel()
        pic = QPixmap('cat.jpg')
        pic_label.setPixmap(pic)
        
        

        self.answ1_input = QLineEdit()
        self.answ2_input = QLineEdit()
        self.answ3_input = QLineEdit()


        final_btn = QPushButton(txt_sendresults)
        final_btn.clicked.connect(self.show_final_win)

        line1 = QVBoxLayout()
        line2 = QVBoxLayout()
        line3 = QVBoxLayout()
        line4 = QHBoxLayout()

        line = QVBoxLayout()

        
        line.addWidget(fio_label)
        line.addWidget(fio_input)
        
        line.addWidget(instr1)
        line.addWidget(pic_label)

        line.addWidget(self.answ1_input)
        line.addWidget(self.answ1_input)
        line.addWidget(self.answ1_input)








        line.addWidget(final_btn)
        self.setLayout(line)





 