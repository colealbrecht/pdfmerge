# This is a custom QListWidget that allows for dragging and dropping files
# into the listbox

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class DDListWidget(QtWidgets.QListWidget):

	def __init__(self, parent=None):
		super(DDListWidget, self).__init__(parent)

	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.accept()
		else:
			super(DDListWidget, self).dragEnterEvent(event)

	def dragMoveEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(QtCore.Qt.CopyAction)
			event.accept()
		else:
			super(DDListWidget, self).dragMoveEvent(event)

	def dropEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(QtCore.Qt.CopyAction)
			event.accept()

			files = []
			for url in event.mimeData().urls():
				files.append(str(url.toLocalFile()))
			self.addItems(files)

		else:
			event.setDropAction(QtCore.Qt.MoveAction)
			super(DDListWidget, self).dropEvent(event)
