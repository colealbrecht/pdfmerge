# Standard libraries
import sys
import os

# Import pikepdf for manipulating PDFs
import pikepdf
from pikepdf import Pdf, OutlineItem

# Import PyQt5 for GUI Components
from PyQt5 import uic
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog, QMainWindow, QApplication

# Import the Ui
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		
		super(MainWindow, self).__init__(*args, **kwargs)

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Connect buttons to functions
		self.ui.btnAdd.clicked.connect(self.openFileNamesDialog)
		self.ui.btnRemove.clicked.connect(self.removeFilesFromList)
		self.ui.btnUnsecure.clicked.connect(self.removeSecurityFromFiles)
		self.ui.btnCombine.clicked.connect(self.mergeFiles)

	# Open the File Browser for opening multiple files
	def openFileNamesDialog(self):
		
		self.ui.statusbar.showMessage("")

		options = QFileDialog.Options()
		
		files, _ = QFileDialog.getOpenFileNames(self, "Add PDFs", "", "PDF Files (*.pdf);;All Files (*)", options=options)
		if files:
			self.ui.lstFiles.addItems(files)


	# Open the File Browser for saving a file
	def openSaveFileDialog(self):

		options = QFileDialog.Options()

		filename, _ = QFileDialog.getSaveFileName(self, "Save Combined PDF As", "", "PDF Files (*.pdf);;All Files (*)", options=options)
		if filename:
			return filename


	# Remove the selected files from the listbox
	def removeFilesFromList(self):
		
		for item in self.ui.lstFiles.selectedItems():
			self.ui.lstFiles.takeItem(self.ui.lstFiles.row(item))


	# Merge the files in the listbox
	def mergeFiles(self):
		
		# Only try to combine if files have been added to the list
		# Allow for a single pdf to be 'combined', in this case it will just remove security if there is any
		if self.ui.lstFiles.count():

			outfile = self.openSaveFileDialog()
			
			# Only merge the pdfs if there is an output filename
			if outfile:

				self.ui.statusbar.showMessage("Combining...")

				output = Pdf.new()

				page_count = 0

				try:

					with output.open_outline() as outline:
						# Combine PDFs
						for i in range(0, self.ui.lstFiles.count()):
						
							filename = self.ui.lstFiles.item(i).text()

							with Pdf.open(filename) as pdf:

								oi = OutlineItem(os.path.basename(filename), page_count)
								outline.root.append(oi)
								page_count += len(pdf.pages)
								output.pages.extend(pdf.pages)


					# Save file
					output.save(outfile)

					# Clear files from list
					self.clearFilesFromList()

					# Update statusbar with success message
					self.ui.statusbar.showMessage("Success. Saved file '%s'" % (os.path.basename(outfile)))


				# If combining the PDFs fails
				except:

					# Update the statusbar with an error message with the file that caused it to fail
					self.ui.statusbar.showMessage("Error processing '%s'" % (os.path.basename(filename)))
					output.close()

	# Remove the Security settings from all files in the listbox
	def removeSecurityFromFiles(self):

		# Only try to combine if files have been added to the list
		# Allow for a single pdf to be 'combined', in this case it will just remove security if there is any
		if self.ui.lstFiles.count():

			self.ui.statusbar.showMessage("Removing security from PDFs...")


			try:

				for i in range(0, self.ui.lstFiles.count()):

					output = Pdf.new()

					page_count = 0

					filename = self.ui.lstFiles.item(i).text()

					outfile = filename.replace(".pdf", "-UNSECURED.pdf")

					with output.open_outline() as outline:
						with Pdf.open(filename) as pdf:

							oi = OutlineItem(os.path.basename(filename), page_count)
							outline.root.append(oi)
							page_count += len(pdf.pages)
							output.pages.extend(pdf.pages)

					# Save the file
					output.save(outfile)

				# Clear files from list
				self.clearFilesFromList()

				# Update statusbar with success message
				self.ui.statusbar.showMessage("Success. Removed security from %d pdfs" % (i+1))

			except:

				# Update the statusbar with an error message with the file that caused it to fail
				self.ui.statusbar.showMessage("Error processing '%s'" % (os.path.basename(filename)))
				output.close()



	# Clear all files from the listbox
	def clearFilesFromList(self):

		self.ui.lstFiles.clear()

if __name__ == "__main__":
	
	# Start the app
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()