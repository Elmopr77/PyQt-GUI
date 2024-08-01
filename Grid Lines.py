import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5 import QtCore

class GridWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Simple PyQt App with Grid")
		self.setFixedSize(800, 600)
		
		# Create a QLabel to display a message
		self.label = QLabel("<h1>Hello, World!</h1>", parent=self)
		self.label.move(50, 100)
		
	def paintEvent(self, event):
		painter = QPainter(self)
		pen = QPen(QColor(200, 200, 200), 1, QtCore.Qt.SolidLine)
		painter.setPen(pen)
		
		# Draw vertical lines
		for x in range(0, self.width(), 20):  # Change 20 to adjust spacing
			painter.drawLine(x, 0, x, self.height())
		
		# Draw horizontal lines
		for y in range(0, self.height(), 20):  # Change 20 to adjust spacing
			painter.drawLine(0, y, self.width(), y)
		
# Create a QApplication instance
app = QApplication(sys.argv)

# Create and show the main window
window = GridWindow()
window.show()

# Start the app event loop
sys.exit(app.exec_())
			
