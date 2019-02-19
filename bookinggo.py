import requests

try: 
  import simplejson as json
except:
  import json

urlDave = "https://techtest.rideways.com/dave"
urlEric = "https://techtest.rideways.com/eric"
urlJeff = "https://techtest.rideways.com/jeff"

print("Hello! Welcome to BookingGo!")
print("I see you want to book some transport. Please type the Co-ordinates that you are currently at!")

whileLoop = 1

while(whileLoop):
	startCords = input("(Type 'def' to use default values): ")
	if (startCords == 'def'):
		startCords = '3.410632,-2.157533'
		whileLoop = 0
	else:
		whileLoop = 0

whileLoop = 1

print("Great! Now please type the Co-ordinates that you want to end up in")

while(whileLoop):
	endCords = input("(Type 'def' to use default values): ")
	if (endCords == 'def'):
		endCords = '3.410632,-2.157533'
		whileLoop = 0
	else:
		whileLoop = 0

#"https://techtest.rideways.com/dave?pickup=3.410632,-2.157533&dropoff=3.410632,-2.157533"

passengerNo = input("Type the number of people you would like us to pick up: ")

parameters = "?pickup=" + endCords + "&dropoff=" + endCords
getUrlDave = urlDave + parameters
getUrlEric = urlEric + parameters
getUrlJeff = urlJeff + parameters

attempts = 0

while attempts < 3:
	try:
		rd = requests.get(getUrlDave)
		dd = rd.json()
		if str(rd) == "<Response [200]>":
			print ("success d")
			break
		else:
			attempts += 1
			print ("Response Error")
			print (rd)
	except e:
		attempts += 1
		print ("Error ")

attempts = 0
while attempts < 3:
	try:
		re = requests.get(getUrlDave)
		de = re.json()
		if str(re) == "<Response [200]>":
			print ("success e")
			break
		else:
			attempts += 1
			print ("Response Error")
			print (re)
	except e:
		attempts += 1
		print ("Error ")

attempts = 0
while attempts < 3:
	try:
		rj = requests.get(getUrlDave)
		dj = rj.json()
		if str(rj) == "<Response [200]>":
			print ("success j")
			break
		else:
			attempts += 1
			print ("Response Error")
			print (rj)
	except e:
		attempts += 1
		print ("Error ")
"""
rd = requests.get(getUrlDave)
dd = rd.json()

re = requests.get(getUrlEric)
de = re.json()

rj = requests.get(getUrlJeff)
dj = rj.json()
"""

print ("r")
print (rd)
print (re)
print (rj)
print("")
"""
print ("r.status_code")
print(r.status_code)
print("")

print ("r.headers")
print (r.headers)
print("")

print ("r.content")
print (r.content)
print("")

print ("data")
print (d)
print("")

print ("supplier_id")
print(d['supplier_id'])
print("")

print ("pickup")
print (d['pickup'])
print("")

print ("dropoff")
print (d['dropoff'])
print("")

print ("options")
print (d['options'])
print("")
"""

carPriceListD = []
carPriceListE = []
carPriceListJ = []

carPriceList = []
carCapacityList = [
					['STANDARD', 4],
					['EXECUTIVE', 4],
					['LUXURY',4],
					['PEOPLE_CARRIER',6],
					['LUXURY_PEOPLE_CARRIER',6],
					['MINIBUS',16]
				]


for item in dd['options']:
	#print (item)
	#print (item['car_type'])
	for car in carCapacityList:
		if car[0] == item['car_type'] and car[1] >= int(passengerNo):
			carPriceListD.append([item['car_type'], item['price'], "Dave"])

for item in de['options']:
	#print (item)
	#print (item['car_type'])
	for car in carCapacityList:
		if car[0] == item['car_type'] and car[1] >= int(passengerNo):
			carPriceListE.append([item['car_type'], item['price'], "Eric"])

for item in dj['options']:
	#print (item)
	#print (item['car_type'])
	for car in carCapacityList:
		if car[0] == item['car_type'] and car[1] >= int(passengerNo):
			carPriceListJ.append([item['car_type'], item['price'], "Jeff"])

print (carPriceListD)
print (carPriceListE)
print (carPriceListJ)

for item in dd['options']:
	#print (item)
	#print (item['car_type'])
	for car in carCapacityList:
		if car[0] == item['car_type'] and car[1] >= int(passengerNo):
			carPriceList.append([item['car_type'], item['price'], "Dave"])

for item in de['options']:
	#print (item)
	#print (item['car_type'])
	for car in carCapacityList:
		if car[0] == item['car_type'] and car[1] >= int(passengerNo):
			appendedItem = 0
			for i in carPriceList:
				if i[0] == car[0]:
					appendedItem = 1
					if int(i[1]) > int(item['price']):
						itemIndex = carPriceList.index(i)
						carPriceList[itemIndex] = [i[0], item['price'], "Eric"]
			if appendedItem == 0:
				carPriceList.append([item['car_type'], item['price'], "Eric"])

for item in dj['options']:
	#print (item)
	#print (item['car_type'])
	for car in carCapacityList:
		if car[0] == item['car_type'] and car[1] >= int(passengerNo):
			appendedItem = 0
			for i in carPriceList:
				if i[0] == car[0]:
					appendedItem = 1
					if int(i[1]) > int(item['price']):
						itemIndex = carPriceList.index(i)
						carPriceList[itemIndex] = [i[0], item['price'], "Jeff"]
			if appendedItem == 0:
				carPriceList.append([item['car_type'], item['price'], "Jeff"])


print ("")
print ("All done! Here are your cheapest options!")
#print (carPriceList)

futureJson = {}

for item in carPriceList:
	carPriceValues = str(item[0]) + " - " + item[2] + " - " + str(item[1])
	futureJson[str(item[0])] = {"supplier_id": item[2], "price": item[1]}
	print (carPriceValues)

print ("")
print (json.dumps(futureJson))