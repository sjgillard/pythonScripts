# File finder
import os

class FileFinder(object):
	def __init__(self, directory):
		self.directory = directory

	def findLog(self): # Find log file for given asset or project
		for dirName, subdirList, fileList in os.walk(self.directory):
			for file in fileList:
				if 'Log.json' in file:
					currDir = os.getcwd()
					return os.path.join(currDir, file)

	def findAssetFile(self, asset): # Find asset file path
		assetFiles = []

		for dirName, subdirList, fileList in os.walk(self.directory):
			for file in fileList:
				if asset in file:
					assetFiles.append(file)

		return assetFiles

	def findProject(self): # Find asset project
		pass

	def findDirectory(self, findFile): # Find the directory or directories of any file given can be found in
		for dirName, subdirList, fileList in os.walk(self.directory):
			for file in fileList:
				if findFile in file:
					return os.path.dirname(file)

	def findActiveProjects(self): # Finds all projects labeled active
		active = os.path.join(self.directory, 'Active')

		activeProjects = os.listdir(active)
		return activeProjects

	def findInactiveProjects(self): # Finds all projects labeled Inactive/Archived
		inactive = os.path.join(self.directory, 'Inactive')

		inactiveProjects = os.listdir(inactive)
		return inactiveProjects

	def getFileList(self, dirType): # Gets a list of files for any project or directory
		if 'project' in dirType:
			log = findLog()
			with open(log, 'r') as logFile:
				data = json.load(logFile)

			return data['Asset List']
		else:
			fileList = []
			for dirName, subdirList, fileList in os.walk(self.directory):
				for file in fileList:
					fileList.append(file)

			return fileList
