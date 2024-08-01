import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

#Create a QApplication instance
app = QApplication(sys.argv)

#Create a QWidget, which will serve as the main window 
window = QWidget()

#Set the window title
window.setWindowTitle("Simple PyQt Application")

#Set the window size (width, height)
window.setGeometry(100, 100, 400, 300)

#Create a QLabel to display a message
label = QLabel("<h1>Hello, World!</h1>", parent=window)

#Move the label to a specific postion within the window
label.move(100, 100)

#Show the window
window.show()

#Start the application's event loop
sys.exit(app.exec_())

