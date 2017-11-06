from PyQt4.QtGui import QMainWindow, QPalette, QColor
from .view.player_view import Ui_VLCMainWindow
from .player_model import VLCPLayer
import vlc


class VLCPLayerController(QMainWindow, Ui_VLCMainWindow):
	playing = False

	def __init__(self, data_path):
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.set_pallet()

		self.data_path = data_path
		self.vlc = VLCPLayer()

		self.vlc.event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.playback_finished)

	def set_pallet(self):
		self.palette = self.frame.palette()
		self.palette.setColor(QPalette.Window, QColor(0, 0, 0))
		self.frame.setPalette(self.palette)
		self.frame.setAutoFillBackground(True)

	def playback_finished(self, event):
		print('End of media stream (event %s)' % event.type)
		VLCPLayerController.playing = False

	def play(self):
		self.vlc.player.set_hwnd(self.frame.winId())
		self.vlc.play()
		self.show()
		VLCPLayerController.playing = True
		while VLCPLayerController.playing:
			pass
		print("Finished playing")
		self.close()

	def pause(self):
		self.vlc.pause()

	def add(self, video_path):
		self.vlc.enqueue(video_path)
