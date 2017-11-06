from PyQt4.Qt import QObject, pyqtSignal
from src.player.view.player_view import PlayerView
from src.player.player_model import VLCModel
import vlc


class PlayerObject(QObject):
	playback_started = pyqtSignal()
	playback_finished = pyqtSignal()

	def __init__(self):
		super(PlayerObject, self).__init__()
		self.frame_view = PlayerView()

		self.connect_signals()

	@property
	def window_id(self):
		return self.frame_view.frame.winId()

	def connect_signals(self):
		self.playback_started.connect(self.on_playback_started)
		self.playback_finished.connect(self.on_playback_finished)

	def on_playback_started(self):
		print("Showing frame_view from: {}".format(self.thread().objectName()))
		self.frame_view.exec_()

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

	def connect_signals(self):
		self.add.connect(self.on_add)
		self.play.connect(self.on_play)

	def playback_finished(self, event):
		print('End of media stream (event %s)' % event.type)
		self.player.playback_finished.emit()

	def on_play(self):
		self.player.playback_started.emit()
		self.vlc.player.set_hwnd(self.player.window_id)
		self.vlc.play()

	def pause(self):
		self.vlc.pause()

	def on_add(self, video_request):
		print("Adding: {}".format(video_request))
		# self.vlc.add(video_request)
