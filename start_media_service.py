from src.player.player_controller import VLCPLayerController
from src.server.controller import VLCService, ServiceController
from PyQt4.Qt import QApplication, QThread
import sys
import os
sys.path.append(os.path.dirname(__file__))


class ServiceThread(QThread):
	def __init__(self):
		QThread.__init__(self)
		self.service_controller = ServiceController()
		self.service = None

	def setup(self, player_controller):
		self.service = VLCService
		self.service.set_controller(player_controller)
		self.service_controller.moveToThread(self)

	def run(self):
		self.service_controller.start_all(self.service)



def start_server():
	data_path = os.path.join(os.path.dirname(__file__), 'data')
	player_controller = VLCPLayerController(data_path)

	services_thread = ServiceThread()
	services_thread.setup(player_controller)
	services_thread.start()

	while 1:
		pass



if __name__ == '__main__':
	app = QApplication(sys.argv)
	start_server()
	sys.exit(app.exec_())
