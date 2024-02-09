from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
import Teacher as t
import dbConnect
import quizApp as qa
import student_login1App as sdtlog
from PyQt5.QtCore import QTimer, QTime

class MyWidget(QWidget):
    def __init__(self,ogrno):
        super(MyWidget,self).__init__()
        self.ogrno=str(ogrno)
        
        self.ui=qa.Ui_Form()
        self.ui.setupUi(self)
        self.questions=[]
        self.puan=0
        dbConnect.mycursor.execute("SELECT questions FROM questions")
        get_questions=dbConnect.mycursor.fetchall()
        for i in get_questions:
            for k in i:
                self.questions.append(k)
        count_questions = len(self.questions)
        self.count=count_questions




        self.ui.btn_sonraki_soru_2.clicked.connect(self.sonraki_soru)
        self.ui.lbl_soru.setText(self.questions[0])
        self.ui.btn_chc1.setText("A")
        self.ui.btn_chc2.setText("B")
        self.ui.btn_chc3.setText("C")
        self.ui.btn_chc4.setText("D")
        self.ui.btn_chc5.setText("E")
        
        self.ui.btn_chc5.clicked.connect(self.sonraki_soru)
        self.ui.btn_chc4.clicked.connect(self.sonraki_soru)
        self.ui.btn_chc3.clicked.connect(self.sonraki_soru)
        self.ui.btn_chc2.clicked.connect(self.sonraki_soru)
        self.ui.btn_chc1.clicked.connect(self.sonraki_soru)
        
        self.ui.btn_chc5.clicked.connect(self.checkbox_check)
        self.ui.btn_chc4.clicked.connect(self.checkbox_check)
        self.ui.btn_chc3.clicked.connect(self.checkbox_check)
        self.ui.btn_chc2.clicked.connect(self.checkbox_check)
        self.ui.btn_chc1.clicked.connect(self.checkbox_check)
        
        self.ui.btn_chc5.clicked.connect(self.get_point1)
        self.ui.btn_chc4.clicked.connect(self.get_point2)
        self.ui.btn_chc3.clicked.connect(self.get_point3)
        self.ui.btn_chc2.clicked.connect(self.get_point4)
        self.ui.btn_chc1.clicked.connect(self.get_point5)
        self.count2=0
        
        self.ui.btn_sonraki_soru.clicked.connect(self.bitir)
        self.geridon=sdtlog.MyWidget(self.ogrno) 
        
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.total_seconds = 600
        self.timer.start(1000)
        self.ui.sayac.setDigitCount(5)
        minutes = count_questions // 60
        seconds = count_questions % 60
        formatted_time = "{:02d}:{:02d}".format(seconds, minutes)
        self.ui.sayac.display(formatted_time)
        

        
        
    def update_timer(self):
        if self.total_seconds > 0:
            self.total_seconds -= 1
            minutes = self.total_seconds // 60
            seconds = self.total_seconds % 60
            formatted_time = "{:02d}:{:02d}".format(minutes, seconds)
            self.ui.sayac.display(formatted_time)
        else:
            self.timer.stop()
            QMessageBox.information(self, "Geri Sayım Bitti", "Süre doldu!")
            self.bitir()
        
    def checkbox_check(self):
        if self.count2==1:
            self.ui.checkBox_2.setChecked(True)
        elif self.count2==2:
            self.ui.checkBox_7.setChecked(True)
        elif self.count2==3:
            self.ui.checkBox_5.setChecked(True)
        elif self.count2==4:
            self.ui.checkBox_8.setChecked(True)
        elif self.count2==5:
            self.ui.checkBox_6.setChecked(True)
        elif self.count2==6:
            self.ui.checkBox_10.setChecked(True)
        elif self.count2==7:
            self.ui.checkBox_9.setChecked(True)
        elif self.count2==8:
            self.ui.checkBox_4.setChecked(True)
        elif self.count2==9:
            self.ui.checkBox_3.setChecked(True)
        elif self.count2==10:
            self.ui.checkBox.setChecked(True)
    
    def sonraki_soru(self):
        self.count2+=1
        if self.count2<self.count:
            self.ui.lbl_soru_count.setText(f"{self.count2+1}/10")
            self.ui.lbl_soru.setText(self.questions[self.count2])
        else:
            msgbox=QMessageBox(self)
            msgbox.setText("Tüm soruları gördünüz!")
            msgbox.setWindowTitle("SORULAR BİTTİ")
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec_()

            
        
    
    def get_point1(self):
        
        count3=self.count2
        count3=count3-1
        if self.count2<11:
            soru=self.questions[count3]
            sql="SELECT answer FROM questions WHERE questions=%s"
            dbConnect.mycursor.execute(sql,soru)
            cevap=dbConnect.mycursor.fetchone()
            for i in cevap:
                if i==self.ui.btn_chc5.text():
                    self.puan=self.puan+1
                    
                    
        else:
            print("---")

    def get_point2(self):
        
        count4=self.count2
        count4=count4-1
        
        if self.count2<11:
            soru=self.questions[count4]
            sql="SELECT answer FROM questions WHERE questions=%s"
            dbConnect.mycursor.execute(sql,soru)
            cevap=dbConnect.mycursor.fetchone()
            for i in cevap:
                if i==self.ui.btn_chc4.text():
                    self.puan=self.puan+1
        else:
            print("---")
    def get_point3(self):
        
        count5=self.count2
        count5=count5-1
        if self.count2<11:
            soru=self.questions[count5]
            sql="SELECT answer FROM questions WHERE questions=%s"
            dbConnect.mycursor.execute(sql,soru)
            cevap=dbConnect.mycursor.fetchone()
            for i in cevap:
                if i==self.ui.btn_chc3.text():
                    self.puan=self.puan+1
        else:
            print("---")

    def get_point4(self):
        
        count6=self.count2
        count6=count6-1
        if self.count2<11:
            soru=self.questions[count6]
            sql="SELECT answer FROM questions WHERE questions=%s"
            dbConnect.mycursor.execute(sql,soru)
            cevap=dbConnect.mycursor.fetchone()
            for i in cevap:
                if i==self.ui.btn_chc2.text():
                    self.puan=self.puan+1
        else:
            print("---")

            
    def get_point5(self):
        
        count7=self.count2
        count7=count7-1
        if self.count2<11:
            soru=self.questions[count7]
            sql="SELECT answer FROM questions WHERE questions=%s"
            dbConnect.mycursor.execute(sql,soru)
            cevap=dbConnect.mycursor.fetchone()
            for i in cevap:
                if i==self.ui.btn_chc1.text():
                    self.puan=self.puan+1
        else:
            print("---")
    def bitir(self):
        print(self.ogrno)
        sql="UPDATE students SET studentsPoint=%s WHERE studentsnumber=%s"
        values=(int(self.puan*10),self.ogrno)
        dbConnect.mycursor.execute(sql,values)
        
        try:
            dbConnect.mydb.commit()
        except dbConnect.pymysql.connect.Error as err:
            print(err)
        finally:
            print("Veri güncellendi!")
        self.close()
        self.geridon.show()



