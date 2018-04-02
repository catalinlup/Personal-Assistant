try:
	import pygame
except:
	print("Error Please Install Pygame")
class Player:
	music=[]
	def __init__(self):
		try:
			pygame.mixer.init()
		except:
			print("Error Failed to Initialize Mixer")
	def addMusic(self,filepath):
		if type(filepath)==str:
			self.music.append(filepath)
		else:
			print("Error str required as Filepath")
	def getSize(self):
		return len(self.music)
	def PlayMusic(self,val):
		if type(val)==int:
			if val>=self.getSize():
				print("Error Index Too Large")
			else:
				pygame.mixer.music.load(self.music[val])
				pygame.mixer.music.play()
				while pygame.mixer.music.get_busy()==True:
					continue
		else:
			print("Error int is required as Index")
	def PlayMusicByFilepath(self,filepath):
		if type(filepath)==str:
			pygame.mixer.music.load(filepath)
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy()==True:
				continue
		else:
			print("Error str is required as Filepath")
			
		
	
	
