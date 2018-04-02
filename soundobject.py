from codes import*
soundObjectName="soundObject"
days={'Monday':10000,'Tuesday':20000,'Wednesday':30000,'Thursday':40000,'Friday':50000,'Saturday':60000,'Sunday':70000}
class soundObject:
	name=""
	filename=""
	time=""
	day=""
	message=""
	def __init__(self,name,filename,time,day,message):
		self.name=name
		self.filename=filename
		self.time=time
		self.day=day
		self.message=message
	def PrintSoundObject(self):
		print(self.name+" "+self.filename+" "+self.time+" "+self.day+" "+self.message)
	def IntValueOfTime(self):
		d = self.day
		h,m=self.time.split(':')
		h=int(h)
		m=int(m)
		d=str(d)
		#print(d)
		val_d = int(days[d])
		#print(val_d)
		return val_d+60*h+m

def getKey(sobject):
	return sobject.IntValueOfTime()
def SortSoundObjectList(objectlist):
	objectlist=sorted(objectlist,key=getKey)
	return objectlist
