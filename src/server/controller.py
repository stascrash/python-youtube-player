import logging
from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.complex import Iterable
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11
from wsgiref.simple_server import make_server

from src.youtube_lib import YouTubeVideo
import os
from collections import namedtuple

from PyQt4.Qt import QObject

class VLCService(ServiceBase):
	player_controller = None

	@staticmethod
	def set_controller(player_controller_instance):
		print("Setting controller")
		VLCService.player_controller = player_controller_instance

	# RPC Calls. These do not need self, see details for 'srpc'
	@srpc(String, _returns=String)
	def add(video_request):
		try:
			yt_vid = YouTubeVideo.get_instance(video_request)
		except ValueError:
			data = namedtuple("Yt_vid", ("stream_url",))
			path = os.path.join(VLCService.player_controller.data_path, video_request)
			yt_vid = data(stream_url=os.path.normpath(path))

		VLCService.player_controller.add(yt_vid)
		return "Received: {}".format(video_request)

	@srpc()
	def pause():
		VLCService.player_controller.pause()

	@srpc()
	def play():
		VLCService.player_controller.play()


class ServiceController(QObject):
	def start_all(self, *services):
		start_services(*services)


def start_services(*services):
	logging.basicConfig(level=logging.DEBUG)
	logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

	app = Application(services, "spyne.vlc.service.http",
	                  in_protocol=Soap11(validator='lxml'),
	                  out_protocol=Soap11())

	wsgi_app = WsgiApplication(app)
	server = make_server('192.168.1.44', 10200, wsgi_app)
	print("listening to http://192.168.1.44:10200")
	print("wsdl is at: http://192.168.1.44:10200/?wsdl")

	server.serve_forever()
