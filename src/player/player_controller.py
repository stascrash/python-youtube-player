from PyQt4.Qt import QObject, pyqtSignal
from src.player.view.player_view import PlayerView
from src.player.player_model import VLCModel
import vlc
import logging


class PlayerObject(QObject):
	playback_started = pyqtSignal()
	playback_finished = pyqtSignal()

	def __init__(self):
		super(PlayerObject, self).__init__()
		self.frame_view = PlayerView()

		self.connect_signals()

	@property
	def window_id(self):
		win_id = self.frame_view.frame.winId()
		logging.debug("Player HWND: ".format(win_id))
		return win_id

	def connect_signals(self):
		self.playback_started.connect(self.on_playback_started)
		self.playback_finished.connect(self.on_playback_finished)

	def on_playback_started(self):
		print("Showing frame_view from: {}".format(self.thread().objectName()))
		self.frame_view.resize(800, 600)
		self.frame_view.show()

	def on_playback_finished(self):
		print("Closing frame_view from: {}".format(self.thread().objectName()))
		self.frame_view.close()


class VLCPLayerController(QObject):
	add = pyqtSignal(str)
	play = pyqtSignal()

	def __init__(self, data_path):
		super(VLCPLayerController, self).__init__()
		self.player = PlayerObject()

		self.vlc = VLCModel(data_path)
		self.vlc.event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.playback_finished)

		self.connect_signals()

	def connect_signals(self):
		self.add.connect(self.on_add)
		self.play.connect(self.on_play)

	def playback_finished(self, event):
		logging.debug('End of media stream (event {})'.format(event.type))
		self.player.playback_finished.emit()

	def on_play(self):
		logging.debug("Playing video on thread: {}".format(self.thread().objectName()))
		self.vlc.player.set_hwnd(self.player.window_id)
		self.player.playback_started.emit()
		self.vlc.play()

	def pause(self):
		self.vlc.pause()

	def on_add(self, video_request):
		logging.debug("Adding: {}".format(video_request))
		self.vlc.add(video_request)
