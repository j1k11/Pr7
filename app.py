import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow 
from random import choice , randint

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui  = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generate)
    def exemple(self):
        print(1)   
        
    def generate(self,):
        self.password_len =8
        alphabet = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
        numbers = "1234567890"
        symbols = "!@#$%^&*()_+-=\\'\"|?.,"
        password = ""
        
        for i in range (self.password_len):
            chance = randint(0,100)
            if self.ui.cb_numbers.isChecked() and chance > 80:
                digit = choice(numbers)
                password += digit
            if self.ui.cb_alphabet.isChecked() and chance > 50:
                leter = choice(alphabet)
                password += leter
                
            symbol = choice(symbols)
            password += symbol 
        self.ui.result.setText(password)  
          
        
                   
app =QApplication([])     
ex = Widget()
ex.show()
app.exec_()