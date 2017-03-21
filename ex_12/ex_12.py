# coding=utf-8
file = open("filtered_words.txt", "r")
filter_text = file.read().split("\n")


def check_txt():
    user1 = input("输入你想要的话:\n")
    for i in filter_text:
        if i in user1:
            user1 = user1.replace(i, "**")
    print(user1)

check_txt()