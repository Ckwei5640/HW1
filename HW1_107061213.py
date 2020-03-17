# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061213.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# C0A880, C0F9A0, C0G640, C0R190, C0X260

filt_data = list(filter(lambda item: 
                         (item['HUMD'] != '-99.000') & ((item['station_id'] == 'C0A880') | (item['station_id'] == 'C0F9A0') | (item['station_id'] == 'C0G640') | (item['station_id'] == 'C0R190') | (item['station_id'] == 'C0X260')), data)) 
         # 提取C0A880, C0F9A0, C0G640, C0R190, C0X260的測站資料

station = []
humd = []

for i in filt_data:
    if(i['station_id'] not in station):
        station.append(i['station_id'])
        humd.append(i['HUMD'])
    else:
        humd[station.index(i['station_id'])] = float(humd[station.index(i['station_id'])]) + float(i['HUMD'])  # sum up

for i in ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']:
    if(i not in station):        
        station.append(i),
        humd.append("None")    #檢查有沒有'沒資料的station'


# Retrive ten data points from the beginning.
target_data=[]
for i,j in zip(station,humd):    # 用zip將station & humd打包成tuple 形成list
    target_data.append([i,j])

target_data = sorted(target_data)  # 依照字母順序排列測站資料
#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================