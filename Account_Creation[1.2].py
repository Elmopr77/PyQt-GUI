import sys
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout

class AccountCreation(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Login Settup")
        self.setFixedSize(400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QFormLayout()

        welcomeLabel = QLabel("Create a new account:")

        emailLabel = QLabel("Email:")
        self.email_field = QLineEdit()
        
        passwordLabel = QLabel("Password:")
        self.password_field = QLineEdit()

        self.createAccountButton = QPushButton("Create account")
        self.createAccountButton.clicked.connect(self.accountSaved)
        self.createAccountButton.clicked.connect(self.accountLogin)

        self.layout.addRow(welcomeLabel)
        self.layout.addRow(emailLabel, self.email_field)
        self.layout.addRow(passwordLabel, self.password_field)
        self.layout.addRow(self.createAccountButton)

        central_widget.setLayout(self.layout)

    def accountSaved(self):
        account1 = []
        email = self.email_field.text()
        password = self.password_field.text()

        if "@" in email and len(password) >= 5:
            account1.append(email)
            account1.append(password)
            
            with open('account1.pkl', 'wb') as f:
                pickle.dump(account1, f)

        else:
            QMessageBox.warning(self, "Failed to create account!", "Please enter a valid email or password.")

    def accountLogin(self):
        #Clear the layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().deleteLater()
        
        #Add login widgets
        self.layout.addWidget(QLabel("Login to your newly created account."))
        
        emailAccessLabel = QLabel("Email:")
        self.emailAcess_field = QLineEdit()

        passwordAccesslabel = QLabel("Password:")
        self.passwordAccess_field = QLineEdit()

        self.loginButton = QPushButton("Login")
        self.loginButton.clicked.connect(self.accountAccess)

        self.layout.addRow(emailAccessLabel, self.emailAcess_field)
        self.layout.addRow(passwordAccesslabel, self.passwordAccess_field)
        self.layout.addRow(self.loginButton)

    def accountAccess(self):
        with open('account1.pkl', 'rb') as f:
            ac1 = pickle.load(f)
        
        emailLogin = self.emailAcess_field.text()
        passwordLogin = self.passwordAccess_field.text()
        loginTries = 0

        while loginTries <= 5:
            if (emailLogin == ac1[0]) and (passwordLogin == ac1[1]):
                self.homeWindow()
                break
            else:
                QMessageBox.warning(self, "Login failed", "Please enter the correct email or password.")
                loginTries += 1
                break

                if loginTries == 5:
                    QMessageBox.warning(self, "Account access blocked", "To many tries have been entered.")
                    
    
    def homeWindow(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().deleteLater()

        self.layout.addWidget(QLabel("Welcome to the Home Window"))
        




def main():
    app = QApplication(sys.argv)
    window = AccountCreation()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
