# from PyQt5.QtWidgets import QMainWindow
# from .view.player_view import Ui_VLCMainWindow
from .player_model import VLCPLayer
import vlc
import os


# class VLCPLayerController(QMainWindow, Ui_VLCMainWindow):
class VLCPLayerController(object):
	playing = False

	def __init__(self, data_path):
		self.data_path = data_path
		self.player = VLCPLayer()

		self.player.event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.playback_finished)

	def playback_finished(self, event):
		print('End of media stream (event %s)' % event.type)
		VLCPLayerController.playing = False

	def play(self):
		self.player.play()
		VLCPLayerController.playing = True
		while VLCPLayerController.playing:
			pass
		print("Finished playing")


	def pause(self):
		self.player.pause()

	def add(self, video_path):
		self.player.enqueue(video_path)

