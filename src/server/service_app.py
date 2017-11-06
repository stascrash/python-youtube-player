from PyQt4.Qt import QApplication, QThread
from PyQt4.QtGui import QSystemTrayIcon, QMenu
from src.player.player_controller import VLCPLayerController
from src.server.services_controller import Services, VLCService


class Systray(QSystemTrayIcon):
	def __init__(self, icon, parent, data_path):
		super(Systray, self).__init__(icon, parent)
		self.init_systray(parent)

		self.player = VLCPLayerController(data_path)
		self.player_thread = QThread(parent)
		self.player_thread.setObjectName("VLC Player Thread")
		self.player.moveToThread(self.player_thread)
		self.player_thread.start()

		VLCService.player_controller = self.player
		self.services = Services()
		self.services_thread = QThread(parent)
		self.services_thread.setObjectName("RPC Services Thread")
		self.services.moveToThread(self.services_thread)
		self.services_thread.start()
		self.services.start_with_twisted_backend()

	def init_systray(self, parent):
		self.menu = QMenu(parent)
		self.exit = self.menu.addAction("Exit")
		self.setContextMenu(self.menu)
		self.exit.triggered.connect(self.hide)

	def hide(self):
		self.timer_on.stop()
		self.timer_off.stop()

		if self.player_thread.isRunning():
			print("Terminating {}".format(self.player_thread.objectName()))
			self.player_thread.terminate()
			self.player_thread.wait()

		print("Exiting")
		super(Systray, self).hide()
		app = QApplication.instance()
		app.exit(0)
