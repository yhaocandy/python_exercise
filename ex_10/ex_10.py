from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string
import random

def Color1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def Color2():
    return (random.randint(32, 127), random.randint(32 ,127), random.randint(32, 127))


str_num = string.digits+string.ascii_letters
key = [random.choice(str_num) for i in range(4)]
fin_str = ""
code = fin_str.join(key)


width = 150
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# font = None，size = 10，index = 0，encoding ='' ）
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)  # 创建字体
draw = ImageDraw.Draw(image)    # 创建可被修改的对象（image（要被修改的对象)，mode = None(颜色可选模式) ）
#  填充背景像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=Color1())
#  已知字母，填充颜色
for i in range(1, 25):
    draw.text((35, 10), code, font=font, fill=Color2())  #  （左右上下，text，fill = None，font = None，anchor = None，spacing = 0，align =“left” ）

image = image.filter(ImageFilter.BLUR)
image.save('ex_10.jpg', 'jpeg')



