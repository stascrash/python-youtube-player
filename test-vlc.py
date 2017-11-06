from suds.client import Client
import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

vlc_client = Client('http://192.168.1.44:10200/?wsdl')

# vlc_client.service.add("https://www.youtube.com/watch?v=_V7ZKk-NJVA")
vlc_client.service.add("https://www.youtube.com/watch?v=_V7ZKk-NJVA")
# vlc_client.service.add("maya.mov")
# vlc_client.service.pause()
vlc_client.service.play()















# import vlc
# import sys
# from PyQt5 import QtGui, QtCore, QtWidgets
# import youtube_dl
#
# class Player(QtWidgets.QMainWindow):
# 	def __init__(self):
# 		super(Player, self).__init__()
# 		self.instance = vlc.get_default_instance()
# 		self.player = self.instance.media_player_new()
#
# 		self.build_ui()
# 		self.play_url()
#
# 	def build_ui(self):
# 		self.widget = QtWidgets.QWidget(self)
# 		self.setCentralWidget(self.widget)
# 		self.frame = QtWidgets.QFrame()
# 		self.layout = QtWidgets.QHBoxLayout()
# 		self.palette = self.frame.palette()
# 		self.palette.setColor(QtGui.QPalette.Window,
# 							  QtGui.QColor(0, 0, 0))
# 		self.frame.setPalette(self.palette)
# 		self.frame.setAutoFillBackground(True)
# 		self.layout.addWidget(self.frame)
# 		self.widget.setLayout(self.layout)
#
# 	def play_url(self):
# 		print("Trying to play")
# 		# media = self.instance.media_new(r"https://www.youtube.com/watch?v=FJT8lPtWkAQ")
# 		media = self.instance.media_new("test")
# 		# media = self.instance.media_new(r"C:\Users\stasc\Desktop\Maya-Python-API\maya_python_0000.mp4")
# 		self.player.set_media(media)
# 		self.player.set_hwnd(self.frame.winId())
# 		self.player.play()
#
#
# if __name__ == "__main__":
# 	app = QtWidgets.QApplication(sys.argv)
# 	player = Player()
# 	player.show()
# 	player.resize(640, 480)
# 	# if sys.argv[1:]:
# 	# 	player.OpenFile(sys.argv[1])
# 	sys.exit(app.exec_())
#
# # player.media_new("https://www.youtube.com/watch?v=FJT8lPtWkAQ")
