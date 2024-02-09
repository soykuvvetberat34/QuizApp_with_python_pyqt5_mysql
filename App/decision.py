import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import decisionUi
from PyQt5.QtGui import QIcon, QPixmap
import dbConnect 
import TeacherApp
import student_login1App as stdapp
ogrno=0

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.ui=decisionUi.Ui_MainWindow()
        self.ui.setupUi(self)
        font=QFont()
        font2=QFont()
        font2.setPointSize(6)
        font2.setFamily("Orbitron")
        font.setPointSize(15)
        self.ui.baslik.setFont(font)
        self.initUI()
 

    def initUI(self):
        self.setWindowTitle("Quiz Sistemi")

        label = QLabel(self)
        pixmap = QPixmap("foto.jpeg")
        label.setFixedSize(100, 100) 
        label.move(20,20)
        label.setScaledContents(True)
        label.setPixmap(pixmap)
        self.show()
        self.ui.Btn_ogr_giris.clicked.connect(self.ogr_giris)

        self.ui.Btn_ogrtmn_giris.clicked.connect(self.ogrtmn_giris)
        self.ui.Btn_ogr_kayit.clicked.connect(self.ogr_kayit)

    def hide_show():
        MyWindow.show()     
    def ogr_giris(self):
        while(True):
            i,okPressed=QInputDialog.getText(self,"Öğrenci giriş","Öğrenci numaranızı girin",QLineEdit.Normal,"")
            if i=="":
                msgBox10=QMessageBox(self)
                msgBox10.setText("Tekrar Dene!")
                msgBox10.setWindowTitle("Giriş Başarısız")
                msgBox10.setStandardButtons(QMessageBox.Ok)               
                continue
            else:
                break
        ogr_giris_no=int(i)
        global ogrno
        ogrno=ogr_giris_no
        sql="SELECT studentsName FROM students WHERE studentsnumber=%s"
        dbConnect.mycursor.execute(sql,ogr_giris_no)
        result_stdname=dbConnect.mycursor.fetchall()
        if result_stdname==():
            msgBox2=QMessageBox(self)
            msgBox2.setText("Tekrar Dene!")
            msgBox2.setWindowTitle("Giriş Başarısız")
            msgBox2.setStandardButtons(QMessageBox.Ok)
        else:
            msgBox=QMessageBox(self)
            msgBox.setText("Yönelendiriliyorsunuz...")
            msgBox.setInformativeText("Yetki -> Öğrenci")
            msgBox.setWindowTitle("Giriş Başarılı")
            msgBox.setStandardButtons(QMessageBox.Yes)
            result2 = msgBox.exec_()#
            if result2 == QMessageBox.Yes:#daha mantıklı   
                self.close()
                self.stdapp1=stdapp.MyWidget(ogrno)
                self.stdapp1.show()    
                

                             

   
    def ogrtmn_giris(self):
        while(True):
            text,okPressed=QInputDialog.getText(self,"Öğretmen Giriş","Şifrenizi girin!",QLineEdit.Password,"")
            if text=="":
                msgBox11=QMessageBox(self)
                msgBox11.setText("Tekrar Dene!")
                msgBox11.setWindowTitle("Giriş Başarısız")
                msgBox11.setStandardButtons(QMessageBox.Ok)     
                continue
            else:
                break
            
        sql="SELECT AuthorizedUserName FROM authorizedusers WHERE AuthorizedUserPassword=%s"
        dbConnect.mycursor.execute(sql,int(text))
        result=dbConnect.mycursor.fetchall()
        if result==():
            msgBox2=QMessageBox(self)
            msgBox2.setText("Tekrar Dene!")
            msgBox2.setWindowTitle("Giriş Başarısız")
            msgBox2.setStandardButtons(QMessageBox.Ok)
        else:
            msgBox=QMessageBox(self)
            msgBox.setText("Yönelendiriliyorsunuz...")
            msgBox.setInformativeText("Yetki -> Öğretmen")
            msgBox.setWindowTitle("Giriş Başarılı")
            msgBox.setStandardButtons(QMessageBox.Yes)
            self.teacher=TeacherApp.MyWindow()
            self.teacher.show()
            self.close()

            
     
    def ogr_kayit(self):
        while(True):
            std_no,okPressed=QInputDialog.getText(self,"Öğrenci Kayıt","Öğrenci numaranızı girin",QLineEdit.Normal,"")
            msgBox3=QMessageBox(self)
            msgBox3.setText(f"Öğrenci numaranız {std_no} Kaydedilsin mi?    ")
            msgBox3.setWindowTitle("Öğrenci kayıt")
            msgBox3.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            result=msgBox3.exec_()
            if result==QMessageBox.No:
                std_no=""
                continue
            else:
                break
                
                
        while(True):
            std_name,okPressed=QInputDialog.getText(self,"Öğrenci Kayıt","Adınızı girin",QLineEdit.Normal,"")
            msgBox4=QMessageBox(self)
            msgBox4.setText(f"Adiniz: {std_name} kaydedilsin mi?  ")
            msgBox4.setWindowTitle("Öğrenci kayıt")
            msgBox4.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            result2=msgBox4.exec_()
            if result2==QMessageBox.No:
                std_name=""
                continue
            else:
                break
        while(True):
            std_surname,okPressed=QInputDialog.getText(self,"Öğrenci Kayıt","Soyadınızı girin",QLineEdit.Normal,"")
            msgBox5=QMessageBox(self)
            msgBox5.setText(f"Soyadiniz: {std_surname} ,Kaydedilsin mi?  ")
            msgBox5.setWindowTitle("Öğrenci kayıt")
            msgBox5.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            result3=msgBox5.exec_()
            if result3==QMessageBox.No:
                std_surname=""
                continue
            else:
                break
        sql="SELECT studentsName FROM students WHERE studentsnumber=%s"
        std_no=int(std_no)
        dbConnect.mycursor.execute(sql,std_no)
        result4=dbConnect.mycursor.fetchall()
        if result4==():
            sql="INSERT INTO students(studentsnumber,studentsName,studentsSurname,studentsPoint) VALUE(%s,%s,%s,%s)"
            values=(std_no,std_name,std_surname,0)
            dbConnect.mycursor.execute(sql,values)
            try:
                dbConnect.mydb.commit()
            except dbConnect.pymysql.connect.Error as err:
                msgBox7=QMessageBox(self)
                msgBox7.setText(f"HATA KODU:{err}")
                msgBox7.setWindowTitle("HATA!")
                msgBox7.setStandardButtons(QMessageBox.Ok)
                result5=msgBox6.exec_()    
                app.quit()
            finally:
                dbConnect.mydb.close()        
                msgBox6=QMessageBox(self)
                msgBox6.setText(f"Öğrenci {std_name} {std_surname} Kaydedildi! Giriş yapabilirsin  ")
                msgBox6.setWindowTitle("Öğrenci kaydedildi!")
                msgBox6.setStandardButtons(QMessageBox.Ok)
                result6=msgBox6.exec_()
                msgBox9=QMessageBox(self)
                msgBox9.setText("Programın kapatılması gerek giriş yapmak için tekrar açın!")
                msgBox9.setWindowTitle("UYARI")
                msgBox9.setStandardButtons(QMessageBox.Ok)
                result8=msgBox9.exec_()
                app.quit()

        else:     
                msgBox8=QMessageBox(self)
                msgBox8.setText(f"{std_no} nolu öğrenci zaten kayıtlı. Giriş YAP!  ")
                msgBox8.setWindowTitle("Öğrenci kaydedilemedi!")
                msgBox8.setStandardButtons(QMessageBox.Ok)
                result7=msgBox8.exec_()
                dbConnect.mydb.close()    



        
if __name__=='__main__':
    
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())
    


        


