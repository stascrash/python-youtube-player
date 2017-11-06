import logging
from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.complex import Iterable
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11
from spyne.protocol.json import JsonDocument
from wsgiref.simple_server import make_server
from PyQt4.Qt import QObject
from spyne.server.twisted import TwistedWebResource

from twisted.internet import reactor
from twisted.web.server import Site
# from twisted.web.wsgi import WSGIResource
from twisted.python import log


class VLCService(ServiceBase):
	player_controller = None

	# RPC Calls. These do not need self, see details for 'srpc'
	@srpc(String) # String
	def add(video_request):
		VLCService.player_controller.add.emit(video_request)

	@srpc()
	def play():
		VLCService.player_controller.play.emit()

	# @srpc()
	# def pause():
	# 	VLCService.player_controller.pause()




class Services(QObject):

	def __init__(self):
		super(Services, self).__init__()

	def start_with_twisted_backend(self):
		PORT = 10200
		HOST = "192.168.1.44"

		logging.basicConfig(level=logging.DEBUG)
		logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

		observer = log.PythonLoggingObserver('twisted')
		log.startLoggingWithObserver(observer.emit, setStdout=False)

		application = Application([VLCService], 'spyne.vlc.service.http',
		                          in_protocol=Soap11(validator='lxml'),
		                          out_protocol=Soap11())

		logging.info('listening on: %s:%d' % (HOST, PORT))
		logging.info('wsdl is at: http://%s:%d/?wsdl' % (HOST, PORT))

		resource = TwistedWebResource(application)
		site = Site(resource)

		reactor.listenTCP(PORT, site, interface=HOST)
		reactor.run()

	def start(self):
		print("Starting on thread: {}".format(self.thread().objectName()))
		logging.basicConfig(level=logging.DEBUG)
		logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
		app = Application([VLCService], "spyne.vlc.service.http",
		                  in_protocol=Soap11(validator='soft'),
		                  out_protocol=Soap11())

		wsgi_app = WsgiApplication(app)
		server = make_server('192.168.1.44', 10200, wsgi_app)
		print("listening to http://192.168.1.44:10200")
		print("wsdl is at: http://192.168.1.44:10200/?wsdl")

		server.serve_forever()
