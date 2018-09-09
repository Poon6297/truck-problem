###########################

# 1. Algorithm retakes the load even though it is not needed

###########################
from classes import *


n = input("Enter n: ")
##############
# 3 is needed to have an effective move, 1 to go, 1 to store, 1 to come back
##############

# DIRECTION #
# 0 = left  #
# 1 = right #


start(n,desertCampList)
bob = Truck()

while(1):
	checkWinningMove(bob,n,desertCampList)
	if(checkWin(bob,n)):
		for i in range(n):
			print("ID :" + str(i) + "only has total count: " + str(desertCampList[i].totalOilCount))
		break
	elif(checkSufficient(n,desertCampList[bob.id],bob.id)):
		bob.move(1)
	else:
		bob.move(0)


