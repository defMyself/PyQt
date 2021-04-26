from PyQt5.QtWidgets import *
import sys

class Test(QDialog):

    button_clicked_signal = pyqtSignal() # 自定义信号，不带参
    
    def __init__(self,parent=None):
        super().__init__(parent)

        btn = QPushButton('关闭', self)
        btn.clicked.connect(self.btn_clicked) # 信号/槽
        
        self.button_clicked_signal.connect(self.my_close) # 接收信号，连接到槽
        
        
    def btn_clicked(self):
        self.button_clicked_signal.emit() # 发送自定义信号，无参
        
    def my_close(self):
        self.close()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Test()
    dlg.show()
    sys.exit(app.exec_())
