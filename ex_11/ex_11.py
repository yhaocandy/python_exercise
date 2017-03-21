# coding=utf-8
file = open("filtered_words.txt", "r")
filter_text = file.read().split("\n")


def check_txt():
    jf = False
    user1 = input("输入你想要的话:\n")
    for a in filter_text:
        if a in user1:
            jf = True

    if jf:
        print("no!")
    else:
        print("right")
check_txt()
