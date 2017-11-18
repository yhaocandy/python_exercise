from wordcloud import ImageColorGenerator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread

text = open('132.txt','r').read()
bg_pic = imread('1234.jpg')

wordcloud = WordCloud(mask=bg_pic,background_color='white',scale=1.5).generate(text)
image_colos = ImageColorGenerator(bg_pic)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file('test.jpg')