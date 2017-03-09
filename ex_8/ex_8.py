
from bs4 import BeautifulSoup
file = BeautifulSoup(open("demo.html", encoding='utf-8'))
body_1 = file.find_all("body")
print(body_1)

