# -*- coding: utf-8 -*-
import sys
from uicalculate import Ui_MainWindow
from PyQt4 import QtCore,QtGui

class Digcalculator(QtGui.QMainWindow,Ui_MainWindow):
    lcdstring = ''#显示屏显示的数字
    operation = ''#操作符
    currentNum = ''#当前值
    preventNum = ''#上一个值
    result = ''#结果
    def __init__(self,parent = None):
       super(Digcalculator, self).__init__()
       self.setupUi(self)
       self.action()


    def action(self):
        #将所有数字的按钮与其方法绑定
        self.number0.clicked.connect(self.buttonClicked)
        self.number1.clicked.connect(self.buttonClicked)
        self.number2.clicked.connect(self.buttonClicked)
        self.number3.clicked.connect(self.buttonClicked)
        self.number4.clicked.connect(self.buttonClicked)
        self.number5.clicked.connect(self.buttonClicked)
        self.number6.clicked.connect(self.buttonClicked)
        self.number7.clicked.connect(self.buttonClicked)
        self.number8.clicked.connect(self.buttonClicked)
        self.number9.clicked.connect(self.buttonClicked)
        self.point.clicked.connect(self.buttonClicked)


        #将操作符与方法绑定
        self.add.clicked.connect(self.opClicked)
        self.sub.clicked.connect(self.opClicked)
        self.mult.clicked.connect(self.opClicked)
        self.exc.clicked.connect(self.opClicked)


        #将clear与其方法绑定点击清零操作后将结果清除
        self.clear.clicked.connect(self.clearClicked)


        #将result与其方法绑定
        self.result.clicked.connect(self.resultClicked)





    def buttonClicked(self):
        if len(self.lcdstring) <= 9:
            self.lcdstring = self.lcdstring + self.sender().text()
            if str(self.lcdstring) == '.':
                self.lcdstring = '0.'
                self.lcd.display(self.lcdstring)
                self.currentNum = float(self.lcdstring)
            else:
                if str(self.lcdstring).count('.') > 1:
                    self.lcdstring = str(self.lcdstring)[:-1]#当点大于1时就将最后一个点去除实际上就是取最新的点
                    self.lcd.display(self.lcdstring)
                    self.currentNum = float(self.lcdstring)
                else:
                    self.lcd.display(self.lcdstring)
                    self.currentNum = float(self.lcdstring)
        else:
            pass




    def opClicked(self):
        if self.operation != '':
            self.resultClicked()
            self.preventNum = self.currentNum
            self.currentNum = 0
            self.lcdstring = ''
            self.operation = self.sender().text()
        else:
            self.preventNum = self.currentNum
            self.currentNum = 0
            self.lcdstring = ''
            self.operation = self.sender().text()



    def clearClicked(self):
        #将所有数据清零
        self.lcdstring = ''
        self.operation = ''
        self.currentNum = 0
        self.preventNum = 0
        self.result = 0
        self.lcd.display(0)



    def resultClicked(self):
        if self.operation == '+':
            self.result = self.currentNum + self.preventNum
            self.currentNum = self.result
            self.operation = ''
            self.preventNum = 0
            self.lcd.display(self.result)
        elif self.operation == '-':
            self.result = self.preventNum - self.currentNum
            self.currentNum = self.result
            self.operation = ''
            self.preventNum = 0
            self.lcd.display(self.result)
        elif self.operation == '*':
            self.result = self.currentNum * self.preventNum
            self.currentNum = self.result
            self.operation = ''
            self.preventNum = 0
            self.lcd.display(self.result)
        elif self.operation == '/':
            if self.currentNum == 0:
                self.lcd.display('Error')
                self.result = 0
                self.preventNum = 0
            else:
                self.result = self.preventNum/self.currentNum
                self.currentNum = self.result
                self.operation = ''
                self.preventNum = 0
                self.lcd.display(self.result)



    def closeEvent(self,event):
        reply = QtGui.QMessageBox.question(self,u'警告',u'确认退出?',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Digcalculator()
    window.show()
    sys.exit(app.exec_())