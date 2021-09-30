import math
import csv

with open("data.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    total = 0
    number_of_entries = len(data)

    for x in data:
        total = total + int(x)

    mean = total / number_of_entries
    print("Mean is ",mean)
    return mean

squared_list = []

for number in data:
    ans = int(number) - mean(data)
    ans = ans**2
    squared_list.append(ans)

sum = 0
for i in squared_list:
    sum = sum + int(i)

result = sum / len(data)

standard_deviation = math.sqrt(result)
print("Standard Deviation is ", standard_deviation)