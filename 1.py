import sys
from PyQt5.QtWidgets import QApplication, QWidget

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
	show_w()
