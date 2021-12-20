import csv
from collections import Counter


## mean
with open("SOCR-HeightWeight.csv", newline='') as f:
    r = csv.reader(f)
    file_data = list(r)

file_data.pop(0)

data = []

for dt in range(len(file_data)):
    a = file_data[dt][1]
    data.append(float(a))

#-[2,3,4,5] --> 0+2+3+4

b = len(data)
sum = 0

for c in data:
    sum += c

mean = sum/b

## median

with open("SOCR-HeightWeight.csv", newline='') as we:
    s = csv.reader(we)
    file_data2 = list(s)

file_data2.pop(0)

data2 = []

for dt2 in range(len(file_data2)):
    a2 = file_data2[dt2][1]
    data2.append(float(a2))

#-[2,3,4,5] --> 0+2+3+4

#[2,4,78,56,4,6,1]

#[2,4,78,56,4,6]

data2.sort()
b2 = len(data2)

#floor division is done using '//'

if b2 % 2 == 0:
    m12 = float(data[b2//2])

    m22 = float(data[b2//2 - 1])
    
    median = m12+m22 // 2

else :
    median = data[b2//2]
    

## mode


with open("SOCR-HeightWeight.csv", newline='') as she:
    t = csv.reader(she)
    file_data3 = list(t)

file_data3.pop(0)

data3 = []

for dt3 in range(len(file_data3)):
    a3 = file_data[dt3][1]
    data3.append(float(a3))

mode_data = Counter(data3)

# {} represents dictionary
# "50-60" : 1

mode_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0,
}

#mode_data = [(58,2) , (69,3)]

for height, occurence in mode_data.items():
    if 50 < float(height) < 60:
        mode_range["50-60"] = mode_range["50-60"] + occurence
    elif 60 < float(height) < 70:
        mode_range["60-70"] = mode_range["60-70"] + occurence
    elif 70 < float(height) < 80:
        mode_range["70-80"] = mode_range["70-80"] + occurence

mode_r, mode_o = 0, 0

for range, occurence in mode_range.items():
    if occurence > mode_o:
        mode_r, mode_o =  [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float( (mode_r[0] + mode_r[1]) / 2 )

print("Median: ", str(median))

print("Mean: " , str(mean))

print("Mode: " , str(mode))


