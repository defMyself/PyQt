import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel, QPushButton, QApplication, QMainWindow,QAction, qApp, QHboxLayout, QVBoxLayout, QGridLayout,QLineEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication

class AppIcon(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('t1.jpg'))
        self.show()

def show_w():
	app = QApplication(sys.argv)
	
	w = QWidget()
	w.resize(500, 500)
	w.move(500, 100)
	w.setWindowTitle('Simple')
	w.show()
	
    #w1 = QWidget()
    #w1.resize(600,600)
    #w1.move(600,100)
    #w1.setwindowTitle('another')
    #w1.show()

	sys.exit(app.exec_())
	# sys.exit()
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
    ex = AppIcon()
    sys.exit(app.exec_())
