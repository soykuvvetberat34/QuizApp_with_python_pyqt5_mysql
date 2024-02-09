import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Teacher as t
from PyQt5.QtGui import QIcon, QPixmap
import dbConnect
import decision
    
ques_count = 0
questions = []
answers = []
ques_id = []

dbConnect.mycursor.execute("SELECT questions FROM questions")
questions = dbConnect.mycursor.fetchall()
for i in questions:
    ques_count += 1

dbConnect.mycursor.execute("SELECT idquestions FROM questions")
ques_id = dbConnect.mycursor.fetchall()
dbConnect.mycursor.execute("SELECT answer FROM questions")
answers = dbConnect.mycursor.fetchall()


dbConnect.mycursor.execute("SELECT idstudents FROM students")
idstudents = [item[0] for item in dbConnect.mycursor.fetchall()]
dbConnect.mycursor.execute("SELECT studentsnumber FROM students")
studentsnumber = [item[0] for item in dbConnect.mycursor.fetchall()]
dbConnect.mycursor.execute("SELECT studentsName FROM students")
studentsName = [item[0] for item in dbConnect.mycursor.fetchall()]
dbConnect.mycursor.execute("SELECT studentsSurname FROM students")
studentsSurname = [item[0] for item in dbConnect.mycursor.fetchall()]
dbConnect.mycursor.execute("SELECT studentsPoint FROM students")
studentsPoint = [item[0] for item in dbConnect.mycursor.fetchall()]

idstudents2 = [str(item) for item in idstudents]
studentsnumber2 = [str(item) for item in studentsnumber]
studentsPoint2 = [str(item) for item in studentsPoint]

print(idstudents2)
print(studentsName)
print(studentsPoint2[0])

std_count=0
for i in studentsName:
    std_count+=1
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = t.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initGUI()

    def initGUI(self):
        self.ui.pushButton.clicked.connect(self.SoruEkle)
        self.ui.pushButton_2.clicked.connect(self.SoruSil)
        self.ui.pushButton_3.clicked.connect(self.SoruGuncelle)
        self.ui.pushButton_4.clicked.connect(self.showWindowLogin)
        font = QFont()
        font.setPointSize(12)
        font.setFamily("Orbitron")
        self.ui.label_baslik.setFont(font)

        font2 = QFont()
        font2.setPointSize(10)
        font2.setFamily("Pacifico")
        self.ui.label_2.setFont(font2)
        self.ui.label_3.setFont(font2)
        
        self.ui.tableWidget.setRowCount(ques_count)
        self.ui.tableWidget.setColumnCount(3)
        headers=["Soru id","Soru","Doğru cevap"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget.setColumnWidth(1,400)
        self.ui.tableWidget.setColumnWidth(2,245)

        self.count=0
        for i in range(ques_count):
            self.ui.tableWidget.setItem(self.count,0, QTableWidgetItem(str(ques_id[self.count][0])))
            self.ui.tableWidget.setItem(self.count,1, QTableWidgetItem(questions[self.count][0]))
            self.ui.tableWidget.setItem(self.count,2, QTableWidgetItem(answers[self.count][0]))
            self.count+=1
        
        #-----------------------------------------------------------------
        self.ui.tableWidget_2.setRowCount(std_count)
        self.ui.tableWidget_2.setColumnCount(5)
        headers2=["Öğrenci id","Öğrenci numarası","Öğrenci adı","Öğrenci soyadı","Öğrenci puanı"]
        self.ui.tableWidget_2.setHorizontalHeaderLabels(headers2)
        self.ui.tableWidget_2.setColumnWidth(1,160)
        self.ui.tableWidget_2.setColumnWidth(2,170)
        self.ui.tableWidget_2.setColumnWidth(3,180)
        count2=0
        print(count2)
        for i in range(std_count):
            self.ui.tableWidget_2.setItem(count2,0, QTableWidgetItem(idstudents2[count2]))
            self.ui.tableWidget_2.setItem(count2,1, QTableWidgetItem(studentsnumber2[count2]))
            self.ui.tableWidget_2.setItem(count2,2, QTableWidgetItem(studentsName[count2]))
            self.ui.tableWidget_2.setItem(count2,3, QTableWidgetItem(studentsSurname[count2]))
            self.ui.tableWidget_2.setItem(count2,4, QTableWidgetItem(studentsPoint2[count2]))
            count2+=1
        self.ui.tableWidget_2.doubleClicked.connect(self.onClick2)
        self.ui.tableWidget.doubleClicked.connect(self.onClick)

    def onClick(self):

        msgBox_newq2=QMessageBox(self)
        msgBox_newq2.setIcon(QMessageBox.Information)
        msgBox_newq2.setText("SORULAR HAKKINDA İŞLEM YAPMAK İÇİN AŞAĞIDAKİ BUTONLARI KULLAN!")
        msgBox_newq2.setWindowTitle("UYARI")
        msgBox_newq2.setStandardButtons(QMessageBox.Ok)
        msgBox_newq2.exec_()
    def onClick2(self):

        msgBox3=QMessageBox(self)
        msgBox3.setIcon(QMessageBox.Information)
        msgBox3.setText("ÖĞRENCİ BİLGİLERİNE ERİŞİMİNİZ BULUNMAMAKTADIR, HERHANGİ BİR BİLGİYİ DEĞİŞTİREMEZSİNİZ!")
        msgBox3.setWindowTitle("UYARI")
        msgBox3.setStandardButtons(QMessageBox.Ok)
        msgBox3.exec_()
            
    #-----------------------------------------------------------------
    def SoruEkle(self):
        
        while(True):
            i,okPressed=QInputDialog.getText(self,"SORU EKLE","Sorunuzu giriniz,soru veritabanına Kaydedilecektir!",QLineEdit.Normal,"")
            
            if i=="":
                msgBox10=QMessageBox(self)
                msgBox10.setText("Soru ekle kısmı boş bırakılamaz! Tekrar dene.")
                msgBox10.setWindowTitle("UYARI")
                msgBox10.setIcon(QMessageBox.Critical)
                msgBox10.setStandardButtons(QMessageBox.Ok) 
                msgBox10.exec_()              
                continue
            else:
                break 
        while(True):
            i2,okPressed=QInputDialog.getText(self,"Cevap EKLE","Cevabınızı giriniz,cevap veritabanına Kaydedilecektir!",QLineEdit.Normal,"")
            
            if i2=="":
                msgBox11=QMessageBox(self)
                msgBox11.setText("Cevap ekle kısmı boş bırakılamaz! Tekrar dene.")
                msgBox11.setWindowTitle("UYARI")
                msgBox11.setIcon(QMessageBox.Critical)
                msgBox11.setStandardButtons(QMessageBox.Ok) 
                msgBox11.exec_()              
                continue
            else:
                break 
        sql1="INSERT INTO questions(questions,answer) VALUE(%s,%s)"
        values1=(i,i2)
        dbConnect.mycursor.execute(sql1,values1)
        try:
            dbConnect.mydb.commit()
        except dbConnect.pymysql.connect.Error as err:
            print(err)
        finally:
            msgBox11=QMessageBox(self)
            msgBox11.setText("Kayıt başarılı bir şekilde tamamlandı.Tekrar giriş yaptığınızda sorunuzu görüntüleyebilirsiniz!")
            msgBox11.setWindowTitle("KAYIT BAŞARILI")
            msgBox11.setIcon(QMessageBox.Information)
            msgBox11.setStandardButtons(QMessageBox.Ok) 
            msgBox11.exec_() 

        


        
    def SoruSil(self):
        while(True):
            i2,okPressed=QInputDialog.getText(self,"SORU SİL","Silinecek sorunun id numarasını girin",QLineEdit.Normal,"")

            if i2=="":
                msgBox11=QMessageBox(self)
                msgBox11.setText("Cevap ekle kısmı boş bırakılamaz! Tekrar dene.")
                msgBox11.setWindowTitle("UYARI")
                msgBox11.setIcon(QMessageBox.Critical)
                msgBox11.setStandardButtons(QMessageBox.Ok) 
                msgBox11.exec_()              
                continue
            else:
                break
        i2=int(i2)
        sql="DELETE FROM questions where idquestions=%s"
        dbConnect.mycursor.execute(sql,i2)
        try:
            dbConnect.mydb.commit()
        except dbConnect.pymysql.connect.Error as err:
            print(err)
        finally:
            msgBox11=QMessageBox(self)
            msgBox11.setText("Kayıt Silindi.Tekrar giriş yaptığınızda sorunuz görünmeyecektir!")
            msgBox11.setWindowTitle("KAYIT SİLİNDİ")
            msgBox11.setIcon(QMessageBox.Information)
            msgBox11.setStandardButtons(QMessageBox.Ok) 
            msgBox11.exec_()   
        
    
    def SoruGuncelle(self):
        while(True):
            i3,okPressed=QInputDialog.getText(self,"SORU GÜNCELLE","Güncellenecek sorunun id numarasını girin",QLineEdit.Normal,"")

            if i3=="":
                msgBox12=QMessageBox(self)
                msgBox12.setText("Bu kısım boş bırakılamaz! Tekrar dene.")
                msgBox12.setWindowTitle("UYARI")
                msgBox12.setIcon(QMessageBox.Critical)
                msgBox12.setStandardButtons(QMessageBox.Ok) 
                msgBox12.exec_()              
                continue
            else:
                break
        i3=int(i3)
        while(True):
            i4,okPressed=QInputDialog.getText(self,"SORU GÜNCELLE","Eski sorunun yerine gelecek yeni soruyu girin!",QLineEdit.Normal,"")

            if i4=="":
                msgBox13=QMessageBox(self)
                msgBox13.setText("Bu kısım boş bırakılamaz! Tekrar dene.")
                msgBox13.setWindowTitle("UYARI")
                msgBox13.setIcon(QMessageBox.Critical)
                msgBox13.setStandardButtons(QMessageBox.Ok) 
                msgBox13.exec_()              
                continue
            else:
                break

        while(True):
            i5,okPressed=QInputDialog.getText(self,"CEVAP GÜNCELLE","Eski cevabın yerine gelecek yeni cevabı girin!",QLineEdit.Normal,"")

            if i5=="":
                msgBox14=QMessageBox(self)
                msgBox14.setText("Bu kısım boş bırakılamaz! Tekrar dene.")
                msgBox14.setWindowTitle("UYARI")
                msgBox14.setIcon(QMessageBox.Critical)
                msgBox14.setStandardButtons(QMessageBox.Ok) 
                msgBox14.exec_()              
                continue
            else:
                break
        sql="UPDATE questions set questions=%s WHERE idquestions=%s"
        values=(i4,i3)
        dbConnect.mycursor.execute(sql,values)
        sql2="UPDATE    questions set answer=%s WHERE idquestions=%s"
        values2=(i5,i3)
        dbConnect.mycursor.execute(sql2,values2)
        try:
            dbConnect.mydb.commit()
        except dbConnect.pymysql.connect.Error as err:
            print(err)
        finally:
            msgBox12=QMessageBox(self)
            msgBox12.setText("Kayıt Güncellendi.Tekrar giriş yaptığınızda güncelleme gözükecektir!")
            msgBox12.setWindowTitle("KAYIT GÜNCELLENDİ")
            msgBox12.setIcon(QMessageBox.Information)
            msgBox12.setStandardButtons(QMessageBox.Ok) 
            msgBox12.exec_()   

    
        
    def showWindowLogin(self):
        self.close()
        dbConnect.mydb.close()
        self.main=decision.MyWindow()
        self.main.show()
        
    

        
        


        