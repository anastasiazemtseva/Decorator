import csv

def saveToCsv(func):
    def wrapped():
        with open('csvv.csv','w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for i in func():
                csv_writer.writerow([i])
    return wrapped

@saveToCsv
def returnDictionary():
    x = []
    return x

returnDictionary()