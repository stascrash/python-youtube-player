import vlc
# from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from src.youtube_lib import YouTubePlayer


class VLCPLayer(YouTubePlayer):
	def __init__(self):
		super(VLCPLayer, self).__init__()

		self.instance = vlc.get_default_instance()
		self.playlist = self.instance.media_list_new()
		self.player = self.instance.media_player_new()
		self.list_player = self.instance.media_list_player_new()
		self.list_player.set_media_player(self.player)
		self.list_player.set_media_list(self.playlist)
		self.event_manager = self.list_player.event_manager()


# class VLCPLayerModel(QObject):
class VLCPLayerModel(object):
	# on_play = pyqtSignal()
	# on_yt_que_add = pyqtSignal("PyQt_PyObject")

	def __init__(self):
		super(VLCPLayerModel, self).__init__()
		self.player = VLCPLayer()

	# @pyqtSlot(name="play")
	def play(self):
		print("Playing...")
		self.player.play()

	# @pyqtSlot(object, name="add")
	def add_to_yt_que(self, yt_vid):
		print("Adding...")
		self.player.enqueue(yt_vid)
