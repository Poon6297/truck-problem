###########################

# 1. Algorithm retakes the load even though it is not needed

###########################
from classes import *

UNLIMITED = 999999999
n = int(input("Enter n: "))
desertCampList=[]
ready = 0

##############
# 3 is needed to have an effective move, 1 to go, 1 to store, 1 to come back
##############

# DIRECTION #
# 0 = left  #
# 1 = right #

winningCondition=[0]*(n+1) #creates an array to dynamically calculate the amount of oil required
for i in range(n-2,n+1,1):
	winningCondition[i] = 0
winningCondition[n-3] = 3
for i in range(n-4,0,-1):
	winningCondition[i]=(winningCondition[i+1]*3) - 1

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
			print("OI NO OIL LA SIAL")
		self.moves += 1
		if(direction):
			self.pickup(min(3,desertCampList[self.id].oilCount)) #picks up all available oil
			self.id += 1
		else:
			self.pickup(1)
			self.id -= 1
		self.oilCount -= 1
		self.unload()
		print("Bob is currently at " + str(self.id))


class DesertCamp:

	oilCount = 0
	id = 0
	totalOilCount = 0

	def __init__(self,id,oilCount=0):
		self.oilCount = oilCount
		self.id = id

	def add(self,count):
		self.oilCount += count
		self.totalOilCount += count
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
	print("ID :" + str(id) + "only has count: " + str(desertCamp.oilCount))
	# if(desertCamp.oilCount >= (3+id)): #ensures that truck will have enough to traverse back to base camp, bruteforce technique
	if(desertCamp.oilCount >= (3**(n-id-2)-1)): #more efficient algorithm but DOESN'T MAKE IT FASTER???
		return True
	else:
		return False

def checkWin(truck,n):
	if (truck.id == n):
		print("TOTAL MOVES = " + str(truck.moves) + "\nYOU WON !\n")

		return True
	else:
		return False

start(n,desertCampList)
bob = Truck()



while(1):
	checkWinningMove(bob,n,desertCampList)
	if(checkWin(bob,n)):
		for i in range(n):
			print("ID :" + str(i) + "only has total count: " + str(desertCampList[i].totalOilCount))
		break
	elif(checkSufficient(n,desertCampList[bob.id],bob.id)):
		ready = 1
		bob.move(1)
	else:
		bob.move(0)


