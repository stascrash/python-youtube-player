import sys
import os
sys.path.append(os.path.dirname(__file__))


from PyQt4.Qt import QApplication
from PyQt4.QtGui import QWidget, QIcon
from src.server import service_app
import logging
LOGGER = logging.getLogger()


def main():
	LOGGER.debug("Starting")
	app = QApplication(sys.argv)
	app.setQuitOnLastWindowClosed(False)

	icon = QIcon("data/fire.ico")
	parent = QWidget()

	data_path = os.path.join(os.path.dirname(__file__), 'data')

	tray = service_app.Systray(icon, parent, data_path)
	tray.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

