import collections
for num in range(1, 6):
    st_file = "{}.txt".format(num)
    file = open(st_file, "r")
    str1 = file.read().split(" ")
    print(str1)
    important_word = ['people', 'blame', 'intelligent', 'opportunity', 'contentment' ]
    for word in important_word:
        print(collections.Counter(str1)[word])

