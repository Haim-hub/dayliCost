import csv

in1 = str(raw_input())
todaysNumber = in1.split(",")
tab = float(todaysNumber[0])
days = float(todaysNumber[1])
lastMean = 0
with open('/Users/niklashaim/Documents/dayliCost/dataStorage.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
	 	if line_count == 0:
	 		line_count += 1
	 	else:
	 		tab += float(row[0])
	 		days += float(row[1])
	 		lastMean = float(row[2])
	 		line_count += 1	

newMean = tab/days
with open('/Users/niklashaim/Documents/dayliCost/dataStorage.csv', mode='a') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([todaysNumber[0],todaysNumber[1],newMean])							
print('The dayli cost changed from ' + str(lastMean) + ' to ' + str(newMean))    