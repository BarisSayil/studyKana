from random import shuffle

def getList(kanaType):						#Reads the relevant .txt file to get the list of kana to study.
	listOfKana=[]
	if kanaType=='h':
		file='hiragana.txt'
	elif kanaType=='k':
		file='katakana.txt'
	with open(file) as f:
		while 1:
			line=f.readline()
			if line=='':
				break
			line=line.split()
			listOfKana.append(line)
	shuffle(listOfKana)
	return listOfKana

def passiveStudy(theList):					#Shows the kana and you type the pronunciation.
	for i in range(len(theList)):
		a=input(theList[i][0]+'\n')
		if a==theList[i][1]:
			print('CORRECT!\n')
		else:
			print('WRONG! The answer is {}.\n'.format(theList[i][1]))
			wrong.append(theList[i])

def activeStudy(theList):					#Shows the pronunciation and you write the kana on a piece of paper.
	print("Write the kana on a paper, if it's correct press enter. Otherwise type something and then press enter.\n")
	for i in range(len(theList)):
		a=input(theList[i][1])
		a=input(theList[i][0]+'\n')
		if a!='':
			wrong.append(theList[i])
			print()

def getKanaType():							#Asks the user if he wants to study hiragana or katakana. He types h or k.
	valid=False
	while not valid:
		kanaType=input('Hey there. Wanna study hiragana or katakana? h/k:')
		if kanaType=='h' or kanaType=='k':
			valid=True
	return kanaType

def getStudyType():							#Asks the user if he wants to study actively or passively. He types a or p.
	valid=False
	while not valid:
		studyType=input('Wanna study actively or passively? a/p:')
		if studyType=='a' or studyType=='p':
			valid=True
	return studyType

def study(studyType):						#Starts the study session.
	if studyType=='a':
		activeStudy(theList)
	elif studyType=='p':
		passiveStudy(theList)

def showResults():							#Shows the kana that need further studying, if any.
	if len(wrong):
		print('Well done. You need to study these a bit more:')
		for elem in wrong:
			print(elem)	
	else:
		print('Congratulations, you are perfection itself :)')


wrong=[]

kanaType=getKanaType()

theList=getList(kanaType)

studyType=getStudyType()

study(studyType)

showResults()
