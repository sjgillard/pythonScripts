# File finder
import os
import glob

class FileFinder(object):
	def __init__(self, directory):
		self.directory = directory

	def findLog(self, name): # Find log file for given asset or project
		conn = sqlite3.connect('trackingDB.db')
		uppedName = name.upper()
		log = conn.execute("SELECT * FROM %s" % uppedName)

		return log

	def findAssetFile(self, asset): # Find asset file path
		assetFiles = []

		for dirName, subdirList, fileList in os.walk(self.directory):
			for file in fileList:
				if asset in file:
					assetFiles.append(file)

		return assetFiles

	def findProject(self, name): # Find asset project
		conn = sqlite3.connect('trackingDB.db')
		project = conn.execute("SELECT PROJECT FROM ASSET WHERE NAME = %s" % name)
		conn.close()

		return project

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

	def getFileList(self, dirType, name = ''): # Gets a list of files for any project or directory
		if 'project' in dirType:
			conn = sqlite3.connect('trackingDB.db')
			temp = conn.execute("SELECT RELATED_FILES FROM PROJECTS WHERE NAME = %s" % name)
			conn.close()
			return temp
		else:
			fileList = []
			for dirName, subdirList, fileList in os.walk(self.directory):
				for file in fileList:
					fileList.append(file)

			return fileList

	def findLatestFiles(self):
		newestFiles = []
		fileExtensions = ['.ma', '.mb', '.jpeg', '.png', '.doc', '.docx', '.py', '.mel']
		for dirName, subdirList, fileList in os.walk('src/Projects/Active'):
			for extension in fileExtensions:
				temp = '*%s' % extension
				tempName = os.path.join(dirName, temp)
				newest = max(glob.iglob(tempName), key = os.path.getctime)
				if newest:
					newestFiles.append(newest)

		return newestFiles
