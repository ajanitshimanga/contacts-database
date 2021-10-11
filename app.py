import os

file1 = open("count.txt", "r")
value = int(file1.readline())
file1.close()

file1 = open("count.txt", "w")
file1.write(str(value+1))
file1.close()
