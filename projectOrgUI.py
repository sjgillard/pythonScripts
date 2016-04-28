# projectOrganizer UI

import PyQt4.QtCore as qc
import PyQt4.QtGui as qg
import os
import sys
#import projectOrganizer
import assetTracking
import fileFinder
import platform

class ProjectOrgUI(qg.QMainWindow):
	def __init__(self):
		qg.QMainWindow.__init__(self)
		self.setWindowTitle('Project Organizer Window')
		self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
		#self.setModal(False)
		self.setFixedHeight(800)
		self.setFixedWidth(1500)
		overallLayout = qg.QHBoxLayout()
		self.setLayout(overallLayout)

		exitAction = qg.QAction('Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit Application')
		exitAction.triggered.connect(self.close)

		newProjectAction = qg.QAction('New Project', self)
		newProjectAction.setShortcut('Ctrl+P')
		newProjectAction.setStatusTip('Create a New Project')

		newAssetAction = qg.QAction('New Asset', self)
		newAssetAction.setShortcut('Ctrl+A')
		newAssetAction.setStatusTip('Create a New Asset')

		editProjectAction = qg.QAction('Edit Project', self)
		editProjectAction.setStatusTip('Edit a Project')

		editAssetAction = qg.QAction('Edit Asset', self)
		editAssetAction.setStatusTip('Edit an Asset')

		editStatusAction = qg.QAction('Edit Status', self)
		editStatusAction.setStatusTip('Edit a Status of an Asset or Project')

		checkLogAction = qg.QAction('Check Log', self)
		checkLogAction.setStatusTip('Check the Log of an Asset or Project')

		updateLogAction = qg.QAction('Update Log', self)
		updateLogAction.setStatusTip('Update the Log of an Asset or Project')

		findAssetAction = qg.QAction('Find Asset', self)
		findAssetAction.setStatusTip('Find Asset File')

		findLatestAction = qg.QAction('Find Latest', self)
		findLatestAction.setStatusTip('Find Latest File')

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)
		fileMenu.addAction(newProjectAction)
		fileMenu.addAction(newAssetAction)
		fileMenu.addAction(findLatestAction)
		fileMenu.addAction(checkLogAction)
		editMenu = menubar.addMenu('&Edit')
		editMenu.addAction(editProjectAction)
		editMenu.addAction(editAssetAction)
		editMenu.addAction(editStatusAction)
		editMenu.addAction(updateLogAction)

		toolbar = self.addToolBar('Actions')
		toolbar.addAction(checkLogAction)
		toolbar.addAction(updateLogAction)
		toolbar.addAction(findAssetAction)
		toolbar.addAction(findLatestAction)

		fileLayout = qg.QVBoxLayout()
		overallLayout.addLayout(fileLayout)


		filesLabel = qg.QLabel('Project Directory', self)
		filesLabel.move(10, 60)
		filesLabel.setLayout(fileLayout)
		filesLabel.resize(200, 30)
		# Put this in a function to get
		#dirName = qg.QFileDialog.getExistingDirectory(self, 'Select Directory', '/home/sgillard')
		projectDir = qg.QPushButton('Choose a Project', self)
		projectDir.move(10, 85)
		projectDir.resize(projectDir.sizeHint())
		projectSelectorLabel = qg.QLabel('Select Projects from:', self)
		projectSelectorLabel.move(10, 115)
		projectSelectorLabel.resize(200, 30)

		projects = ['Active', 'Inactive', 'Global']
		projectSelector = qg.QComboBox(self)
		projectSelector.addItems(projects)
		projectSelector.move(10, 140)
		projectSelector.setLayout(fileLayout)

		projectDisplay = qg.QTableWidget(self)
		projectDisplay.setRowCount(10)
		projectDisplay.setColumnCount(2)
		title1 = qg.QTableWidgetItem('Directory')
		title2 = qg.QTableWidgetItem('# of Files')
		projectDisplay.setItem(0, 0, title1)
		projectDisplay.setItem(0, 1, title2)
		projectDisplay.move(10, 175)
		projectDisplay.resize(300, 550)
		projectDisplay.show()

		displayLayout = qg.QVBoxLayout()
		displayLayout.addLayout(overallLayout)

		message = 'Display info about selected project or asset'
		logText = qg.QTextEdit(self)
		logText.setPlainText(message)
		logText.setDisabled(True)
		logText.resize(750, 500)
		logText.move(350, 65)
		logText.setLayout(displayLayout)

		editMessage = 'Edit log information'
		logEdit = qg.QTextEdit(self)
		logEdit.setPlainText(editMessage)
		logEdit.resize(750, 150)
		logEdit.move(350, 575)
		logEdit.setLayout(displayLayout)

		submitEdit = qg.QPushButton('Submit Change to Log', self)
		submitEdit.move(350, 735)
		submitEdit.resize(submitEdit.sizeHint())

		notifyEdit = qg.QPushButton('Notify Team of Change', self)
		notifyEdit.move(575, 735)
		notifyEdit.resize(notifyEdit.sizeHint())

		extrasLayout = qg.QVBoxLayout()
		extrasLayout.addLayout(overallLayout)

		teamLabel = qg.QLabel('Team Members for Project:', self)
		teamLabel.move(1150, 65)
		teamLabel.resize(200, 30)
		teamLabel.setLayout(displayLayout)

		members = 'My friends'
		teamMembers = qg.QTextEdit(self)
		teamMembers.setPlainText(members)
		teamMembers.setDisabled(True)
		teamMembers.setLayout(displayLayout)
		teamMembers.resize(300, 200)
		teamMembers.move(1150, 100)

		outputLabel = qg.QLabel('Ouptput:', self)
		outputLabel.move(1150, 300)
		outputLabel.resize(200, 30)
		outputLabel.setLayout(displayLayout)

		output = 'Ouptput Display'
		outputDisplay = qg.QTextEdit(self)
		outputDisplay.setPlainText(output)
		outputDisplay.setDisabled(True)
		outputDisplay.setLayout(displayLayout)
		outputDisplay.resize(300, 400)
		outputDisplay.move(1150, 325)




if __name__ == "__main__":
	app = qg.QApplication(sys.argv)
	main_window = ProjectOrgUI()
	main_window.show()
	sys.exit(app.exec_())
