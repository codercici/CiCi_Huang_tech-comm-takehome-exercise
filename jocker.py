import time
import csv
import sys 
import requests 

global_list = []

def deliver_joke(prompt, punchline): #procedure to deliver a joke 
	print(prompt)
	time.sleep(2)
	print(punchline)

def read_input(input): #read input during the game 
	if input == "next":
		return True
	elif input == "quit":
		return False
	else:
		print("I don't understand")

def read_csv(file_name): #read the argument csv FILE 
	lst = []
	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			lst += [row]
	return lst 


def get_data(): #determine what source to be used for delivering jokes 
	if len(sys.argv) < 2: #use Reddit as a data source because a csv file is not given
		global_list = from_online()
		return global_list
	elif len(sys.argv) == 2: #use the CSV file as a data source because it is given
		global_list = read_csv(sys.argv[1])
		return global_list
	else: #edge case, if the number of arguments is not correct
		print("The number of arguments is not correct! Please try again!")
		sys.exit()



def from_online(): #get jokes from reddit online 
	r = requests.get('https://www.reddit.com/r/dadjokes.json', headers = {'User-agent': 'your bot 0.1'})

	if not r or r.status_code >= 400: #edge case, check server error 
		print("The reddit link is not valid, Sorry for no jokes!")
		sys.exit()
		return 

	results = r.json()

	data = results['data']['children']
	lst = []

	for i in range(len(data)):
		r = data[i]['data']
		if r['over_18'] == False and r['selftext'] != '':
			if r['title'][:3] == 'Why' or r['title'][:4] == "What" or r['title'][:3] == "How":
				lst.append([r['title'], r['selftext']])
	return lst


if __name__ == "__main__": #main function 
	global_list = get_data()
	print("Hello, I am a jocker robot, please input 'next' for jokes or 'quit' to quit the game ")
	for row in global_list:
		right = "emmm?"
		while(right != True and right != False): #returned by read_input to handle user input 
			i = read_input(input("Please input next or quit: "))
			if i == True: #user inputs next 
				deliver_joke(row[0], row[1])
				right = True
			elif i == False: #user inputs quit 
				right = False
				sys.exit()
			else: #user input something else, goes back to while loop 
				right = "eemmm?"







