from myro import *
import random
import time
import os

def needToSleep():
	start=time.clock()
	while (time.clock()-start)<20:
		os.system('cls')
		if getBright("center") < 1000000: #define 1000 to be threshold, can use getBright("center") too?
			print "Sleeping..."
			time.sleep(5)
			print "Sleep Complete!"
			break
		else:
			print "Time Left: "+str(20-(round(time.clock()-start,2)))
			turnLeft(random.uniform(0.01,1), random.uniform(0.1,2))
			turnRight(random.uniform(0.01,1), random.uniform(0.1,2))
	
	if (time.clock()-start)<20:
		beep(0.5, 500)
		beep(0.5, 400)
		beep(0.5, 300)
		beep(0.5, 200)
		beep(0.5, 100)
		return True
	
	else:
		return False
