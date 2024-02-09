import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Teacher as t
import dbConnect
import student_login1 as stdlog
import quizAppCommand as qac

global no1
class MyWidget(QWidget):
    def __init__(self,ogrno):
        super(MyWidget,self).__init__()
        self.ogrno=ogrno
        global no1
        no1=ogrno
        print(ogrno)
        self.ui=stdlog.Ui_Form()
        self.ui.setupUi(self)
        sql="SELECT studentsName FROM students WHERE studentsnumber=%s"
        dbConnect.mycursor.execute(sql,ogrno)
        std_name=dbConnect.mycursor.fetchall()
        self.name=std_name[0][0]
        sql2="SELECT studentsSurname FROM students WHERE studentsnumber=%s"
        dbConnect.mycursor.execute(sql2,ogrno)
        std_surname=dbConnect.mycursor.fetchall()       
        self.surname=std_surname[0][0]
        self.ui.label.setText(f"HOSGELDIN {self.name} {self.surname}")
        self.setWindowTitle("HOSGELDIN")
        self.ui.btn_point.clicked.connect(self.seePoint)
        self.ui.btn_solve.clicked.connect(self.checkSolve)
    def seePoint(self):
        sql3="SELECT studentsPoint FROM students WHERE studentsnumber=%s"
        dbConnect.mycursor.execute(sql3,self.ogrno)
        std_point=dbConnect.mycursor.fetchall()
        msgbox=QMessageBox(self)
        msgbox.setWindowTitle("PUANIN")
        msgbox.setText(f"{self.name} {self.surname} adlı öğrencinin puanı")
        msgbox.setInformativeText(f"puan:{std_point[0][0]}")
        msgbox.exec_()
    def checkSolve(self):
        sql="SELECT studentsPoint FROM students WHERE studentsnumber=%s"
        dbConnect.mycursor.execute(sql,self.ogrno)
        result=dbConnect.mycursor.fetchone()
        print(result[0])
        print(self.ogrno)
        if result[0]==0:
            msgbox3=QMessageBox(self)
            msgbox3.setWindowTitle("Quiz Başlat")
            msgbox3.setIcon(QMessageBox.Information)
            msgbox3.setText("Ok tuşuna bastığınızda testiniz Başlayacaktır!")
            msgbox3.setInformativeText("Hazır olduğunuzda Ok'a basın.")
            msgbox3.setStandardButtons(QMessageBox.Ok)
            result=msgbox3.exec_()
            if result== QMessageBox.Ok:
                self.close()
                self.quiztime=qac.MyWidget(self.ogrno)
                self.quiztime.show()
                
        else:
            msgbox2=QMessageBox(self)
            msgbox2.setWindowTitle("UYARI")
            msgbox2.setIcon(QMessageBox.Information)
            msgbox2.setText("Quiz'e zaten girdiniz!")
            msgbox2.setInformativeText("Aktif başka sınavınız yoktur.")
            msgbox2.setStandardButtons(QMessageBox.Ok)
            msgbox2.exec_()

