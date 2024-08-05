import sys
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class AccountCreation(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Login Settup")
        self.setFixedSize(400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        form_layout = QFormLayout()

        welcomeLabel = QLabel("Hello")
        welcomeLabel.move(30, 30)

        emailLabel = QLabel("Email:")
        self.email_field = QLineEdit()
        

        passwordLabel = QLabel("Password:")
        self.password_field = QLineEdit()

        createAccountButton = QPushButton("Create new account")
        createAccountButton.clicked.connect(self.accountSaved)

        form_layout.addRow(emailLabel, self.email_field)
        form_layout.addRow(passwordLabel, self.password_field)
        form_layout.addRow(createAccountButton)

        central_widget.setLayout(form_layout)

    def accountSaved(self):
        account1 = []
        email = self.email_field.text()
        password = self.password_field.text()

        if "@" in email and len(password) >= 5:
            account1.append(email)
            account1.append(password)
            
            with open('account1', 'wb') as f:
                pickle.dump(account1, f)

            QMessageBox.information(self, "Your account has been succesfully created.", f"Welcome {email}.")

        else:
            QMessageBox.warning(self, "Failed to create account!", "Please enter a valid email or password.")


def main():
    app = QApplication(sys.argv)
    window = AccountCreation()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
