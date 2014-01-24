from myro import *
import random
import time
import os


def checkTrack():
	if getLine("left") and getLine("right"):
		return True;
	else:
		return False;
		
def trackMove():
	move(-.1,0)
	if getTurnDir()=="left":
		stop()
		rotate(.1)
		while True:
			if getTurnDir()==0:
				stop()
				break
	
	if getTurnDir()=="right":
		stop()
		rotate(-.1)
		while True:
			if getTurnDir()==0:
				stop()
				break

def getTurnDir():
	if getLine("left") and not getLine("right"):
		return "left"
	elif not getLine("left") and getLine("right"):
		return "right"
	else:
		return 0
		
def needToPoop():
	start=time.clock()
    #insert fart sound
	didStart=False
	while (time.clock()-start)<30: #define 30seconds to be how long the user has to help the pet
		os.system('cls')
		if not checkTrack():
			print "Time Left: "+str(30-(round(time.clock()-start,2)))+"s"
			#turnLeft(random.uniform(0.01,1), random.uniform(0.1,2))
			#turnRight(random.uniform(0.01,1), random.uniform(0.1,2))
		else:
			print "Going to the washroom..."
			didStart=True
			startMovement()
			print "All done!"
			time.sleep(2)
			return True
			break

	print didStart
	return didStart
##	if not didStart:
##		return False

def startMovement():
	while getLine("right") or getLine("left"): #1000 is threshold
		trackMove()
		
	stop()
	#insert shitting animation
	beep(2, 300)
	rotate(-.1)
	while True:
		if getLine("right") and getLine("left"):
			stop()
			break
	
	while getLine("right") or getLine("left"):
		trackMove()
	
	stop()
