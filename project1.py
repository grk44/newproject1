import pyinputplus as pyip
import csv
import random
import time
import os
# import classes, fun1
# from classes import ship, drones
# from fun1 import *

# Global Use Variables
# shipdata -- created from the CSV file, contains multivalue lists of ships and modules
# shipcount -- number of ships generated from the shipdata file
# newship -- ship use by the player, data entered into the myship class
#

class ship:	
	def __init__(self, name, hull, shield, systems, dronebay, engines, fuel):
		super(ship, self).__init__()
		self.name = name
		self.hull = hull
		self.shield = shield
		self.systems = systems
		self.dronebay = dronebay
		self.engines = engines
		self.fuel = fuel

class drones:
	def __init__(self, dtype, dtier):
		super(drones, self).__init__()
		self.dtype = dtype
		self.dtier = dtier

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def checkstatus():
	clearConsole()
	print('\n===Ship Status===')
	time.sleep(0.2)
	print('Current Hull: {0}'.format(myship.hull))
	time.sleep(0.3)
	print('Current Shield: {0}'.format(myship.shield))
	print('Sytems Level: {0}'.format(myship.systems))
	time.sleep(0.2)
	print('Drone Bay: {0}'.format(myship.dronebay))
	time.sleep(0.5)
	print('Engine Speed: {0}'.format(myship.engines))
	time.sleep(0.2)
	print('Current Fuel: {0} Units'.format(myship.fuel))
	print('\n')
	pass


def loadships():
	shipfile = open('./datafiles/oldships.csv')
	csvreader = csv.reader(shipfile)
	global shipdata
	global shipcount
	shipcount=int(0)
	shipdata = list(csvreader)
	#print(shipdata[2])
	for x in shipdata:
		x[6] = random.randint(0,6)
		shipcount=shipcount+1
		#print(x)
	shipfile.close()


def scanner():
	print('\nScanning....')
	time.sleep(0.5)
	#nearby salvage detected go there?
	#instead of vvv this? vvv
	if myship.systems =='Tier 1':
		nodes=random.randint(1,6)
		print('Range 400:')

	time.sleep(0.3)
	print('Possible Contacts Detected: {0}'.format(nodes))
	jumpsel=pyip.inputYesNo(prompt='Jump to Possible Contact? (Y/N)')	
	if jumpsel == 'yes':
		jumpdrive()
	if jumpsel == 'no':
		return

def hazardroll():
	z=random.randint(0,6)
	if z == 0:
		print('Clean Jump')
		return
	if z > 0 and z < 3:
		g=random.randint(10,30)
		print('!!!\nMinor damage from floating debris\n!!!')
		myship.hull = myship.hull - g
		return
	if z > 3 and z < 6:
		g=random.randint(25,45)
		print('!!!\nModerate damage from large debris\n!!!')
		myship.hull = myship.hull - g
		return
	if z == 6:
		g=random.randint(50,70)
		print('!!!\nMajor damage from floating debris\n!!!')
		myship.hull = myship.hull - g
		return


def jumpdrive():
	if myship.fuel > 0:
		clearConsole()
		time.sleep(0.2)
		print('Preparing FTL...')
		time.sleep(0.3)
		print('Target position locked...')
		time.sleep(0.2)
		print('Execute Jump')
		myship.fuel=myship.fuel - 1
		hazardroll()
		print('Fuel Remaining...{0}\n'.format(myship.fuel))
		global conShip
		# conShip=ship.name('0')
		if myship.systems == 'Tier 1':
			shipcontact= random.randint(0,1)
			if shipcontact == 1:
				print('Nearby Ship Detected')
				x=random.randint(1,5)
				print(shipdata[x][0])
				conShip=ship(shipdata[x][0],shipdata[x][1],shipdata[x][2],shipdata[x][3],shipdata[x][4],shipdata[x][5],shipdata[x][6])
				return
			if shipcontact == 0:
				print('Nothing of Value nearby')
				conShip=ship('0','0', '0', '0','0', '0', '0')
				return
def nearstatus():
	if conShip.name != '0':
		print('Scanning Nearby Ship')
		print('\n===Nearby Ship Status===')
		print('Name Detected: {0}'.format(conShip.name))
		time.sleep(0.2)
		print('Hull: {0}'.format(conShip.hull))
		time.sleep(0.3)
		print('Shield: {0}'.format(conShip.shield))
		print('Sytems Level: {0}'.format(conShip.systems))
		time.sleep(0.2)
		print('Drone Bay: {0}'.format(conShip.dronebay))
		time.sleep(0.5)
		print('Engine Speed: {0}'.format(conShip.engines))
		time.sleep(0.2)
		print('Current Fuel: {0} Units'.format(conShip.fuel))
		print('\n')
		return
	if conShip.name =='0':
		print('Nothing Nearby')
		return

def salvage():
	clearConsole()
	nearstatus()
	# if conShip.name != '0':
	# 	print('Scanning Nearby Ship')
	# 	print('\n===Nearby Ship Status===')
	# 	print('Name Detected: {0}'.format(conShip.name))
	# 	time.sleep(0.2)
	# 	print('Hull: {0}'.format(conShip.hull))
	# 	time.sleep(0.3)
	# 	print('Shield: {0}'.format(conShip.shield))
	# 	print('Sytems Level: {0}'.format(conShip.systems))
	# 	time.sleep(0.2)
	# 	print('Drone Bay: {0}'.format(conShip.dronebay))
	# 	time.sleep(0.5)
	# 	print('Engine Speed: {0}'.format(conShip.engines))
	# 	time.sleep(0.2)
	# 	print('Current Fuel: {0} Units'.format(conShip.fuel))
	# 	print('\n')
	# if conShip.name =='0':
	# 	print('Nothing Nearby')
	# 	return
	if conShip.name == '0':
		return
	print('No life signs detected...\nBeginning Salvage Operation')

	depdrone=pyip.inputYesNo(prompt='Deploy Drones? (Y/N)')
	if depdrone == 'yes':
		droneselect()
	if depdrone == 'no':
		return

def droneselect():	
	clearConsole()
	print('===Drones Avaliable===')
	time.sleep(0.2)
	print('Drone Bay [1] Status - Drone Type: {0} - Tier: {1}'.format(mydrone1.dtype,mydrone1.dtier))
	time.sleep(0.3)
	print('Drone Bay [2] Status - Drone Type: {0} - Tier: {1}'.format(mydrone2.dtype,mydrone2.dtier))
	time.sleep(0.2)
	print('Drone Bay [3] Status - Drone Type: {0} - Tier: {1}'.format(mydrone3.dtype,mydrone3.dtier))
	
	dronesel=pyip.inputMenu(['Bay 1','Bay 2','Bay 3'],numbered=True,prompt='\nDrone to deploy to nearby ship:\n')
	if dronesel == 'Bay 1':
		dronetype=mydrone1.dtype
	if dronesel == 'Bay 2':
		dronetype=mydrone2.dtype
	if dronesel == 'Bay 3':
		dronetype=mydrone3.dtype

def dronedeploy():
	clearConsole()
	nearstatus()
	if conShip == '0':
		print('\nNo Ship To Salvage Nearby')
		return
	if dronesel == 'Salvage':
		if conShip.hull > myship.hull:
			hulldiff = conShip.hull - myship.hull
			print('Extra Hull plating found...')
			print('Possible return: {0}'.format(hulldiff))
			time.sleep(0.3)
			print('Drone is harvesting...')
			time.sleep(0.5)
			q=random.randint(0,hulldiff)
			print('Hull Plating added\nTotal harvested:{0}')
			myship.hull = myship.hull + q
			print('New hull Status: {0}'.format(myship.hull))
		if conShip.fuel > 0
			time.sleep(0.3)
			print('Retrieving Fuel...')
			myship.fuel = myship.fuel + conShip.fuel
			time.sleep(0.5)
			print('Fuel Retrieved: {0} units now avaliable'.format(myship.fuel))


def systems():
	clearConsole()
	print('\n\n===Systems===')
	time.sleep(0.5)
	if myship.systems == 'Tier 1':
		print('Tier 1 Systems Detected')
		time.sleep(0.75)
		print('Engine jump range {0}:'.format(myship.engines))
		time.sleep(0.25)
		print('Scanner range 400:')
		time.sleep(0.3)
		print("All Systems [OK]")
		time.sleep(0.2)
		print('Ready for input\n')

		syssel=''	
		syssel=pyip.inputMenu(['Scan','Return'],numbered=True)
		if syssel == 'Scan':
			#print('Scanning')				
			scanner()
		# if syssel == 'Exec FTL':
		# 	print('Plotting FTL Jump')
		if syssel == 'Return':
			pass
	if myship.systems == 'Tier 2':
		print('Tier 2 Systems Detected')
		time.sleep(0.75)
		print('Engine jump range {0}:'.format(myship.engines))
		time.sleep(0.25)
		print('Scanner range 600:')
		time.sleep(0.3)
		print("All Systems [OK]")
		time.sleep(0.2)
		print('Ready for input\n')



clearConsole()
print('=======================\n=======================')
print('You awaken in an empty space ship.\nYou have no idea where you are or how you got here\n')
# myshipname=input('What is the name of your ship?: ')

myship=ship('Navigator I', 100, 150, 'Tier 1', 1, 300, 15)
mydrone1=drones('Salvage', '1')
mydrone2=drones('Empty','0')
mydrone3=drones('Empty','0')
loadships()
conShip=ship('0','0', '0', '0','0', '0', '0')


dronesel=mydrone1.dtype
while myship.hull > 0:
	print('Selected Drone: {0}'.format(dronesel))
	menusel=pyip.inputMenu(['Check Ship Status', 'Use Ship Systems', 'Contact Nearby Ship'],prompt='What would you like to do?\n',numbered=True)
	print(menusel)
	if menusel == 'Check Ship Status':
		checkstatus()
	if menusel == 'Use Ship Systems':
		systems()
	if menusel == 'Contact Nearby Ship':
		salvage()
		
	pass