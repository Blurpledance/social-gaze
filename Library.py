import os, glob, math
from psychopy import core, visual, prefs, event, gui
from psychopy import sound

def importTrials(trialsFilename, colNames=None, separator='\t'):
	try:
		trialsFile = open(trialsFilename, 'rb')
	except IOError:
		print trialsFilename, 'is not a valid file'

	if colNames is None: # Assume the first row contains the column names
		colNames = trialsFile.next().rstrip().split(separator)
	trialsList = []
	for trialStr in trialsFile:
		trialList = trialStr.rstrip().split(separator)
		assert len(trialList) == len(colNames)
		trialDict = dict(zip(colNames, trialList))
		trialsList.append(trialDict)
	return trialsList


def importTrialsWithHeader(trialsFilename, colNames=None, separator='\t', header=True):
	try:
		trialsFile = open(trialsFilename, 'rb')
	except IOError:
		print trialsFilename, 'is not a valid file'

	if colNames is None: # Assume the first row contains the column names
		colNames = trialsFile.next().rstrip().split(separator)
	trialsList = []
	for trialStr in trialsFile:
		trialList = trialStr.rstrip().split(separator)
		assert len(trialList) == len(colNames)
		trialDict = dict(zip(colNames, trialList))
		trialsList.append(trialDict)
	if header:
		return (colNames, trialsList)
	else:
		return trialList

def printHeader(header,headerFile='header.txt',separator="\t", overwrite=False):
	if overwrite or (not overwrite and not os.path.isfile(headerFile)):
		headerFile = open('header.txt','w')
		writeToFile(headerFile,header,writeNewLine=True)
		return True
	else:
		return False

def evaluateLists(trialList):
	assert isinstance(trialList,list)
	for curTrial in trialList:
		assert isinstance(curTrial,dict)
		for key,value in curTrial.items():
			try:
				if isinstance(eval(curTrial[key]),list):
					curTrial[key]=eval(value)
			except:
				pass
	return trialList

def popupError(text):
	errorDlg = gui.Dlg(title="Error", pos=(200,400))
	errorDlg.addText('Error: '+text, color='Red')
	errorDlg.show()

def getSubjCode(preFilledInText=''):
	 userVar = {'subjCode':preFilledInText}
	 dlg = gui.DlgFromDict(userVar)
	 return userVar['subjCode']

def getRunTimeVars(varsToGet,order,expVersion):
	"""Get run time variables, see http://www.psychopy.org/api/gui.html for explanation"""
	infoDlg = gui.DlgFromDict(dictionary=varsToGet, title=expVersion, fixed=[expVersion],order=order)
	if infoDlg.OK:
		return varsToGet
	else: print 'User Cancelled'


def openOutputFile(subjCode):
	if  os.path.isfile(subjCode+'.txt'):
		popupError('Error: That subject code already exists')
		return False
	else:
		try:
			outputFile = open(subjCode+'.txt','w')
		except:
			print 'could not open file for writing'
		return outputFile


def writeToFile(fileHandle,trial,separator='\t', sync=True,writeNewLine=False):
	"""Writes a trial (array of lists) to a previously opened file"""
	line = separator.join([str(i) for i in trial]) #TABify
	if writeNewLine:
		line += '\n' #add a newline
	try:
		fileHandle.write(line)
	except:
		print 'file is not open for writing'
	if sync:
			fileHandle.flush()
			os.fsync(fileHandle)

def polarToRect(angleList,radius):
	"""Accepts a list of angles and a radius.  Outputs the x,y positions for the angles"""
	coords=[]
	for curAngle in angleList:
		radAngle = (float(curAngle)*2.0*math.pi)/360.0
		xCoord = round(float(radius)*math.cos(radAngle),0)
		yCoord = round(float(radius)*math.sin(radAngle),0)
		coords.append([xCoord,yCoord])
	return coords


def loadFiles(directory,extension,fileType,win='',whichFiles='*',stimList=[]):
	""" Load all the pics and sounds. Uses pyo or pygame for the sound library (see prefs.general['audioLib'])"""
	path = os.getcwd() #set path to current directory
	if isinstance(extension,list):
		fileList = []
		for curExtension in extension:
			fileList.extend(glob.glob(os.path.join(path,directory,whichFiles+curExtension)))
	else:
		fileList = glob.glob(os.path.join(path,directory,whichFiles+extension))
	fileMatrix = {} #initialize fileMatrix  as a dict because it'll be accessed by file names (picture names, sound names)
	for num,curFile in enumerate(fileList):
		fullPath = curFile
		fullFileName = os.path.basename(fullPath)
		stimFile = os.path.splitext(fullFileName)[0]
		if fileType=="image":
			try:
				surface = pygame.image.load(fullPath) #gets height/width of the image
				stim = visual.ImageStim(win, image=fullPath,mask=None,interpolate=True)
				(width,height) = (surface.get_width(),surface.get_height())
			except: #no pygame, so don't store the image dimensions
				(width,height) = ('','')
			stim = visual.ImageStim(win, image=fullPath,mask=None,interpolate=True)
			fileMatrix[stimFile] = {'stim':stim,'fullPath':fullFileName,'filename':stimFile,'num':num,'width':width, 'height':height}
		elif fileType=="sound":
			fileMatrix[stimFile] = {'stim':sound.Sound(fullPath), 'duration':sound.Sound(fullPath).getDuration()}

	#optionally check a list of desired stimuli against those that've been loaded
	if stimList and set(fileMatrix.keys()).intersection(stimList) != set(stimList):
		popupError(str(set(stimList).difference(fileMatrix.keys())) + " does not exist in " + path+'\\'+directory)
	return fileMatrix
