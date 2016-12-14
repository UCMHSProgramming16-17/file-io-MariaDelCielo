#csvwriting.py
#import module
import csv
import math

#create file
csvfile = open('csvwriting.csv', 'w')

#create csvwriter
csvwriter = csv.writer(csvfile, delimiter=',')

#write information
csvwriter.writerow(['a', 'b', 'c', 'd'])
csvwriter.writerow(['a', 'b', 'hypo'])
for a in range(1,10):
    for b in range(1,10):
        hypo = math.sqrt(a**2 + b**2)
        csvwriter.writerow([a, b, hypo])

#close file
csvfile.close()