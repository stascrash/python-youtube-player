from threading import Thread
from src.player.player_controller import VLCPLayerController
from src.server.controller import VLCService, start_services
# from PyQt5.QtWidgets import QApplication
import sys
import os
sys.path.append(os.path.dirname(__file__))

def start_server():
	data_path = os.path.join(os.path.dirname(__file__), 'data')
	player_controller = VLCPLayerController(data_path)
	vlc_service = VLCService
	vlc_service.set_controller(player_controller)
	media_server_thread = Thread(name="VLC-Media-Server", target=start_services, args=(vlc_service, ))
	media_server_thread.setDaemon(True)
	media_server_thread.start()

	print("Server loop running in thread:", media_server_thread.name)

	try:
		while True:
			pass
	except KeyboardInterrupt:
		print("\nServer Interrupted")


if __name__ == '__main__':
	# app = QApplication(sys.argv)
	start_server()
	# sys.exit(app.exec_())
