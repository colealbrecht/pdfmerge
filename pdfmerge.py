# Import sys for args
import sys

# Import pikepdf for manipulating PDFs
from pikepdf import Pdf

# Import PyQt5 for GUI Components
from PyQt5 import uic
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog, QMainWindow, QApplication


class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		
		super().__init__(*args, **kwargs)
		uic.loadUi("mainwindow.ui", self)

		self.btnAdd.clicked.connect(self.openFileNamesDialog)
		self.btnRemove.clicked.connect(self.removeFilesFromList)
		self.btnCombine.clicked.connect(self.mergeFiles)

	# Open the File Browser for opening multiple files
	def openFileNamesDialog(self):
		
		self.statusbar.showMessage("")

		options = QFileDialog.Options()
		
		files, _ = QFileDialog.getOpenFileNames(self, "Add PDFs", "", "PDF Files (*.pdf);;All Files (*)", options=options)
		if files:
			self.lstFiles.addItems(files)

	# Open the File Browser for saving a file
	def openSaveFileDialog(self):

		options = QFileDialog.Options()

		filename, _ = QFileDialog.getSaveFileName(self, "Save Combined PDF As", "", "PDF Files (*.pdf);;All Files (*)", options=options)
		if filename:
			return filename


	# Remove the selected files from the listbox
	def removeFilesFromList(self):
		
		for item in self.lstFiles.selectedItems():
			self.lstFiles.takeItem(self.lstFiles.row(item))


	# Merge the files in the listbox
	def mergeFiles(self):
		
		if self.lstFiles.count():

			outfile = self.openSaveFileDialog()
			
			# Only merge the pdfs if there is an output filename
			if outfile:

				self.statusbar.showMessage("Combining...")

				pdf = Pdf.new()	

				# Combine PDFs
				for i in range(0, self.lstFiles.count()):
					pdf.pages.extend(Pdf.open(self.lstFiles.item(i).text()).pages)

				# Save file
				pdf.save(outfile)

				# Clear files from list
				self.clearFilesFromList()

				self.statusbar.showMessage("Success. Saved file %s" % (outfile))


	# Clear all files from the listbox
	def clearFilesFromList(self):

		self.lstFiles.clear()

if __name__ == "__main__":
	
	# Start the app
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()