def read_csv(file_name):
	with open(file_name) as csv_file:
    	csv_reader = csv.reader(csv_file, delimiter=',')
    lst = []
    for row in csv_reader:
    	lst += [row]
    return lst 

read_csv("jokes.csv")