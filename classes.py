UNLIMITED = 999999999
desertCampList=[]

class Truck:
	oilCount = 0
	id = 0
	moves = 0

	def pickup(self,count):
		desertCampList[self.id].minus(count)
		self.oilCount += count

	def unload(self):
		desertCampList[self.id].add(self.oilCount)
		self.oilCount = 0

	def move(self,direction):
		if(self.oilCount<0):
			raise Exception("OI NO OIL LA SIAL")
		self.moves += 1
		if(direction):
			self.pickup(min(3,desertCampList[self.id].oilCount)) #picks up all available oil
			self.id += 1
		else:
			self.pickup(1)
			self.id -= 1
		self.oilCount -= 1
		self.unload()
		# print("Bob is currently at " + str(self.id))


class DesertCamp:

	oilCount = 0
	id = 0
	totalOilCount = 0

	def __init__(self,id,oilCount=0):
		self.oilCount = oilCount
		self.id = id

	def add(self,count):
		self.oilCount += count
		self.totalOilCount = max(self.totalOilCount,self.oilCount)
		if(self.oilCount<0):
			raise Exception('ERROR SIAL CAMP LESS THAN 0')

	def minus(self,count):
		self.oilCount -= count
		if(self.oilCount<0):
			raise Exception('ERROR SIAL CAMP LESS THAN 0')

def start(n,desertCampList):
	desertCampList.append(DesertCamp(0,UNLIMITED))
	for i in range(1,n+1):
		desertCampList.append(DesertCamp(i))

def checkWinningMove(truck,n,desertCampList):
	if((n - truck.id)==3 & desertCampList[truck.id].oilCount>=3):
		print("difference : "+str(n - truck.id) +" oilCount " + str(desertCampList[truck.id].oilCount))
		truck.move(1)
		truck.move(1)
		truck.move(1)

def checkSufficient(n,desertCamp,id):
	# print("ID :" + str(id) + "only has count: " + str(desertCamp.oilCount))
	if(desertCamp.oilCount >= (3+id)): #ensures that truck will have enough to traverse back to base camp, bruteforce technique
		return True
	else:
		return False

def checkWin(truck,n):
	if (truck.id == n):
		print("TOTAL MOVES = " + str(truck.moves) + "\nYOU WON !\n")

		return True
	else:
		return False