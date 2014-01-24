from myro import *
import time
import random
import math
import os
import string

from shit import *
from sleep import *
from read import *

random.seed()
init("COM4")

setLED("left", "off")
setLED("right", "off")
setLED("front", "off")
setLED("back", "off")
autoCamera()

clear = lambda: os.system('cls')
x=0
HAPPY=50
EAT=0
POOP=1
SLEEP=2
FETCH=3
fRED=0
fBLUE=1
fYELLOW=2
# status[]={"idle", "eat", "poop", "sleep"}
percent=[50,50,50,50]
food=[30,30,30]
didIdle=False

f = open("pName.txt")
pName = f.readlines()
f.close()

for i, s in enumerate(pName):
	pName[i]=s.strip()

def idle():
	global didIdle
	start = time.clock()
	willMove=random.randint(0,3)
	rotate=random.uniform(-1,1)
	speed=random.uniform(-1,1)
	duration=random.uniform(1,3)
	
	if willMove==0:
		didIdle=True
		while (time.clock()-start)<duration:
			move(speed,rotate)
	else:
		didIdle=False
	stop()

def changeFood():
	global food
	food[fRED]=2*math.cos((2*math.pi/9)*x)+2
	food[fBLUE]=2*math.cos((2*math.pi/9)*(x-3))+2
	food[fYELLOW]=2*math.cos((2*math.pi/9)*(x-6))+2

def changeUI():
##	global percent
	clear()
	print string.center("myPetto User Interface: "+name, 30)
	
	print "Fullness:     " + str(percent[EAT])+"[",
	for i in range(25):
		if i <= int(percent[EAT])/4:
			print "F",
		else:
			print "-",
	print "]\n"
	
	print "POOP:         " + str(percent[POOP])+"[",
	for i in range(25):
		if i < int(percent[POOP])/4:
			print "P",
		else:
			print "-",
	print "]\n"
	
	print "Energy Level: " + str(percent[SLEEP])+"[",
	for i in range(25):
		if i < int(percent[SLEEP])/4:
			print "Z",
		else:
			print "-",
	print "]\n"
	
	print "Love:         " + str(percent[FETCH])+"[",
	for i in range(25):
		if i < int(percent[FETCH])/4:
			print "F",
		else:
			print "-",
	print "]\n"
	
	print "Happiness:    " + str(HAPPY)+"[",
	for i in range(25):
		if i < HAPPY/4:
			print "H",
		else:
			print "-",
	print "]\n"

def loadBar():
	for i in range(0,101):
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
		for j in range(0,i/4+1):
			print "@",
		for k in range(i/4,26):
			print " ",
		print str(i)+"%",
		if i>95:
			time.sleep(1)
		elif speedType==0:
			time.sleep(Lspeed)
		else:
			time.sleep(Hspeed)
		print "\n"
		if i!=100:
			clear()

def save():
	f=open(name+ '.save', 'w')
	f.write(name+ '\n')
	f.write(str(x)+ '\n')
	for i in range (0,4):
		f.write(str(percent[i])+ '\n')
	f.close()

choice=raw_input("Create a new pet or load a previous one? ('n' - new, 'l' - load): ")
while choice != 'n' and choice != 'l':
	choice=raw_input("Please enter a valid input-> 'n' - new, 'l' - load: ")

clear()

if choice == 'n':
	choice=raw_input("Do you want a custom or random pet name? ('c' - custom, 'r' - random): ")
	while choice != 'c' and choice != 'r':
		choice=raw_input("Please enter a valid input-> 'c'-custom or 'r'-random: ")

	if choice == 'r':
		num=random.randint(0,len(pName)-1)
		name=pName[num]
	elif choice == 'c':
		name=raw_input("Please give your pet a name: ")
elif choice == 'l':		
	name=raw_input("Enter the name of the pet you want to load. (Case-sensitive): ")
	while not os.path.exists(name+'.save'):
		name=raw_input('Pet not found, please try again: ')
	f = open(name+'.save')
	name=f.readline().strip()
	x=int(f.readline().strip())
	for i in range (0,4):
		percent[i]=int(f.readline().strip())
	f.close()

clear()
print "Get ready to meet your new pet - " + name + "!"
time.sleep(0.5)
clear()
##loadBar()

while True:
##	global percent
##	global HAPPY
	changeUI()
	
	didDie=False
	for p in percent:
		if p==0:
			didDie=True
	if didDie:
		clear()
		print "Oh No! "+name+" has died!"
		time.sleep(5)
		break
	
	idle()
	if getObstacle("center") > 1000:
		#user wants to do an event
		print "What do you want to do with your pet?"
		print "Type 'e' to feed it"
		print "     'p' to take it to the bathroom"
		print "     'z' to put it to sleep"
		print "     'f' to play fetch"
		print "     'b' to go back"
		print "     's' to save your pet's state"
		print "     'x' to exit the game"
		
		event=raw_input()
		while event != 'e' and event != 'p' and event != 'z' and event != 'f' and event != 'b'  and event != 's' and event != 'x':
			print "Invalid Input: Please try again \r"
			event=raw_input()
		
		clear()
		if event == 'e':
			changeFood()
			sum=0
			for c in food:
				sum+=c
			foodChoice=random.uniform(0,sum)
			if foodChoice<food[fRED]:
				hungry("Apple")
			elif foodChoice<(food[fRED]+food[fBLUE]):
				hungry("Blueberry")
			else:
				hungry("Grape")
			percent[EAT]+=24
##			global x
			x+=1
		elif event == 'p':
			didPoop=needToPoop()
			if didPoop:
				percent[POOP]+=22
			else:
				print "Oh no! You were too slow in taking him to the washroom!"
		elif event == 'z':
			didSleep=needToSleep()
			if didSleep:
				percent[SLEEP]+=22
			else:
				print "Oh no! You were too slow in putting your pet to sleep!"
		elif event == 'f':
			fetch()
			percent[FETCH]+=23
		elif event == 's':
			save()
			print "File for " + name + " saved successfully!"
		elif event == 'x':
			sure=raw_input("Are you sure? Unsaved progress will be lost. ('y'/'n'): ")
			while sure != 'y' and sure != 'n':
				print "Invalid input. Please type 'y'-yes or 'n'-no"
				sure=raw_input("Are you sure? Unsaved progress will be lost. ('y'/'n'): ")
				
			if sure=='y':
				break
		else:
			pass
		time.sleep(2)

	for i in range(len(percent)):
		if percent[i]>100:
			percent[i]=100
			
	if didIdle:
		percent[EAT]-=4
		percent[POOP]-=2
		percent[SLEEP]-=1
		percent[FETCH]-=3
		for i in range(len(percent)):
			if percent[i]<0:
				percent[i]=0
		h=0
		for i in percent:
			h+=i
		HAPPY=h/int(len(percent))
