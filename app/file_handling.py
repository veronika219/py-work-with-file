file = open("../apples.csv", "r")
print(file.readline()) # Read single line

print(file.readlines()) # read file into a list

file.seek(10) # set a point
print(file.read()) # and print file's content from 10 - elem

print(file.tell()) # show a current in file