import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

#Create a QApplication instance
app = QApplication(sys.argv)

#Create a QWidget, which will serve as the main window
window = QWidget()

#Set the window title
window.setWindowTitle("Simple PyQt App")

#Set the window size (width, height)
window.setFixedSize(800, 600) #Set fixed size instead of setGeometry

#Create a QLabel to display a message
label = QLabel("<h1>Hello, World!</h1>", parent=window)

#Move the label to a specific postition within the window
label.move(50, 100)

#Show the window
window.show()

#Start the app event loop
sys.exit(app.exec_())
