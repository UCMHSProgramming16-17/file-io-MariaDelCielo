# open file and allow yourself to write inside
file = open('mylist.txt', 'w')

#add items to file
for n in range(10):
    file.write(str(n)+input("Item! ") + '\n')

#close file
file.close()