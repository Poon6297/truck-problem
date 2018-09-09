from classes import *


ready = False

##############
# 3 is needed to have an effective move, 1 to go, 1 to store, 1 to come back
#
#
# DIRECTION #
# 0 = left  #
# 1 = right #
#
##############


n = int(input("Enter n: "))
winningCondition=[0]*(n+1) #creates an array to dynamically calculate the amount of oil required

setWinningCondition(n,winningCondition)
start(n,desertCampList)
bob = Truck()
# for i in range(n+1):
# 	print(winningCondition[i])


while(1):
	if(checkWinningMove(bob,n,desertCampList)): #checks for winning move and executes
		bob.move(1)
		bob.move(1)
		bob.move(1)
		if(checkWin(bob,n)):
			for i in range(n):
				print("ID :" + str(i) + "only has total count: " + str(desertCampList[i].totalOilCount))
		break
	if(ready == True):
		while(desertCampList[bob.id].oilCount>3): #moves all oil to next desert camp
			bob.move(1)
			bob.move(0)
		bob.move(1)  #moves oil to desert camp without coming back
	else:
		bob.move(1)
		if(checkSufficient(winningCondition,bob,desertCampList)==True): #if oil is sufficient for truck to traverse till the end
			ready = True
		else:
			# time.sleep(10)
			bob.move(0)




