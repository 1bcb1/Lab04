#  CC: Brooks Brickley & Hector Hernandez 2019
import math
from statistics import mean
print('What is the name of the file you want to open?')
file_name = input() + '.csv'
fileID = open(file_name, 'r')

print('What is the angle measurement?')
angle = math.radians(float(input()))
data = []
nextline = fileID.readline()
while nextline != '':
    data.append(nextline.split(','))
    nextline = fileID.readline()

accleration_x = []
accleration_y = []
accleration = []
for i in range(len(data)):
    accleration_x.append((float(data[i][1])))
    accleration_y.append(-1*float(data[i][2]))

for i in range(len(data)):
    a = math.sqrt(((accleration_x[i]**2) + (accleration_y[i]**2)))
    accleration.append(a)

average_accleration = mean(accleration) / 100

top = average_accleration-(9.81)*(math.sin(angle))
bottom = 9.81*(math.cos(angle))
answer = -top/bottom

print('What is the name of the file you want to add this answer to?')
name = input() + '.csv'

outfile = open(name, 'a')
outfile.write(str(answer) + '\n')
