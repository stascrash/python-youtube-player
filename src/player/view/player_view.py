from PyQt4.QtGui import QDialog, QVBoxLayout, QPalette, QFrame, QColor


class PlayerView(QDialog):
	def __init__(self):
		super(PlayerView, self).__init__()
		self._layout = QVBoxLayout()
		self.setLayout(self._layout)

		self.frame = QFrame()
		self._layout.addWidget(self.frame)

		self.set_pallet()

	def set_pallet(self):
		self.palette = self.frame.palette()
		self.palette.setColor(QPalette.Window, QColor(0, 0, 0))
		self.frame.setPalette(self.palette)
		self.frame.setAutoFillBackground(True)
