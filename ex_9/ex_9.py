# coding: UTF-8
from bs4 import BeautifulSoup
file = BeautifulSoup(open("demo.html", encoding='utf-8'))
href = file.select("[href]")
print(href)
