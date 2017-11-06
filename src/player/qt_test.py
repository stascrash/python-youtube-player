import sys
from PyQt4.Qt import QApplication, QTimer, QThread, QObject, pyqtSignal
from PyQt4.QtGui import QWidget, QSystemTrayIcon, QDialog, QVBoxLayout, QLabel, QIcon, QMenu







class PlayerThread(QThread):
	def __init__(self, p):
		super(PlayerThread, self).__init__(p)
		self.setObjectName("Dialog-Thread")


class RPCThread(QThread):
	def __init__(self, p):
		super(RPCThread, self).__init__(p)
		self.setObjectName("RPC-Thread")


class Systray(QSystemTrayIcon):

	def __init__(self, icon, parent):
		super(Systray, self).__init__(icon, parent)

		self.menu = QMenu(parent)
		self.exitAction = self.menu.addAction("Exit")
		self.setContextMenu(self.menu)

		self.exitAction.triggered.connect(self.hide)

		self.timer_on = QTimer()
		self.timer_off = QTimer()

		self.player = PlayerObject()

		self.timer_on.timeout.connect(self.player.show_dialog.emit)
		self.timer_off.timeout.connect(self.player.close_dialog.emit)

		self.t = PlayerThread(parent)
		self.player.moveToThread(self.t)
		self.t.start()

		self.start_timers()
		
	def hide(self):
		self.timer_on.stop()
		self.timer_off.stop()
		if self.t.isRunning():
			print("Terminating {}".format(self.t.objectName()))
			self.t.terminate()
			self.t.wait()
		print("Exiting")
		super(Systray, self).hide()
		app = QApplication.instance()
		app.exit(0)


	def start_timers(self):
		self.timer_on.start(3000)
		self.timer_off.start(3500)





if __name__ == '__main__':
	print("Starting")
	app = QApplication(sys.argv)
	app.setQuitOnLastWindowClosed(False)
	icon = QIcon("fire.ico")
	parent = QWidget()
	tray = Systray(icon, parent)
	tray.show()
	sys.exit(app.exec_())







# ---------------------------------
# import sys
# from PyQt4 import QtGui
#
# class SystemTrayIcon(QtGui.QSystemTrayIcon):
#
#     def __init__(self, icon, parent=None):
#         QtGui.QSystemTrayIcon.__init__(self, icon, parent)
#         menu = QtGui.QMenu(parent)
#         exitAction = menu.addAction("Exit")
#         self.setContextMenu(menu)
#
# def main():
#     app = QtGui.QApplication(sys.argv)
#
#     w = QtGui.QWidget()
#     trayIcon = SystemTrayIcon(QtGui.QIcon("fire.ico"), w)
#
#     trayIcon.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()