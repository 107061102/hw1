# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061102.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    #print(mycsv)
    header = mycsv.fieldnames
    #print(header)
    for row in mycsv:
        data.append(row)
        #print(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list
target_data = []
target_data_tmp = list(filter(lambda item: item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000', data))

if sum(float(item['HUMD']) for item in target_data_tmp if item['station_id'] == 'C0A880') == 0: data = 'None'
else: data = sum(float(item['HUMD']) for item in target_data_tmp if item['station_id'] == 'C0A880')
target_data.append(['C0A880',data])
if sum(float(item['HUMD']) for item in target_data_tmp if item['station_id'] == 'C0F9A0') == 0: data = 'None'
else: data = sum(float(item['HUMD']) for item in target_data_tmp if item['station_id'] == 'C0F9A0')
target_data.append(['C0F9A0',data])
if sum(float(item['HUMD']) for item in target_data_tmp if item['station_id'] == 'C0G640') == 0: data = 'None'
else: data = sum(float(item['HUMD']) for item in target_data_tmp if item['station_id'] == 'C0G640')
target_data.append(['C0G640',data])
if sum(float(item['HUMD']) for item in target_data_tmp if item['station_id'] == 'C0R190') == 0: data = 'None'
else: data = sum(float(item['HUMD']) for item in target_data_tmp if item['station_id'] == 'C0R190')
target_data.append(['C0R190',data])
if sum(float(item['HUMD']) for item in target_data_tmp if item['station_id'] == 'C0X260') == 0: data = 'None'
else: data = sum(float(item['HUMD']) for item in target_data_tmp if item['station_id'] == 'C0X260')
target_data.append(['C0X260',data])

# Retrive ten data points from the beginning.

#target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================
