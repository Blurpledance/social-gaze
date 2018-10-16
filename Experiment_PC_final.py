from psychopy import core, visual,logging, prefs, event, gui, parallel, sound
import os, glob, math, random, Image, pyglet
import numpy as np
prefs.general['audioLib'] = ['pyo'] #using pyo as the default sound library
from Library import *
#from functions import *
from generateTrials import *
import webbrowser as web
import cv2

parallel.setPortAddress(0XD020)
parallel.setData(0)

###################### functions
def showText(textToShow, delay, col):
	visual.TextStim(win,text=textToShow,height = 45,color = col).draw()
	visual.TextStim.size = (1,8)
	win.flip()
	#core.wait(30)
	core.wait(delay)
	pass

def fixCross():
	visual.TextStim(win,text="+",height = 90, pos=(0.0, 95.0), color = 'white').draw() ### y of 95.0 gets to eye level
	win.flip()
	core.wait(2)
	win.flip(clearBuffer=True)
	pass
	
def loadVids(directory, stimList=[]):
	path = os.getcwd()
	fileList = []
	fileList.extend(glob.glob(os.path.join(path,directory)))
	return(fileList)
	
def showVids(vidList, counter, AP):
	mov = visual.MovieStim2(win,loop = False, noAudio=True,size=[1000,1000], pos=[0,0],flipVert=False, flipHoriz=False, filename='Z:\\Documents\\GazeProgram\\vids\\'+vidList[int(counter)-1]["stimName"])
	noise.play()
	fixCross()
	responded = False
	core.wait(.25)
	win.clearBuffer()
	timer = core.Clock()
	DINstr = str(vidList[int(counter)-1]["stimCode"])
	parallel.setData(int(DINstr,2))
	while timer.getTime()<(4):
		mov.draw()
		win.flip(clearBuffer=True)
		if event.getKeys(keyList = 'q'):
			print "tying to exit"
			core.quit()
			break
		if event.getKeys(keyList = ['right']):
			RT = timer.getTime()
			entry = 'Right'
			responded=True
		if event.getKeys(keyList = ['left']):
			RT = timer.getTime()
			entry = 'Left'
			responded=True
		if responded == False:
			RT = 'NA'
			entry = 'NA'
			responded=False
		else:
			pass
	mov.draw()
	win.flip(clearBuffer=True)
	core.wait(3) ######## this is the amount of pause at the end of the video
	win.flip(clearBuffer=True)
	parallel.setData(0)
	while timer.getTime()<(15):
		if event.getKeys(keyList = 'q'):
			print "tying to exit"
			core.quit()
			break
		if event.getKeys(keyList = ['right']):
			RT = timer.getTime()
			entry = 'Right'
			responded=True
		if event.getKeys(keyList = ['left']):
			RT = timer.getTime()
			entry = 'Left'
			responded=True
		if responded == False:
			RT = 'NA'
			entry = 'NA'
			responded=False
		else:
			pass
	outString = (runTimeVars['subjCode'], int(counter), AP, RT, entry, responded, vidList[int(counter)-1]["target_sex"], vidList[int(counter)-1]["identity"],vidList[int(counter)-1]["target_race"],vidList[int(counter)-1]["side"],vidList[int(counter)-1]["speed"],vidList[int(counter)-1]["gaze"],  vidList[int(counter)-1]["stimCode"],vidList[int(counter)-1]["stimName"])
	writeToFile(outputFile,outString,writeNewLine=True)

######################################################## study starts here
###### getting subject info, generating trials
parallel.setData(0)
while True:
	runTimeVarOrder = ['subjCode','gender']
	runTimeVars = getRunTimeVars({'subjCode':'', 'gender':['M','F','Unknown']},runTimeVarOrder,'ver1')
	outputFile = openOutputFile('data\\'+runTimeVars['subjCode'])
	print 'output file is',outputFile
	if outputFile:
		break
generateTrials(int(runTimeVars['subjCode']))

win = visual.Window([1024,768],color="grey", units='pix', waitBlanking=False, fullscr=True)
noise= sound.Sound('Z:\\Documents\\GazeProgram\\noise.wav')
event.Mouse(visible=False)
parallel.setData(0)
##### getting trials to list
trialsFilename = 'trials\\'+runTimeVars['subjCode'] + ".txt"
Trials = importTrials(trialsFilename, colNames=['SubID', 'block_order', 'resp_order', 'target_sex', 'identity', 'target_race','side','speed','gaze','stimCode','stimName'], separator='\t')
stims = loadVids("\vids\\*")

############ Main Instructs
#showText ('You will see a set of animated faces.',5, 'white')
#showText ('You will briefly see a fixation cross and hear an orientation sound before each face is presented.',5, 'white')
#showText ('On some trials you will be asked to simply view the faces.',5, 'white')
#showText ('On other trials, you will report whether the face turned from your left or your right, responding with the left or right arrow on the keyboard.',10, 'white')
#showText ('You will have a short break halfway through the study.',5, 'white')
#showText ('Please do your best to remain still for the duration of the time that sensors are attached to your body.',10, 'white')

############### Baseline recording
#showText ('A 5 minute baseline recording of your physiological activity will begin shortly. Please remain still with your eyes open. ',10, 'white')
parallel.setData(int('10000000', 2)) ## this is the unused pin
#showText ('Collecting baseline data. Please remain still with your eyes open.',300, 'white')
parallel.setData(0)			
#showText ('Baseline recording is now over. The study will begin shortly.',5, 'white')

######### Between person blocked active/passive

if Trials[1]["resp_order"] == 'Active':
	######### Active Response first
	showText ('You will see a series of faces. As soon as the face disappears, use the keyboard to respond.',10, 'white')
	showText ('Press the left arrow if the face turned from your left, and the right arrow if the face turned from your right.',5, 'white')
	showText ('Faces will be presented in 10 seconds.', 10, 'white')
	########### block A
	counter = 1
	while counter % 49 != 0:  #49
		showVids(Trials, counter,  'A')
		counter += 1
	########### BREAK
	showText ('You are halfway through the physiology portion of the study. You will now have a 2 minute break.', 95, 'white')
	showText ('You will again see a series of faces. This time, do not enter a response. Just sit calmly and view the faces on the screen.',15, 'white')
	showText ('The study will resume in 10 seconds.', 10, 'white')
	########### block B
	while counter % 97 != 0: #97
		showVids(Trials, counter,  'P')
		counter += 1
else:
	######### Passive Response first
	showText ('You will see a series of faces. Do not enter a response in this part of the study. Just sit calmly and view the faces on the screen.',15, 'white')
	showText ('Faces will be presented in 10 seconds.', 10, 'white')
	########### block A
	counter = 1
	while counter % 49 != 0:  #49
		showVids(Trials, counter,  'P')
		counter += 1
	########### BREAK
	showText ('You are halfway through the physiology portion of the study. You will now have a 2 minute break.', 95, 'white')
	showText ('You will again see a series of faces. This time, use the keyboard to respond as soon as the face disappears.',10, 'white')
	showText ('Press the left arrow if the face turned from your left, and the right arrow if the face turned from your right.',5, 'white')
	showText ('The study will resume in 10 seconds.', 10, 'white')
	########### block B
	while counter % 97 != 0: #97
		showVids(Trials, counter, 'A')
		counter += 1

######### closing
outputFile.close()
showText('The physiology portion of the study is now over. A web browser will open automatically. Please fill out the survey.', 5, 'white')

# then, at the very end of your study, just do the following, where you append ?subjID= to the end of your qualtrics URL (have an embedded data item that is called subjID in qualtrics workflow). Then, call your psychopy SUBID variable where I've written "SUBID".
url='https://uwmadison.co1.qualtrics.com/jfe/form/SV_bwKVmyA3XdivKBL?subjID='+runTimeVars['subjCode']
web.open(url)
