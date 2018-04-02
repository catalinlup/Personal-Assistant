try:
	import xml.etree.ElementTree as ET
except:
	print("Error Install XML Parser")

from soundobject import*

class Program:
	sounds={}
	def __init__(self,filepath):
		self.tree = ET.parse(filepath)
		self.root = self.tree.getroot()
		for sb in self.root.findall(soundObjectName):
			obj=soundObject(sb.get('name'),sb.find('filename').text,sb.find('time').text,sb.find('day').text)
			self.sounds[obj.name]=obj
	def printSounds(self):
		for key in self.sounds:
			self.sounds[key].PrintSoundObject()
