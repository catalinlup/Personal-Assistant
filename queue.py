try:
	from soundobject import*
except:
	print("Couldn't import soundobject in queue")
	pass
class queue:
	actual_queue=[]
	def push(self,element):
		if type(element)==soundObject:
			self.actual_queue.append(element)
			self.actual_queue=SortSoundObjectList(self.actual_queue)
	def empty(self):
		return len(self.actual_queue)==0
	def front(self):
		if self.empty()==False:
			return self.actual_queue[0]
	def pop(self):
		if self.empty()==False:
			self.actual_queue.remove(self.actual_queue[0])
	def Print(self):
		for x in self.actual_queue:
			if type(x)==soundObject:
				print(x.IntValueOfTime())
