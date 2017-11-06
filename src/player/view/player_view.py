from PyQt4.QtGui import QDialog, QVBoxLayout, QPalette, QFrame, QColor, QMainWindow, QWidget


class PlayerView(QMainWindow):
	def __init__(self):
		super(PlayerView, self).__init__()
		self.widget = QWidget()
		self._layout = QVBoxLayout()
		self.setLayout(self._layout)
		self.setCentralWidget(self.widget)

		self.frame = QFrame()

		self.palette = self.frame.palette()
		self.palette.setColor(QPalette.Window, QColor(0, 0, 0))

		self.frame.setPalette(self.palette)
		self.frame.setAutoFillBackground(True)

		self._layout.addWidget(self.frame)
