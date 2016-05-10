#!/usr/bin/python
# Tracking functionality for projectOrganizer.py

import os
import sqlite3
import datetime
import glob
import fileFinder
import random

class AssetTracking(object):

	def __init__(self, userDir):
		dbDir = os.path.join(userDir, 'trackingDB.db')
		self.conn = sqlite3.connect(dbDir)

	def createLogs(self, name, typeAsset, project=''): # Create logs for assets and/or project

		if 'project' in typeAsset:
				creation = 'Created on ' + str(datetime.datetime.now())
				idNum = random.randint(0, 100000)

				# Add the project to the project table
				self.conn.execute("INSERT INTO PROJECTS (ID, NAME, STATUS) VALUES (?, ?, ?)", (idNum, name, 'Active'))
		elif 'Asset' in typeAsset:
			if 'animation' in typeAsset:
				upperName = name.upper()
				time = str(datetime.datetime.now())
				creation = 'Created on ' + str(datetime.datetime.now())
				idNum = random.randint(0, 100000)

				self.conn.execute("INSERT INTO ASSETS (ID, NAME, PROJECT, TYPE, STATUS) VALUES (?, ?, ?)", (idNum, name, project, typeAsset, 'Active'))
				self.conn.execute('''CREATE TABLE %s_UPDATES
										(ID INT PRIMARY KEY     NOT NULL,
											UPDATE_DATE   TEXT    NOT NULL,
											UPDATES       TEXT    NOT NULL)''' % (upperName))
				self.conn.execute("INSERT INTO %s (UPDATE_DATE, UPDATES) VALUES (?, ?)" % (name), (time, creation))
			elif 'model' in typeAsset:
				upperName = name.upper()
				time = str(datetime.datetime.now())
				creation = 'Created on ' + str(datetime.datetime.now())
				idNum = random.randint(0, 100000)

				self.conn.execute("INSERT INTO ASSETS (ID, NAME, PROJECT, TYPE, STATUS) VALUES (?, ?, ?)", (idNum, name, project, typeAsset, 'Active'))
				self.conn.execute('''CREATE TABLE %s_UPDATES
										(ID INT PRIMARY KEY     NOT NULL,
											UPDATE_DATE   TEXT    NOT NULL,
											UPDATES       TEXT    NOT NULL)''' % (upperName))
				self.conn.execute("INSERT INTO %s (UPDATE_DATE, UPDATES) VALUES (?, ?)" % (name), (time, creation))
			elif 'rig' in typeAsset:
				upperName = name.upper()
				time = str(datetime.datetime.now())
				creation = 'Created on ' + str(datetime.datetime.now())
				idNum = random.randint(0, 100000)

				self.conn.execute("INSERT INTO ASSETS (ID, NAME, PROJECT, TYPE, STATUS) VALUES (?, ?)", (idNum, name, project, typeAsset, 'Active'))
				slef.conn.execute('''CREATE TABLE %s_UPDATES
										(ID INT PRIMARY KEY     NOT NULL,
											UPDATE_DATE   TEXT    NOT NULL,
											UPDATES       TEXT    NOT NULL)''' % (upperName))
				self.conn.execute("INSERT INTO %s (UPDATE_DATE, UPDATES) VALUES (?, ?)" % (name), (time, creation))
			elif 'script' in typeAsset:
				upperName = name.upper()
				time = str(datetime.datetime.now())
				creation = 'Created on ' + str(datetime.datetime.now())
				idNum = random.randint(0, 100000)

				self.conn.execute("INSERT INTO ASSETS (ID, NAME, PROJECT, TYPE, STATUS) VALUES (?, ?, ?)", (idNum, name, project, typeAsset, 'Active'))
				self.conn.execute('''CREATE TABLE %s_UPDATES
										(ID INT PRIMARY KEY     NOT NULL,
											UPDATE_DATE   TEXT    NOT NULL,
											UPDATES       TEXT    NOT NULL)''' % (upperName))
				self.conn.execute("INSERT INTO %s (UPDATE_DATE, UPDATES) \ VALUES (?, ?)" % (name), (time, creation))
			elif 'concpet' in typeAsset:
				upperName = name.upper()
				time = str(datetime.datetime.now())
				creation = 'Created on ' + str(datetime.datetime.now())
				idNum = random.randint(0, 100000)

				self.conn.execute("INSERT INTO ASSETS (ID, NAME, PROJECT, TYPE, STATUS) \ VALUES (idNum, name, project, typeAsset, 'Active')")
				self.conn.execute('''CREATE TABLE %s_UPDATES
										(ID INT PRIMARY KEY     NOT NULL,
											UPDATE_DATE   TEXT    NOT NULL,
											UPDATES       TEXT    NOT NULL)''' % (upperName))
				self.conn.execute("INSERT INTO %s (UPDATE_DATE, UPDATES) \ VALUES (?, ?)" % (name), (time, creation))
		elif 'documentation' in typeAsset:
			upperName = name.upper()
			time = str(datetime.datetime.now())
			creation = 'Created on ' + str(datetime.datetime.now())
			idNum = random.randint(0, 100000)

			self.conn.execute("INSERT INTO ASSETS (ID, NAME, PROJECT, TYPE, STATUS) VALUES (?, ?, ?)", (idNum, name, project, typeAsset, 'Active'))
			self.conn.execute('''CREATE TABLE %s_UPDATES
									(ID INT PRIMARY KEY     NOT NULL,
										UPDATE_DATE   TEXT    NOT NULL,
										UPDATES       TEXT    NOT NULL)''' % (upperName))
			self.conn.execute("INSERT INTO %s (UPDATE_DATE, UPDATES) \ VALUES (?, ?)" % (name), (time, creation))

		self.conn.commit()

	def createMasterLogs(self, dir):
		self.conn.execute('''CREATE TABLE PROJECTS
						(ID INT PRIMARY KEY     NOT NULL,
							NAME          TEXT    NOT NULL,
							STATUS        TEXT    NOT NULL,
							RELATED_FILES REAL)''')
		self.conn.execute('''CREATE TABLE ASSETS
						(ID INT PRIMARY KEY     NOT NULL,
							NAME          TEXT    NOT NULL,
							PROJECT       TEXT    NOT NULL,
							TYPE          TEXT    NOT NULL,
							STATUS        TEXT    NOT NULL,
							RELATED_FILES REAL)''')
		self.conn.execute('''CREATE TABLE TEAM_CONTACT
						(ID INT PRIMARY KEY     NOT NULL,
							MEMBER        TEXT    NOT NULL,
							EMAIL         TEXT    NOT NULL,
							PROJECT       TEXT    NOT NULL)''')

	def createGlobalLog(self, dir): # Keep the Global log seperate
		self.conn.execute('''CREATE TABLE GLOBAL
						(ID INT PRIMARY KEY     NOT NULL,
							ORIGIN        TEXT    NOT NULL,
							ASSET         TEXT    NOT NULL)''')

	def updateLog(self, log, message): # Write to logs about updates to assets/project
		updateDate = str(datetime.datetime.now())

		self.conn.execute("INSERT INTO %s (UPDATE_DATE, UPDATES) VALUES (?, ?)" % (log), (updateDate, message))

		self.conn.commit()

	def setStatus(self, name, log, newStatus): # Set status of assets
		message = 'Status changed to ' + newStatus
		updateDate = str(datetime.datetime.now())
		self.conn.execute("INSERT INTO ASSETS STATUS = %s WHERE NAME = %s" % (newStatus, name))

		self.conn.execute("INSERT INTO %s (UPDATE_DATE, UPDATES) VALUES (?, ?)" % (log), (updateDate, message))

		self.conn.commit()

	def setProject(self, project, name):
		self.conn.execute("INSERT INTO ASSETS PROJECT = %s WHERE NAME = %s" % (project, name))

		self.conn.commit()

	def relatedFilesLog(self, log, relatedFiles): # Write related files to logs
		updateDate = str(datetime.datetime.now())
		message = 'Adding list of related files: ' + relatedFiles

		self.conn.execute("INSERT INTO ASSETS RELATED_FILES = %s WHERE NAME = %s" % (relatedFiles, name))
		self.conn.execute("INSERT INTO %s (UPDATE_DATE, UPDATES) \ VALUES (?, ?)" % (log), (updateDate, message))

		self.conn.commit()

	def teamInform(self, member, project, email, message=''): # Inform any team members
		if 'add' in action:
			idNum = random.randint(0, 100000)
			self.conn.execute("INSERT INTO TEAM_CONTACT (ID, MEMBER, EMAIL, PROJECT) VALUES (?, ?, ?, ?)", (idNum, member, email, project))

			self.conn.commit()

		elif 'contact' in action:
			pass # Send message to team members

	def projectLog(self, project, status, assetList=[]): # Update project status and general asset updates
		if 'newAsset' in status:
			#time = str(datetime.datetime.now())
			#message = 'Adding new assets to project: ' + assetList

			fileList = self.conn.execute("SELECT RELATED_FILES FROM PROJECTS WHERE NAME = %s" % project)
			for asset in assetList:
				fileList.append(asset)

			self.conn.execute("INSERT INTO PROJECTS (RELATED_FILES) VALUES (?) WHERE NAME = %s" % (project), (fileList))

		if 'Archived' in status:
			#time = str(datetime.datetime.now())
			#message = 'Project has been archived. You can find the archived files in src/Archived/\'Project Name\''

			self.conn.execute("INSERT INTO PROJECTS (STATUS) VALUES (?) WHERE NAME = %s" % (project), (status))

	def findNewFiles(self): # Finding latest files that haven't been tracked
		newestActive = []
		newestGlobal = []
		finderActive = fileFinder.FileFinder('src/Projects/Active')
		finderGlobal = fileFinder.FileFinder('src/Projects/Global')

		newestActive = finderActive.findLatestFiles()
		newestGlobal = finderGlobal.findLatestFiles()

		returnActive = []
		for file in newestActive:
			temp = self.conn.execute("SELECT * FROM ASSETS WHERE NAME = %s" % file)
			if not temp:
				returnActive.append(temp)

		returnGlobal = []
		for file in newestGlobal:
			temp = self.conn.execute("SELECT * FROM ASSETS WHERE NAME = %s" % file)
			if not temp:
				returnGlobal.append(temp)


		return returnActive, returnGlobal

	def closeConnection(self):
		self.conn.close()

