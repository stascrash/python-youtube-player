from PyQt5.QtWidgets import QMainWindow
from .view.player_view import Ui_VLCMainWindow
from .player_model import VLCPLayer


class VLCPLayerController(QMainWindow, Ui_VLCMainWindow):
	def __init__(self):
		super(VLCPLayerController, self).__init__()
		self.setupUi(self)
		self.player = VLCPLayer()

	def play(self):
		self.player.play()

	def add(self, yt_vid):
		self.player.enqueue(yt_vid)

