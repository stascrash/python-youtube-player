import sys, vlc, pafy  # https://github.com/mps-youtube/pafy
import json


class YouTubeVideo():
	def __init__(self, name='', url='', stream_url='', duration='', owner='anonymous'):
		self.name = name
		self.url = url
		self.stream_url = stream_url
		self.duration = duration
		self.owner = owner

	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)  # , indent=2)

	@staticmethod
	def from_JSON(data):
		data = json.loads(data)
		titl = data["name"]
		url = data["url"]
		str_u = data["stream_url"]
		dur = data["duration"]
		ownr = data["owner"]

		return YouTubeVideo(titl, url, str_u, dur, ownr)

	@staticmethod
	def get_instance(url):
		video = pafy.new(url)
		titl = video.title
		url = url
		str_u = video.getbest().url
		dur = video.duration

		return YouTubeVideo(titl, url, str_u, dur)


class YouTubePlayer:
	def __init__(self):
		# --no-xlib --no-stats --no-video
		self.instance = vlc.Instance("--no-video")
		self.playlist = self.instance.media_list_new()
		self.player = self.instance.media_player_new()
		self.list_player = self.instance.media_list_player_new()
		self.list_player.set_media_player(self.player)
		self.list_player.set_media_list(self.playlist)
		self.event_manager = self.list_player.event_manager()

	def play(self):
		print("I need to play")
		self.list_player.play()
		return

	def pause(self):
		self.list_player.pause()
		return

	def stop(self):
		self.list_player.stop()

		return

	def next(self):
		self.list_player.next()

	def is_playing(self):
		return self.list_player.is_playing()

	def get_nowplaying_idx(self):
		media = self.player.get_media()
		if media is None:
			return -1
		else:
			return self.playlist.index_of_item(media)

	def enqueue(self, yt_vid):
		print("I need to Que: {}".format(yt_vid.stream_url))
		self.playlist.lock()
		media = self.instance.media_new(yt_vid.stream_url)
		media.parse()
		# meta = vlc.Meta()
		# media.set_meta(0, yt_vid.name)
		# media.set_meta(6, yt_vid.to_JSON())
		self.playlist.add_media(media)
		# print "playlist size is now", self.playlist.count()
		self.playlist.unlock()

		# arr = [url for url in self.queue.queue]
		# print "QUEUE:"
		# index = 1
		# for url in arr:
		#     print "  ", index, ": ", url
		#     index += 1
		# return

	def set_volume(self, perc):
		# vol = int(1024 * perc / 100)
		self.player.audio_set_volume(perc)
		print(self.player.audio_get_volume())

	def get_nowplaying(self):
		media = self.player.get_media()
		if media is None:
			return {}
		else:
			return media.get_meta(6)
			# pass

	def get_playlist(self):
		cnt = self.playlist.count()
		l = []
		for i in range(0, cnt):
			vid = self.playlist.item_at_index(i).get_meta(6)
			jvid = json.loads(vid)
			jvid["stream_url"] = ""
			l.append(json.dumps(jvid))
		return json.dumps(l)

	def get_queue(self):
		media = self.player.get_media()
		idx = self.playlist.index_of_item(media)
		if idx < 0:
			idx = 0
		cnt = self.playlist.count()
		l = []
		if cnt > 0:
			for i in range(idx, cnt):
				vid = self.playlist.item_at_index(i).get_meta(6)
				jvid = json.loads(vid)
				jvid["stream_url"] = ""
				l.append(json.dumps(jvid))
		return json.dumps(l)

	@vlc.callbackmethod
	def end_callback(self, event):
		self.next()

	@vlc.callbackmethod
	def pos_callback(self, event):
		# if echo_position:
		# sys.stdout.write('\r%s to %.2f%% (%.2f%%)' % (event.type,
		#                                               event.u.new_position * 100,
		#                                               player.get_position() * 100))
		# sys.stdout.flush()
		pass


def main():
	# pass
	video = YouTubeVideo.get_instance("https://www.youtube.com/watch?v=bpOSxM0rNPM")
	print(video.to_JSON())
	# video = YouTubeVideo.from_JSON(video.to_JSON())
	# print video.name


if __name__ == '__main__':
	main()
