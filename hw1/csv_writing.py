import csv

data = [["col1","col2"],[23,45]]

# with open('example.csv','w',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#     data2 = ['test2','test1']
#     writer.writerow(data2)

file = open('example.csv', 'w',newline='')
writer = csv.writer(file)
writer.writerows(data)

string = ["123.jpg", "456.jpg"]
