from threading import Thread
from src.player.player_controller import VLCPLayerController
from src.server import ThreadedTCPServer
from PyQt5.QtWidgets import QApplication
import sys


def start_server():
	player_controller = VLCPLayerController()
	player_controller.show()

	media_server = ThreadedTCPServer(player_controller)

	media_server_thread = Thread(name="VLC-Media-Server", target=media_server.start)
	media_server_thread.setDaemon(True)
	media_server_thread.start()

	print("Server loop running in thread:", media_server_thread.name)

	# try:
	# 	while True:
	# 		pass
	# except KeyboardInterrupt:
	# 	print("\nServer Interrupted")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	start_server()
	sys.exit(app.exec_())
