# from PyQt5.QtWidgets import QMainWindow
# from .view.player_view import Ui_VLCMainWindow
from .player_model import VLCPLayer
import os

# class VLCPLayerController(QMainWindow, Ui_VLCMainWindow):
class VLCPLayerController(object):
	def __init__(self, data_path):
		self.data_path = data_path
		self.player = VLCPLayer()

	def play(self):
		self.player.play()

	def pause(self):
		self.player.pause()

	def add(self, video_path):
		self.player.enqueue(video_path)

