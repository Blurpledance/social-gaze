from psychopy import core, visual, prefs, event, gui, parallel
import os, glob, math, random, Image, pyglet
import numpy as np
prefs.general['audioLib'] = ['pyo'] #using pyo as the default sound library
from Library import *
#from functions import *
from generateTrials import *
import webbrowser as web


#port = parallel.ParallelPort(address=0XD020)
#port.setData(int(00000000))

###################### functions
def showText(textToShow, delay, col):
	visual.TextStim(win,text=textToShow,height = 45,color = col).draw()
	visual.TextStim.size = (1,8)
	win.flip()
	#core.wait(30)
	core.wait(delay)
	pass

def fixCross():
	visual.TextStim(win,text="+",height = 90, pos=(0.0, 0.0), color = 'white').draw() ### y of 70.0 gets to eye level
	win.flip()
	core.wait(2)
	win.flip(clearBuffer=True)
	pass

def showVids(vidList, counter, AP):
	mov = visual.MovieStim(win,filename='E:\\GazeProgram\\vids\\'+vidList[int(counter)-1]["stimName"])
	### fix opacity?
	fixCross()
	timer = core.Clock()
	responded = False
	DINstr = vidList[int(counter)-1]["stimCode"]
	#port.setData(int(DINstr))
	print (DINstr)
	core.wait(.25)
	while timer.getTime()<(4):
		mov.draw()
		win.flip(clearBuffer=True)
		event.clearEvents
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
	mov.play()
	#port.setData(int(00000000))
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

def loadStims (trialsToShow):
	stims = []
	for i in range(len(trialsToShow)):
		mov = visual.MovieStim(win,filename='E:\\GazeProgram\\vids\\'+trialsToShow[i]["stimName"])
		stims.append(mov)
	return stims

######################################################## study starts here
###### getting subject info, generating trials
#port.setData(int(00000000))
while True:
	runTimeVarOrder = ['subjCode','gender']
	runTimeVars = getRunTimeVars({'subjCode':'', 'gender':['M','F','Unknown']},runTimeVarOrder,'ver1')
	outputFile = openOutputFile('data\\'+runTimeVars['subjCode'])
	print 'output file is',outputFile
	if outputFile:
		break
generateTrials(int(runTimeVars['subjCode']))

win = visual.Window([1024,768],color="grey", units='pix', waitBlanking=False, fullscr=False)
event.Mouse(visible=False)
#port.setData(int(00000000))
##### getting practice and actual trials, to lists
trialsFilename = 'trials\\'+runTimeVars['subjCode'] + ".txt"
Trials = importTrials(trialsFilename, colNames=['SubID', 'block_order', 'resp_order', 'target_sex', 'identity', 'target_race','side','speed','gaze','stimCode','stimName'], separator='\t')
#stims = loadStims(Trials)

############ Main Instructs
showText ('You will see a set of animated faces.',5, 'white')
showText ('You will briefly see a fixation cross before each face is presented.',5, 'white')
showText ('On some trials you will be asked to simply view the faces.',5, 'white')
showText ('On other trials, you will report whether the face turned from the left or right, responding with the left or right arrow on the keyboard.',15, 'white')
showText ('You will have a short break halfway through the study.',5, 'white')
showText ('Please do your best to remain still for the duration of the time that sensors are attached to your body.',10, 'white')

############### Baseline recording
showText ('A 5 minute baseline recording of your physiological activity will begin shortly. Please remain still. ',5, 'white')
#parallel.setData(int(00000001, 2)) ## this is the unused pin
showText ('Collecting baseline data. Please remain still.',5, 'white')
#parallel.setData(int(00000000, 2))
showText ('Baseline recording is now over.',5, 'white')
######### Between person blocked active/passive

if Trials[1]["resp_order"] == 'Active_first':
	######### Active Response first
	showText ('Use the keyboard to respond. Press the left arrow if the face turned from the left, and the right arrow if the face turned from the right.',15, 'white')
	showText ('Faces will be presented in 10 seconds.', 5, 'white')
	########### block A
	counter = 1
	while counter % 3 != 0:  #49
		showVids(Trials, counter,  'A')
		counter += 1
	########### BREAK
	showText ('You are halfway through the physiology portion of the study. You will now have a 2 minute break.', 5, 'white')
	showText ('Do not enter a response in this part of the study. Just sit calmly and view the faces on the screen.',15, 'white')
	showText ('The study will resume in 10 seconds.', 5, 'white')
	########### block B
	while counter % 6 != 0: #97
		showVids(Trials, counter,  'P')
		counter += 1
else:
	######### Passive Response first
	showText ('Do not enter a response in this part of the study. Just sit calmly and view the faces on the screen.',15, 'white')
	showText ('Faces will be presented in 10 seconds.', 5, 'white')
	########### block A
	counter = 1
	while counter % 3 != 0:  #49
		showVids(Trials, counter,  'P')
		counter += 1
	########### BREAK
	showText ('You are halfway through the physiology portion of the study. You will now have a 2 minute break.', 5, 'white')
	showText ('For the next part of the study, use the keyboard to respond. Press the left arrow if the face turned from the left, and the right arrow if the face turned from the right.',15, 'white')
	showText ('The study will resume in 10 seconds.', 5, 'white')
	########### block B
	while counter % 6 != 0: #97
		showVids(Trials, counter, 'A')
		counter += 1

######### closing
outputFile.close()
showText('The physiology portion of the study is now over. A web browser will open automatically. Please fill out the survey.', 5, 'white')

# then, at the very end of your study, just do the following, where you append ?subjID= to the end of your qualtrics URL (have an embedded data item that is called subjID in qualtrics workflow). Then, call your psychopy SUBID variable where I've written "SUBID".
url='https://uwmadison.co1.qualtrics.com/jfe/form/SV_bwKVmyA3XdivKBL?subjID='+runTimeVars['subjCode']
web.open(url)
