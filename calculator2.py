from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QSize
import sys
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.otv=str()
        self.inp=QLineEdit()
        self.inp.setFont(QFont("Zekton",30))
        self.label=QLineEdit()
        self.label.setFont(QFont("Zekton",20))
        self.but0=QPushButton("0")
        self.but0.setFont(QFont("Zekton",25))
        self.but1=QPushButton("1")
        self.but1.setFont(QFont("Zekton",25))
        self.but2=QPushButton("2")
        self.but2.setFont(QFont("Zekton",25))
        self.but3=QPushButton("3")
        self.but3.setFont(QFont("Zekton",25))
        self.but4=QPushButton("4")
        self.but4.setFont(QFont("Zekton",25))
        self.but5=QPushButton("5")
        self.but5.setFont(QFont("Zekton",25))
        self.but6=QPushButton("6")
        self.but6.setFont(QFont("Zekton",25))
        self.but7=QPushButton("7")
        self.but7.setFont(QFont("Zekton",25))
        self.but8=QPushButton("8")
        self.but8.setFont(QFont("Zekton",25))
        self.but9=QPushButton("9")
        self.but9.setFont(QFont("Zekton",25))

        self.btn_plus=QPushButton("+")
        self.btn_plus.setStyleSheet("color: green")
        self.btn_plus.setFont(QFont("Zecton",25))
        self.btn_minus=QPushButton("-")
        self.btn_minus.setStyleSheet("color: green")
        self.btn_minus.setFont(QFont("Zekton",25))
        self.btn_umnoj=QPushButton("*")
        self.btn_umnoj.setStyleSheet("color: green")
        self.btn_umnoj.setFont(QFont("Zekton",25))
        self.btn_step=QPushButton("^")
        self.btn_step.setStyleSheet("color: green")
        self.btn_step.setFont(QFont("Zekton",25))
        self.btn_razdel=QPushButton("/")
        self.btn_razdel.setStyleSheet("color: green")
        self.btn_razdel.setFont(QFont("Zekton",25))
        self.btn_ost=QPushButton("%")
        self.btn_ost.setStyleSheet("color: green")
        self.btn_ost.setFont(QFont("Zekton",25))
        self.btn_ravno=QPushButton("=")
        self.btn_ravno.setStyleSheet("color: green")
        self.btn_ravno.setFont(QFont("Zekton",25))
        self.btn_clear=QPushButton("C")
        self.btn_clear.setStyleSheet("color: red")
        self.btn_clear.setFont(QFont("Zekton",25))
        self.btn_del=QPushButton("")
        self.btn_del.setIcon(QIcon("backspace6.png"))
        self.btn_del.setIconSize(QSize(30,43))
        self.btn_del.setFont(QFont("Zekton",25))
        self.btn_fact=QPushButton("!")
        self.btn_fact.setFont(QFont("Zekton",25))
        self.skobka1=QPushButton("(")
        self.skobka2=QPushButton(")")
        self.fl=QPushButton(".")
        self.fl.setFont(QFont("Zekton",25))
        self.skobka1.setFont(QFont("Zekton",25))
        self.skobka2.setFont(QFont("Zekton",25))
        
        self.box_1=QHBoxLayout()
        self.box_2=QHBoxLayout()
        self.box_3=QHBoxLayout()
        self.box_4=QHBoxLayout()
        self.box_5=QHBoxLayout()
        self.box_6=QHBoxLayout()
        self.box_7=QHBoxLayout()
        self.main_box=QVBoxLayout()

    
        self.box_1.addWidget(self.btn_clear)
        self.box_1.addWidget(self.btn_step)
        self.box_1.addWidget(self.btn_ost)
        self.box_1.addWidget(self.btn_razdel)

        self.box_7.addWidget(self.skobka1)
        self.box_7.addWidget(self.skobka2)
        self.box_7.addWidget(self.fl)
        self.box_7.addStretch()

        self.box_2.addWidget(self.but7)
        self.box_2.addWidget(self.but8)
        self.box_2.addWidget(self.but9)
        self.box_2.addWidget(self.btn_umnoj)

        self.box_3.addWidget(self.but4)
        self.box_3.addWidget(self.but5)
        self.box_3.addWidget(self.but6)
        self.box_3.addWidget(self.btn_minus)

        self.box_4.addWidget(self.but1)
        self.box_4.addWidget(self.but2)
        self.box_4.addWidget(self.but3)
        self.box_4.addWidget(self.btn_plus)

        self.box_6.addWidget(self.but0)


        self.box_5.addWidget(self.btn_ravno)
        self.box_5.addWidget(self.btn_del)

        self.box_6.addLayout(self.box_5)

        self.main_box.addStretch()
        self.main_box.addWidget(self.inp)
        self.main_box.addWidget(self.label)
        self.main_box.addLayout(self.box_7)
        self.main_box.addLayout(self.box_1)
        self.main_box.addLayout(self.box_2)
        self.main_box.addLayout(self.box_3)
        self.main_box.addLayout(self.box_4)
        self.main_box.addLayout(self.box_5)
        self.main_box.addLayout(self.box_6)
        self.main_box.addStretch()

        self.but1.clicked.connect(lambda: self.press_button("1"))
        self.but2.clicked.connect(lambda: self.press_button("2"))
        self.but3.clicked.connect(lambda: self.press_button("3"))
        self.but4.clicked.connect(lambda: self.press_button("4"))
        self.but5.clicked.connect(lambda: self.press_button("5"))
        self.but6.clicked.connect(lambda: self.press_button("6"))
        self.but7.clicked.connect(lambda: self.press_button("7"))
        self.but8.clicked.connect(lambda: self.press_button("8"))
        self.but9.clicked.connect(lambda: self.press_button("9"))
        self.but0.clicked.connect(lambda: self.press_button("0"))

        self.btn_del.clicked.connect(lambda: self.press_button("<"))
        self.btn_ravno.clicked.connect(lambda: self.press_button("="))
        self.btn_plus.clicked.connect(lambda: self.press_button("+"))
        self.btn_minus.clicked.connect(lambda: self.press_button("-"))
        self.btn_umnoj.clicked.connect(lambda: self.press_button("*"))
        self.btn_razdel.clicked.connect(lambda: self.press_button("/"))
        self.btn_step.clicked.connect(lambda: self.press_button("**"))
        self.btn_ost.clicked.connect(lambda: self.press_button("%"))
        self.btn_clear.clicked.connect(lambda: self.press_button("c"))
        self.skobka1.clicked.connect(lambda: self.press_button("("))
        self.skobka2.clicked.connect(lambda: self.press_button(")"))
        self.fl.clicked.connect(lambda: self.press_button("."))
        self.setLayout(self.main_box)
        self.setFixedSize(500,550)
        self.show()
    
    def press_button(self,otv):
    
        if otv == "=":
            try:
                self.otv=str(eval(self.otv))
                self.label.setText(" ")

            except:
                pass

        elif otv == "<":
            self.otv=self.otv[:-1]        
            
            try:
                self.label.setText(str(eval(self.otv)))

            except:
                self.label.setText("")
        
        elif otv == "c":
            self.label.setText("")
            
            self.otv=str()
        
        else:
            self.otv+=otv
            
            try:
                self.label.setText(str(eval(self.otv)))
            
            except:
                self.label.setText("enter correctly")
                
        
        self.inp.setText(self.otv)


app=QApplication([])
win=Calculator()
sys.exit(app.exec())