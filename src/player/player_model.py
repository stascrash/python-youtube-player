import vlc
from src.youtube_lib import YouTubePlayer
from src.youtube_lib import YouTubeVideo
import os
from collections import namedtuple


class VLCPLayer(YouTubePlayer):
	def __init__(self):
		super(VLCPLayer, self).__init__()
		self.instance = vlc.get_default_instance()
		self.playlist = self.instance.media_list_new()
		self.player = self.instance.media_player_new()
		self.list_player = self.instance.media_list_player_new()
		self.list_player.set_media_player(self.player)
		self.list_player.set_media_list(self.playlist)
		self.event_manager = self.player.event_manager()


class VLCModel(VLCPLayer):
	def __init__(self, data_path):
		super(VLCModel, self).__init__()
		self.data_path = data_path

	def add(self, video_request):
		try:
			yt_vid = YouTubeVideo.get_instance(video_request)
		except ValueError:
			data = namedtuple("Yt_vid", ("stream_url",))
			path = os.path.join(self.data_path, video_request)
			yt_vid = data(stream_url=os.path.normpath(path))
		self.add_to_yt_que(yt_vid)

	def add_to_yt_que(self, yt_vid):
		self.enqueue(yt_vid)
