import vlc
from src.youtube_lib import YouTubePlayer


class VLCPLayer(YouTubePlayer):
	def __init__(self):
		YouTubePlayer.__init__(self)
		self.instance = vlc.get_default_instance()
		self.playlist = self.instance.media_list_new()
		self.player = self.instance.media_player_new()
		self.list_player = self.instance.media_list_player_new()
		self.list_player.set_media_player(self.player)
		self.list_player.set_media_list(self.playlist)
		self.event_manager = self.player.event_manager()




class VLCPLayerModel(object):
	def __init__(self):
		self.player = VLCPLayer()

	def play(self):
		self.player.play()

	def pause(self):
		self.player.pause()

	def add_to_yt_que(self, yt_vid):
		self.player.enqueue(yt_vid)
