import random
from Library import *


def generateTrials(subjCode):
	random.seed(subjCode)
	outputFile = openOutputFile('trials/'+str(subjCode))

	mwrsEC=['m_1_EC_right_3.avi',  'm_4_EC_right_3.avi']
	random.shuffle(mwrsEC)
	fwrsEC=['f_1_EC_right_3.avi', 'f_2_EC_right_3.avi']
	random.shuffle(fwrsEC)
	mbrsEC=['m_7_EC_right_3.avi', 'm_8_EC_right_3.avi']
	random.shuffle(mbrsEC)
	fbrsEC=['f_6_EC_right_3.avi',  'f_8_EC_right_3.avi']
	random.shuffle(fbrsEC)
	mwlsEC=['m_1_EC_left_3.avi',  'm_4_EC_left_3.avi']
	random.shuffle(mwlsEC)
	fwlsEC=['f_1_EC_left_3.avi', 'f_2_EC_left_3.avi']
	random.shuffle(fwlsEC)
	mblsEC=['m_7_EC_left_3.avi', 'm_8_EC_left_3.avi']
	random.shuffle(mblsEC)
	fblsEC=['f_6_EC_left_3.avi', 'f_8_EC_left_3.avi']
	random.shuffle(fblsEC)

	mwrfEC=['m_1_EC_right_2.avi',  'm_4_EC_right_2.avi']
	random.shuffle(mwrfEC)
	fwrfEC=['f_1_EC_right_2.avi', 'f_2_EC_right_2.avi']
	random.shuffle(fwrfEC)
	mbrfEC=['m_7_EC_right_2.avi', 'm_8_EC_right_2.avi']
	random.shuffle(mbrfEC)
	fbrfEC=['f_6_EC_right_2.avi', 'f_8_EC_right_2.avi']
	random.shuffle(fbrfEC)
	mwlfEC=['m_1_EC_left_2.avi',  'm_4_EC_left_2.avi']
	random.shuffle(mwlfEC)
	fwlfEC=['f_1_EC_left_2.avi', 'f_2_EC_left_2.avi']
	random.shuffle(fwlfEC)
	mblfEC=['m_7_EC_left_2.avi', 'm_8_EC_left_2.avi']
	random.shuffle(mblfEC)
	fblfEC=['f_6_EC_left_2.avi', 'f_8_EC_left_2.avi']
	random.shuffle(fblfEC)


	#### NC
	mwrsNC=['m_1_NC_right_3.avi',  'm_4_NC_right_3.avi']
	random.shuffle(mwrsNC)
	fwrsNC=['f_1_NC_right_3.avi', 'f_2_NC_right_3.avi']
	random.shuffle(fwrsNC)
	mbrsNC=['m_7_NC_right_3.avi', 'm_8_NC_right_3.avi']
	random.shuffle(mbrsNC)
	fbrsNC=['f_6_NC_right_3.avi', 'f_8_NC_right_3.avi']
	random.shuffle(fbrsNC)
	mwlsNC=['m_1_NC_left_3.avi', 'm_4_NC_left_3.avi']
	random.shuffle(mwlsNC)
	fwlsNC=['f_1_NC_left_3.avi', 'f_2_NC_left_3.avi']
	random.shuffle(fwlsNC)
	mblsNC=['m_7_NC_left_3.avi', 'm_8_NC_left_3.avi']
	random.shuffle(mblsNC)
	fblsNC=['f_6_NC_left_3.avi',  'f_8_NC_left_3.avi']
	random.shuffle(fblsNC)

	mwrfNC=['m_1_NC_right_2.avi',  'm_4_NC_right_2.avi']
	random.shuffle(mwrfNC)
	fwrfNC=['f_1_NC_right_2.avi', 'f_2_NC_right_2.avi']
	random.shuffle(fwrfNC)
	mbrfNC=['m_7_NC_right_2.avi', 'm_8_NC_right_2.avi']
	random.shuffle(mbrfNC)
	fbrfNC=['f_6_NC_right_2.avi', 'f_8_NC_right_2.avi']
	random.shuffle(fbrfNC)
	mwlfNC=['m_1_NC_left_2.avi',  'm_4_NC_left_2.avi']
	random.shuffle(mwlfNC)
	fwlfNC=['f_1_NC_left_2.avi', 'f_2_NC_left_2.avi']
	random.shuffle(fwlfNC)
	mblfNC=['m_7_NC_left_2.avi', 'm_8_NC_left_2.avi']
	random.shuffle(mblfNC)
	fblfNC=['f_6_NC_left_2.avi', 'f_8_NC_left_2.avi']
	random.shuffle(fblfNC)

	NC33 = [mbrsNC[0], mbrfNC[1],mblsNC[0],mblfNC[1],
	mwrsNC[0], mwrfNC[1], mwlsNC[0], mwlfNC[1],
	fbrsNC[0], fbrfNC[1], fblsNC[0], fblfNC[1],
	fwrsNC[0], fwrfNC[1], fwlsNC[0], fwlfNC[1],
	mbrsEC[0], mbrfEC[0],mblsEC[0],mblfEC[0],
	mwrsEC[0], mwrfEC[0], mwlsEC[0], mwlfEC[0],
	fbrsEC[0], fbrfEC[0], fblsEC[0], fblfEC[0],
	fwrsEC[0], fwrfEC[0], fwlsEC[0], fwlfEC[0],
	mbrsEC[1], mbrfEC[1], mblsEC[1], mblfEC[1],
	mwrsEC[1], mwrfEC[1], mwlsEC[1], mwlfEC[1],
	fbrsEC[1], fbrfEC[1], fblsEC[1], fblfEC[1],
	fwrsEC[1], fwrfEC[1], fwlsEC[1], fwlfEC[1]]
	random.shuffle(NC33)

	NC67 = [mbrsEC[0], mbrfEC[1],mblsEC[0],mblfEC[1],
	mwrsEC[0], mwrfEC[1], mwlsEC[0], mwlfEC[1],
	fbrsEC[0], fbrfEC[1], fblsEC[0], fblfEC[1],
	fwrsEC[0], fwrfEC[1], fwlsEC[0], fwlfEC[1],
	mbrsNC[0], mbrfNC[0],mblsNC[0],mblfNC[0],
	mwrsNC[0], mwrfNC[0], mwlsNC[0], mwlfNC[0],
	fbrsNC[0], fbrfNC[0], fblsNC[0], fblfNC[0],
	fwrsNC[0], fwrfNC[0], fwlsNC[0], fwlfNC[0],
	mbrsNC[1], mbrfNC[1], mblsNC[1], mblfNC[1],
	mwrsNC[1], mwrfNC[1], mwlsNC[1], mwlfNC[1],
	fbrsNC[1], fbrfNC[1], fblsNC[1], fblfNC[1],
	fwrsNC[1], fwrfNC[1], fwlsNC[1], fwlfNC[1]]
	random.shuffle(NC67)

	if subjCode % 4 == 0:
		stimOrder = NC67
		block = 'NC'
		blockCode = '0'
		instructions = 'Active'
		instructCode = '1'
		for i in stimOrder:
			if 'm_' in i:
				sex = 'm'
				sexCode = '0'
			else:
				sex = 'f'
				sexCode = '1'
			if '1_' in i:
				identity = '1'
				race = 'w'
				raceCode = '0'
			elif '2_' in i:
				identity = '2'
				race = 'w'
				raceCode = '0'
			elif '3_' in i:
				identity = '3'
				race = 'w'
				raceCode = '0'
			elif '4_' in i:
				identity = '4'
				race = 'w'
				raceCode = '0'
			elif '5_' in i:
				identity = '5'
				race = 'b'
				raceCode = '1'
			elif '6_' in i:
				identity = '6'
				race = 'b'
				raceCode = '1'
			elif '7_' in i:
				identity = '7'
				race = 'b'
				raceCode = '1'
			else:
				identity = '8'
				race = 'b'
				raceCode = '1'
			if 'right' in i:
				side = 'right'
				sideCode = '0'
			else:
				side = 'left'
				sideCode= '1'
			if '2.m' in i:
				speed = 'f'
				speedCode = '0'
			else :
				speed = 's'
				speedCode = '1'
			if 'EC' in i:
				gaze = 'EC'
				gazeCode = '0'
			else:
				gaze = 'NC'
				gazeCode = '1'
			stimCode=sexCode+raceCode+sideCode+speedCode+gazeCode+instructCode+blockCode
			outString = (subjCode,block, instructions, sex,identity,race,side,speed,gaze,stimCode,i)
			writeToFile(outputFile,outString,writeNewLine=True)
		stimOrder = NC33
		block = 'EC'
		blockCode = '1'
		instructions = 'Passive'
		instructCode = '0'
		for i in stimOrder:
			if 'm_' in i:
				sex = 'm'
				sexCode = '0'
			else:
				sex = 'f'
				sexCode = '1'
			if '1_' in i:
				identity = '1'
				race = 'w'
				raceCode = '0'
			elif '2_' in i:
				identity = '2'
				race = 'w'
				raceCode = '0'
			elif '3_' in i:
				identity = '3'
				race = 'w'
				raceCode = '0'
			elif '4_' in i:
				identity = '4'
				race = 'w'
				raceCode = '0'
			elif '5_' in i:
				identity = '5'
				race = 'b'
				raceCode = '1'
			elif '6_' in i:
				identity = '6'
				race = 'b'
				raceCode = '1'
			elif '7_' in i:
				identity = '7'
				race = 'b'
				raceCode = '1'
			else:
				identity = '8'
				race = 'b'
				raceCode = '1'
			if 'right' in i:
				side = 'right'
				sideCode = '0'
			else:
				side = 'left'
				sideCode= '1'
			if '2.m' in i:
				speed = 'f'
				speedCode = '0'
			else :
				speed = 's'
				speedCode = '1'
			if 'EC' in i:
				gaze = 'EC'
				gazeCode = '0'
			else:
				gaze = 'NC'
				gazeCode = '1'
			stimCode=sexCode+raceCode+sideCode+speedCode+gazeCode+instructCode+blockCode
			outString = (subjCode,block, instructions, sex,identity,race,side,speed,gaze,stimCode,i)
			writeToFile(outputFile,outString,writeNewLine=True)

	elif subjCode % 4 == 1:
		stimOrder = NC33
		block = 'EC'
		blockCode = '1'
		instructions = 'Active'
		instructCode = '1'
		for i in stimOrder:
			if 'm_' in i:
				sex = 'm'
				sexCode = '0'
			else:
				sex = 'f'
				sexCode = '1'
			if '1_' in i:
				identity = '1'
				race = 'w'
				raceCode = '0'
			elif '2_' in i:
				identity = '2'
				race = 'w'
				raceCode = '0'
			elif '3_' in i:
				identity = '3'
				race = 'w'
				raceCode = '0'
			elif '4_' in i:
				identity = '4'
				race = 'w'
				raceCode = '0'
			elif '5_' in i:
				identity = '5'
				race = 'b'
				raceCode = '1'
			elif '6_' in i:
				identity = '6'
				race = 'b'
				raceCode = '1'
			elif '7_' in i:
				identity = '7'
				race = 'b'
				raceCode = '1'
			else:
				identity = '8'
				race = 'b'
				raceCode = '1'
			if 'right' in i:
				side = 'right'
				sideCode = '0'
			else:
				side = 'left'
				sideCode= '1'
			if '2.m' in i:
				speed = 'f'
				speedCode = '0'
			else :
				speed = 's'
				speedCode = '1'
			if 'EC' in i:
				gaze = 'EC'
				gazeCode = '0'
			else:
				gaze = 'NC'
				gazeCode = '1'
			stimCode=sexCode+raceCode+sideCode+speedCode+gazeCode+instructCode+blockCode
			outString = (subjCode,block, instructions, sex,identity,race,side,speed,gaze,stimCode,i)
			writeToFile(outputFile,outString,writeNewLine=True)
		stimOrder = NC67
		block = 'NC'
		blockCode = '0'
		instructions = 'Passive'
		instructCode = '0'
		for i in stimOrder:
			if 'm_' in i:
				sex = 'm'
				sexCode = '0'
			else:
				sex = 'f'
				sexCode = '1'
			if '1_' in i:
				identity = '1'
				race = 'w'
				raceCode = '0'
			elif '2_' in i:
				identity = '2'
				race = 'w'
				raceCode = '0'
			elif '3_' in i:
				identity = '3'
				race = 'w'
				raceCode = '0'
			elif '4_' in i:
				identity = '4'
				race = 'w'
				raceCode = '0'
			elif '5_' in i:
				identity = '5'
				race = 'b'
				raceCode = '1'
			elif '6_' in i:
				identity = '6'
				race = 'b'
				raceCode = '1'
			elif '7_' in i:
				identity = '7'
				race = 'b'
				raceCode = '1'
			else:
				identity = '8'
				race = 'b'
				raceCode = '1'
			if 'right' in i:
				side = 'right'
				sideCode = '0'
			else:
				side = 'left'
				sideCode= '1'
			if '2.m' in i:
				speed = 'f'
				speedCode = '0'
			else :
				speed = 's'
				speedCode = '1'
			if 'EC' in i:
				gaze = 'EC'
				gazeCode = '0'
			else:
				gaze = 'NC'
				gazeCode = '1'
			stimCode=sexCode+raceCode+sideCode+speedCode+gazeCode+instructCode+blockCode
			outString = (subjCode,block, instructions, sex,identity,race,side,speed,gaze,stimCode,i)
			writeToFile(outputFile,outString,writeNewLine=True)
	elif subjCode % 4 == 2:
		stimOrder = NC67
		block = 'NC'
		blockCode = '0'
		instructions = 'Passive'
		instructCode = '0'
		for i in stimOrder:
			if 'm_' in i:
				sex = 'm'
				sexCode = '0'
			else:
				sex = 'f'
				sexCode = '1'
			if '1_' in i:
				identity = '1'
				race = 'w'
				raceCode = '0'
			elif '2_' in i:
				identity = '2'
				race = 'w'
				raceCode = '0'
			elif '3_' in i:
				identity = '3'
				race = 'w'
				raceCode = '0'
			elif '4_' in i:
				identity = '4'
				race = 'w'
				raceCode = '0'
			elif '5_' in i:
				identity = '5'
				race = 'b'
				raceCode = '1'
			elif '6_' in i:
				identity = '6'
				race = 'b'
				raceCode = '1'
			elif '7_' in i:
				identity = '7'
				race = 'b'
				raceCode = '1'
			else:
				identity = '8'
				race = 'b'
				raceCode = '1'
			if 'right' in i:
				side = 'right'
				sideCode = '0'
			else:
				side = 'left'
				sideCode= '1'
			if '2.m' in i:
				speed = 'f'
				speedCode = '0'
			else :
				speed = 's'
				speedCode = '1'
			if 'EC' in i:
				gaze = 'EC'
				gazeCode = '0'
			else:
				gaze = 'NC'
				gazeCode = '1'
			stimCode=sexCode+raceCode+sideCode+speedCode+gazeCode+instructCode+blockCode
			outString = (subjCode,block, instructions, sex,identity,race,side,speed,gaze,stimCode,i)
			writeToFile(outputFile,outString,writeNewLine=True)
		stimOrder = NC33
		block = 'EC'
		blockCode = '1'
		instructions = 'Active'
		instructCode = '1'
		for i in stimOrder:
			if 'm_' in i:
				sex = 'm'
				sexCode = '0'
			else:
				sex = 'f'
				sexCode = '1'
			if '1_' in i:
				identity = '1'
				race = 'w'
				raceCode = '0'
			elif '2_' in i:
				identity = '2'
				race = 'w'
				raceCode = '0'
			elif '3_' in i:
				identity = '3'
				race = 'w'
				raceCode = '0'
			elif '4_' in i:
				identity = '4'
				race = 'w'
				raceCode = '0'
			elif '5_' in i:
				identity = '5'
				race = 'b'
				raceCode = '1'
			elif '6_' in i:
				identity = '6'
				race = 'b'
				raceCode = '1'
			elif '7_' in i:
				identity = '7'
				race = 'b'
				raceCode = '1'
			else:
				identity = '8'
				race = 'b'
				raceCode = '1'
			if 'right' in i:
				side = 'right'
				sideCode = '0'
			else:
				side = 'left'
				sideCode= '1'
			if '2.m' in i:
				speed = 'f'
				speedCode = '0'
			else :
				speed = 's'
				speedCode = '1'
			if 'EC' in i:
				gaze = 'EC'
				gazeCode = '0'
			else:
				gaze = 'NC'
				gazeCode = '1'
			stimCode=sexCode+raceCode+sideCode+speedCode+gazeCode+instructCode+blockCode
			outString = (subjCode,block, instructions, sex,identity,race,side,speed,gaze,stimCode,i)
			writeToFile(outputFile,outString,writeNewLine=True)
	else:
		stimOrder = NC33
		block = 'EC'
		blockCode = '1'
		instructions = 'Passive'
		instructCode = '0'
		for i in stimOrder:
			if 'm_' in i:
				sex = 'm'
				sexCode = '0'
			else:
				sex = 'f'
				sexCode = '1'
			if '1_' in i:
				identity = '1'
				race = 'w'
				raceCode = '0'
			elif '2_' in i:
				identity = '2'
				race = 'w'
				raceCode = '0'
			elif '3_' in i:
				identity = '3'
				race = 'w'
				raceCode = '0'
			elif '4_' in i:
				identity = '4'
				race = 'w'
				raceCode = '0'
			elif '5_' in i:
				identity = '5'
				race = 'b'
				raceCode = '1'
			elif '6_' in i:
				identity = '6'
				race = 'b'
				raceCode = '1'
			elif '7_' in i:
				identity = '7'
				race = 'b'
				raceCode = '1'
			else:
				identity = '8'
				race = 'b'
				raceCode = '1'
			if 'right' in i:
				side = 'right'
				sideCode = '0'
			else:
				side = 'left'
				sideCode= '1'
			if '2.m' in i:
				speed = 'f'
				speedCode = '0'
			else :
				speed = 's'
				speedCode = '1'
			if 'EC' in i:
				gaze = 'EC'
				gazeCode = '0'
			else:
				gaze = 'NC'
				gazeCode = '1'
			stimCode=sexCode+raceCode+sideCode+speedCode+gazeCode+instructCode+blockCode
			outString = (subjCode,block, instructions, sex,identity,race,side,speed,gaze,stimCode,i)
			writeToFile(outputFile,outString,writeNewLine=True)
		stimOrder = NC67
		block = 'NC'
		blockCode = '0'
		instructions = 'Active'
		instructCode = '1'
		for i in stimOrder:
			if 'm_' in i:
				sex = 'm'
				sexCode = '0'
			else:
				sex = 'f'
				sexCode = '1'
			if '1_' in i:
				identity = '1'
				race = 'w'
				raceCode = '0'
			elif '2_' in i:
				identity = '2'
				race = 'w'
				raceCode = '0'
			elif '3_' in i:
				identity = '3'
				race = 'w'
				raceCode = '0'
			elif '4_' in i:
				identity = '4'
				race = 'w'
				raceCode = '0'
			elif '5_' in i:
				identity = '5'
				race = 'b'
				raceCode = '1'
			elif '6_' in i:
				identity = '6'
				race = 'b'
				raceCode = '1'
			elif '7_' in i:
				identity = '7'
				race = 'b'
				raceCode = '1'
			else:
				identity = '8'
				race = 'b'
				raceCode = '1'
			if 'right' in i:
				side = 'right'
				sideCode = '0'
			else:
				side = 'left'
				sideCode= '1'
			if '2.m' in i:
				speed = 'f'
				speedCode = '0'
			else :
				speed = 's'
				speedCode = '1'
			if 'EC' in i:
				gaze = 'EC'
				gazeCode = '0'
			else:
				gaze = 'NC'
				gazeCode = '1'
			stimCode=sexCode+raceCode+sideCode+speedCode+gazeCode+instructCode+blockCode
			outString = (subjCode,block, instructions, sex,identity,race,side,speed,gaze,stimCode,i)
			writeToFile(outputFile,outString,writeNewLine=True)
