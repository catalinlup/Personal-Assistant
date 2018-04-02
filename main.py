from player import*
from ProgramGeter import*
from queue import*
from osCommands import*
import datetime
audioFilePath="res/audio/"
mnPlayer=Player()
rfile=open(DATA_COM_NAME,"r")
PROGRAM_TO_RUN_HEADLESS=str(rfile.read())
rfile.close()
program12=Program(PATH_TO_PROGRAMS+"/"+PROGRAM_TO_RUN_HEADLESS)
events=queue()
def getHourMinutes():
	now=datetime.datetime.now()
	day=(datetime.datetime.today().weekday()+1)*10000
	return int(day)+int(now.hour)*60+int(now.minute)
def getCurrentTimeInStr():
	tm="("+PROGRAM_TO_RUN_HEADLESS+")"
	now=datetime.datetime.now()
	day=(datetime.datetime.today().weekday()+1)
	tm+=" Day: "
	tm+=str(day)
	tm+=" Time: "
	tm+=str(now.hour)
	tm+=":"
	tm+=str(now.minute)
	return tm
def Provizoriu():
	tm=getHourMinutes()
	#print(tm)
	for key in program12.sounds:
		if tm==program12.sounds[key].time:
			mnPlayer.PlayMusicByFilepath(audioFilePath+program12.sounds[key].filename)

def PlayEvent(event):
	if type(event)==soundObject:
		ClearScreen()
		print("Currently playing "+event.name+ " ~~~filepath: "+ event.filename)
		mnPlayer.PlayMusicByFilepath(audioFilePath+event.filename)
def AddEvent(event):
	if type(event)==soundObject:
		events.push(event)
def Init():
	for key in program12.sounds:
		AddEvent(program12.sounds[key])
	events.Print()
def CheckForEvents():
	ct=getHourMinutes()
	#print(ct)
	while events.empty()==False and type(events.front())==soundObject and events.front().IntValueOfTime()<ct:
		events.pop()
	if events.empty()==False and type(events.front())==soundObject and events.front().IntValueOfTime()==ct:
		PlayEvent(events.front())
		events.pop()


def main():
	print("Welcome To Personal Assistant")
	Init()
	while True:
		ClearScreen()
		print(getCurrentTimeInStr())
		CheckForEvents()
		continue


main()
