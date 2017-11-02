#! /usr/bin/python
# from PyQt5.QtCore import QObject, pyqtSignal
import socketserver
import json
import netifaces
from urllib.parse import urlencode
from src.youtube_lib import YouTubeVideo


def search(query):
	import youtube_dl

	search_query = {'search_query': query}
	url = 'https://www.youtube.com/results?' + urlencode(search_query)

	ydl_opts = {'quiet': True, 'max_downloads': 10}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		result = ydl.extract_info(url, download=False, process=False)

	names = []
	ids = []

	if 'entries' in result:
		for vid in result['entries']:
			if "/watch?v=" in vid['url']:
				names.append(vid['title'])
				ids.append(vid['url'])
	else:
		names.append(result['title'])
		ids.append(result['url'])

	return {'names': names, 'ids': ids}


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
	def handle(self):

		data = self.request.recv(1024 * 2).strip().decode()
		if " " not in data:
			data += " "
		print(">> {}".format(data))

		response_data = ""
		response_code = 200

		command, args = data.split(' ', 1)
		if command == "/play":
			self.server.player.play()
		elif command == "/pause":
			self.server.player.pause()
		elif command == "/next":
			self.server.player.next()
		elif command == "/add":
			if args:
				yt_vid = YouTubeVideo.get_instance(args)
				# self.server.playlist.append(yt_vid)
				# self.server.player.enqueue(yt_vid)
				self.server.player.add(yt_vid)
		elif command == "/vol":
			if args:
				self.server.player.set_volume(int(args))
		elif command == "/search":
			if args:
				response_code = 300
				response_data = json.dumps(search(args))
		elif command == "/nowplaying":
			response_code = 200
			response_data = self.server.player.get_nowplaying()
		elif command == "/playlist":
			response_code = 100
			response_data = self.server.player.get_playlist()
		elif command == "/queue":
			response_code = 101
			response_data = self.server.player.get_queue()
		elif command == "/isplaying":
			response_code = 102
			response_data = self.server.player.is_playing()
		elif command == "/nowplayingidx":
			response_code = 103
			response_data = self.server.player.get_nowplaying_idx()

		response = "{} {}".format(response_code, response_data)
		self.request.sendall(response.encode())


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
	def __init__(self, player_controller):
		socketserver.TCPServer.__init__(self, (self.get_ip(), 10200), ThreadedTCPRequestHandler)
		self.player = player_controller

	def get_ip(self):
		for interface in netifaces.interfaces():
			try:
				ip_address = netifaces.ifaddresses(interface)[2][0]['addr']
				if ip_address != "127.0.0.1":
					return ip_address
			except KeyError:
				pass
		raise ValueError("Cannot obtain IP address. Check your internet connection")

	def start(self):
		ip, port = self.server_address
		print("Server running at:", ip, port)
		self.serve_forever()
		# server_thread = threading.Thread(name="thr_server", target=server.serve_forever)

# if __name__ == "__main__":
# 	player = YouTubePlayer()
# 	playlist = []
#
# 	HOST = get_ip()
# 	PORT = 10200
#
# 	server = ThreadedTCPServer((HOST, PORT), player, playlist)
#
# 	ip, port = server.server_address
# 	print("Server running at:", ip, port)
# 	server_thread = threading.Thread(name="thr_server", target=server.serve_forever)
# 	server_thread.daemon = True
# 	server_thread.start()
# 	print("Server loop running in thread:", server_thread.name)
#
# 	try:
# 		while True:
# 			pass
# 	except KeyboardInterrupt:
# 		print("\nServer Interrupted")
#
# 	print("stopping player")
# 	player.stop()
# 	print("shutting down")
# 	server.shutdown()
# 	print("closing server")
# 	server.server_close()
# 	print("Bye")
