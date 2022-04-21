
'''brand'''

import requests
from bs4 import BeautifulSoup
from datetime import datetime

brand="Shell"

def getWeek():
    return datetime.now().isocalendar()[1]

def get():
	diesel = ""
	page = requests.get("https://www.maisgasolina.com/")
	soup = BeautifulSoup(page.content, 'html.parser')
	results=soup.find_all("div", class_="entry")
	for x in results:
		if brand in str(x):
			diesel=x.find_all("div", class_="avg-price")
	soup = BeautifulSoup(str(diesel[1]), 'html.parser')
	results = soup.find_all("div", class_="avg-price")
	price = ""
	for x in results[0]:
		price+=str(x)
	#price = results[0]
	print(type(price))
	price = float(price.replace("</div>", "").split("€")[1])
	complete(price)

def complete(price):
	try:
		with open(f"{brand}/history.dat", "r") as f:
			data = f.read()
			data = data.split(", ")
	except:
		data = []
		for x in range(getWeek()-1):
			data.append(None)
	
		
	data.append(price)
	text = ""
	i = 0
	for x in data:
		if i!=0:
			text+=", "
		else:
			i=1
		text+=f"{str(x)}"

	with open(f"{brand}/history.dat", "w") as f:
		f.write(str(text))

def main():
	current_week = getWeek()
	try:
		with open(f"{brand}/week.dat", "r") as f:
			week = f.read()
	except:
		week = current_week
		get()

	if int(week) != current_week:
		get()
	with open(f"{brand}/week.dat", "w") as f:
		f.write(str(current_week))
	return

if __name__ == "__main__":
	main()

