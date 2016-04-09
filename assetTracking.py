# Tracking functionality for projectOrganizer.py

import os
import json
import datetime

class AssetTracking(object):

	def __init__(self):
		pass

	def createLogs(self, dir, name, typeAsset): # Create logs for assets and/or project
		logName = name + 'Log.json'
		log = os.join.path(dir, logName)

		if 'project' in typeAsset:
			data = {'Type': typeAsset,
					'Creation': str(datetime.datetime.now()),
					'Status': 'Active',
					'Asset List': 'None',
					'Team Members': 'None',
					'Member Contact': 'None'}
		elif 'Asset' in typeAsset:
			if 'animation' in typeAsset:
				data = {'Type': typeAsset,
						'Creation': str(datetime.datetime.now()),
						'Status': 'Active',
						'Related Files': 'None'}
			elif 'model' in typeAsset:
				data = {'Type': typeAsset,
						'Creation': str(datetime.datetime.now()),
						'Status': 'Active',
						'Related Files': 'None'}
			elif 'rig' in typeAsset:
				data = {'Type': typeAsset,
						'Creation': str(datetime.datetime.now()),
						'Status': 'Active',
						'Related Files': 'None'}
			elif 'script' in typeAsset:
				data = {'Type': typeAsset,
						'Creation': str(datetime.datetime.now()),
						'Status': 'Active',
						'Related Files': 'None'}
			elif 'concpet' in typeAsset:
				data = {'Type': typeAsset,
						'Creation': str(datetime.datetime.now()),
						'Status': 'Active',
						'Concept Type': 'None'}
		elif 'documentation' in typeAsset:
			data = {'Type': typeAsset,
					'Creation': str(datetime.datetime.now()),
					'Status': 'Active'}

		with open(log, 'w') as newLog:
			json.dump(data, newLog)

	def updateLog(self, log, message): # Write to logs about updates to assets/project
		with open(log, 'r') as logFile:
			data = json.load(logFile)

		data[str(datetime.datetime.now())] = message

		with open(log, 'w') as logFile:
			json.dump(data, logFile)

	def setStatus(self, log, newStatus): # Set status of assets
		with open(log, 'r') as logFile:
			data = json.load(logFile)

		data['Status'] = newStatus
		data[str(datetime.datetime.now())] = 'Status changed to ' + newStatus

		with opne(log, 'w') as logFile:
			json.dump(data, logFile)


	def relatedFilesLog(self, log, relatedFiles): # Write related files to logs
		with open(log, 'r') as logFile:
			data = json.load(logFile)

		data['Related Files'] = relatedFiles
		data[str(datetime.datetime.now())] = 'Adding list of related files: ' + relatedFiles

		with opne(log, 'w') as logFile:
			json.dump(data, logFile)

	def teamInform(self, log, teamList={}, action, message=''): # Inform any team members
		if 'add' in action:
			with open(log, 'r') as logFile:
				data = json.load(logFile)

			for member in teamList:
				data['Team Members'] = member
				data['Member Concept'] = teamList[member]

			data[str(datetime.datetime.now())] = 'Adding team members and contact info'

			with opne(log, 'w') as logFile:
				json.dump(data, logFile)

		elif 'contact' in action:
			pass # Send message to team members

	def projectLog(self, log, status, assetList=[]): # Update project status and general asset updates
		if 'newAsset' in status:
			with open(log, 'r') as logFile:
				data = json.load(logFile)

			for asset in assetList:
				data['Asset List'].append(asset)

			data[str(datetime.datetime.now())] = 'Adding new assets to project: ' + assetList

			with opne(log, 'w') as logFile:
				json.dump(data, logFile)

		elif 'Archive' in status:
			with open(log, 'r') as logFile:
				data = json.load(logFile)

			data['Status'] = 'Archived'

			data[str(datetime.datetime.now())] = 'Project has been archived. You can find the archived files' +
												  ' in src/Archived/\'Project Name\''

			with opne(log, 'w') as logFile:
				json.dump(data, logFile)

	def svnUpdates(self): # Update file if SVN available
		pass
