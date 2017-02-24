import collections
file = open("story1.txt", "r")
str1 = file.read().split(" ")
print(str1)
print(collections.Counter(str1))
print(collections.Counter(str1)["and"])

