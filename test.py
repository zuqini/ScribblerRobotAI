import os
import time
import random		
def swag():
	for i in range(0,100):
		speedType=random.randint(0,8)
		Lspeed=random.uniform(0.3,0.5)
		Hspeed=random.uniform(0.001,0.15)
		print "Status:",
		if i<25:
			print "Booting Up the Robot..."
		elif i<50:
			print "Configuring Settings..."
		elif i<75:
			print "Initializing Robot..."
		else:
			print "Finalizing Process..."

		print "Loading:",
		for j in range(0,i/4):
			print "@",
		for k in range(i/4,25):
			print " ",
		print str(i)+"%",
		if i>95:
			time.sleep(3)
		elif speedType==0:
			time.sleep(Lspeed)
		else:
			time.sleep(Hspeed)
		print "\n"
		if i!=99:
			os.system('cls')

def troll():
	while True:
		swag()
		print "ERROR: Restarting..."
		time.sleep(2)
		os.system('cls')
	
troll()