#import needed libraries
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication,QTableWidgetItem
import mysql.connector
from sqlalchemy import null

# A class for the first window
class LoginScreen(QDialog):
    # A function to initliaze QT wedgit
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)

    # A function to provide functionality for the Log-in page 
    def loginfunction(self):
        # Get texts from feilds
        user = self.emailfield.text()
        password = self.passwordfield.text()

        # Check if either feilds is empty
        if len(user)==0 or len(password)==0:
            self.error.setText("Please input all fields.")

        else:
            # Connect to DB
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "CompanyProj"
            )
            cur = mydb.cursor()

            # A query that returns password of given ssn 
            cur.execute("SELECT password FROM CompanyProj.logininfo WHERE username ='"+user+"'")
            result_pass = cur.fetchone()[0]

            # Check if inserted password is the same in DB
            if str(result_pass) == password:
                print("Successfully logged in.")
                self.error.setText("")
                # Call a function to move to next page
                self.getinfo()
            else:
                self.error.setText("Invalid username or password")
        
    # A function to display second screen
    def getinfo(self):
        display = CreateInfoScreen()
        widget.addWidget(display)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.show()

# A class for the second window
class CreateInfoScreen(QDialog):
    # A function to initliaze QT wedgit
    def __init__(self):
        super(CreateInfoScreen, self).__init__()
        loadUi("search.ui",self)
        self.load()
        self.show.clicked.connect(self.displayinfo)

    # A function to provide functionality for second window
    def displayinfo(self):
        # Get text from feild
        ssn = self.idfeild.text()

        #check if empty
        if len(ssn)==0 :
            self.error.setText("Please input fields.")
        else:   
            # Connect to DB
            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "CompanyProj"
            )
            cur = mydb.cursor()
            # A query to return all information of employee of given ssn
            cur.execute("SELECT * FROM CompanyProj.employeeproj WHERE ssn ='"+ssn+"'")  
            self.error.setText("")
            # As tuple
            df = cur.fetchone()   
            
            for row in range(0,10):
                # Add elements to table
                self.tableWidget.setItem(0,row,QTableWidgetItem(str(df[row])))                   

    # A function with table property
    def load(self):
        # Table dimention
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(10)
        # Header
        self.tableWidget.setHorizontalHeaderLabels(('Fname','Minit','Lname','Ssn','BDate','Address','Sex','Salary','Super_Ssn','Dno'))
        # Size of columns
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,30)
        self.tableWidget.setColumnWidth(2,70)
        self.tableWidget.setColumnWidth(3,80)
        self.tableWidget.setColumnWidth(4,10)
        self.tableWidget.setColumnWidth(5,200)
        self.tableWidget.setColumnWidth(6,10)
        self.tableWidget.setColumnWidth(7,40)
        self.tableWidget.setColumnWidth(8,80)
        self.tableWidget.setColumnWidth(9,5)
    
# Main
app = QApplication(sys.argv)
login = LoginScreen() # log-in page
widget = QtWidgets.QStackedWidget()
widget.addWidget(login) 
# Window's size
widget.setFixedHeight(650)
widget.setFixedWidth(770)
widget.show() # Display
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
