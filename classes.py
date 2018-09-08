class desert:

	def __init__(self,id,oilCount=0):
		self.oilCount = oilCount
		self.id = id

	def drop(self,count):
		self.oilCount += count

	def pickup(self,count):
		self.oilCount -+ count

def start(n,desertCamp):
	for i in range(0,n):
		desertCamp.append(desert(i))