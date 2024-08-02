import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class LoginFormApp(QMainWindow):
	def __init__(self):
		super().__init__()
		
		#Set the window properties (title and initial size)
		self.setWindowTitle("Login Form")
		self.setGeometry(100, 100, 300, 150) #(X, y, width, height)
		
		#Create a central widget for the main window
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		
		#Create a QformLayout to arrange the widgets 
		form_layout = QFormLayout()
		
		#Create QLabel and QLineEdit widgets for email
		email_label = QLabel("Email:")
		self.email_field = QLineEdit()
		
		#Create QLabel and QLineEdit widgets for password
		password_label = QLabel("Password:")
		self.password_field = QLineEdit()
		self.password_field.setEchoMode(QLineEdit.Password) #Hide password input 
		
		#Create a QPushButton for login
		login_button = QPushButton("Login")
		login_button.clicked.connect(self.login)
		
		#Add widgets to the form layout
		form_layout.addRow(email_label, self.email_field)
		form_layout.addRow(password_label, self.password_field)
		form_layout.addRow(login_button)
		
		#Set the layout for the central widget
		central_widget.setLayout(form_layout)
		
	def login(self):
		#Retrieve the email and password entered by the user
		email = self.email_field.text()
		password = self.password_field.text()
		
		#Check if the email and password are valid
		if email == "abc@gmail.com" and password == "abc123":
			QMessageBox.information(self, "Login Successful", f"Welcome, {email}!")
		else:
			QMessageBox.warning(self, "Login Failed", "Invalid email or password. Please try again.")
def main():
	app = QApplication(sys.argv)
	window = LoginFormApp()
	window.show()
	sys.exit(app.exec_())
	
if __name__ == "__main__":
	main()
		
		
		
