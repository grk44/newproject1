import pyinputplus as pyip
import csv
import random
import time

#Global Use Variables
# shipdata -- created from the CSV file, contains multivalue lists of ships and modules
# shipcount -- number of ships generated from the shipdata file
# newship -- ship use by the player, data entered into the myship class

class myship:	
	def __init__(self, myshipname, hull, shield, systems, weapons, engines, fuel):
		super(myship, self).__init__()
		self.myshipname = myshipname
		self.hull = hull
		self.shield = shield
		self.systems = systems
		self.weapons = weapons
		self.engines = engines
		self.fuel = fuel


def checkstatus():
	print('\n===Ship Status===')
	print('Current Hull: {0}'.format(newship.hull))
	print('Current Shield: {0}'.format(newship.shield))
	print('Sytems Level: {0}'.format(newship.systems))
	print('Weapons Level: {0}'.format(newship.weapons))
	print('Engine Speed: {0}'.format(newship.engines))
	print('Current Fuel: {0} Units'.format(newship.fuel))
	print('\n')
	pass


def loadships():
	shipfile = open('./datafiles/oldships.csv')
	csvreader = csv.reader(shipfile)
	global shipdata
	global shipcount
	shipcount=int(0)
	shipdata = list(csvreader)
	# print(csvdata[2])
	for x in shipdata:
		x[6] = random.randint(0,6)
		shipcount=shipcount+1
		#print(x)
	shipfile.close()

def systems():
	print('\n\n===Systems===')
	time.sleep(0.5)
	if newship.systems == 'Tier 1':
		print('Tier 1 Systems Detected')
		time.sleep(0.75)
		print('Engine jump range {0}:'.format(newship.engines))
		time.sleep(0.25)
		print('Scanner range 400:')
		time.sleep(0.5)
		print("All Systems [OK]")
		time.sleep(0.5)
		print('Ready for input')
	if newship.systems == 'Tier 2':
		print('Tier 2 Systems Detected')
		time.sleep(0.75)
		print('Engine jump range {0}:'.format(newship.engines))
		time.sleep(0.25)
		print('Scanner range 600:')
		time.sleep(0.5)
		print("All Systems [OK]")
		time.sleep(0.5)
		print('Ready for input')




print('=======================\n=======================')
print('You awaken in an empty space ship.\nYou have no idea where you are or how you got here\n')
# myshipname=input('What is the name of your ship?: ')

newship=myship('Navigator I', 100, 150, 'Tier 1', 'Tier 1', 300, 15)
loadships()
while newship.hull > 0:
	menusel=pyip.inputMenu(['Check Ship Status', 'Use Ship Systems'],prompt='What would you like to do?\n',numbered=True)
	print(menusel)
	if menusel == 'Check Ship Status':
		checkstatus()
	if menusel == 'Use Ship Systems':
		systems()
		
	pass
