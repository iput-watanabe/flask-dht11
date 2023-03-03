import csv

CSV_FILENAME = './temp_humid_date.csv'

temp_data = []
humid_data = []
date_data = []
sensor_data =[temp_data, humid_data, date_data]

def get_csv_data():
    with open(CSV_FILENAME, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            sensor_data[0].append(row[0])
            sensor_data[1].append(row[1])
            sensor_data[2].append(row[2])
    
    return sensor_data

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    data = get_csv_data()
    print(data)

