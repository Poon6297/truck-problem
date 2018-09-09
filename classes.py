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
			raise Exception("OI NO OIL LA")
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

def start(n,desertCampList): #initialize camps
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ............. THE TRUCK IS MOVING ................\n\n\n\n\n\n\n\n")
	desertCampList.append(DesertCamp(0,UNLIMITED))
	for i in range(1,n+1):
		desertCampList.append(DesertCamp(i))

def checkWinningMove(truck,n,desertCampList): #returns true if the truck can go to target camp
	if((n - truck.id)==3 & desertCampList[truck.id].oilCount>=3):
		print("difference : "+str(n - truck.id) +" oilCount " + str(desertCampList[truck.id].oilCount))
		return True
	else:
		return False

def checkSufficient(winningCondition,bob,desertCampList): #returns true if the total oil count to get to target camp is hit
	if(desertCampList[1].oilCount>=winningCondition[1]):
		return True
	else:
		return False


def checkWin(truck,n): #returns true if truck is at target camp
	if (truck.id == n):
		print("TOTAL MOVES = " + str(truck.moves) + "\nYOU WON !\n")
		return True
	else:
		return False

def setWinningCondition(n,winningCondition): 	#calculates the total oil count requirement at each camp to get to target camp
	for i in range(n-2,n+1,1):
		winningCondition[i] = 0
	winningCondition[n-3] = 3
	for i in range(n-4,0,-1):
		winningCondition[i]=(winningCondition[i+1]*3) - 1