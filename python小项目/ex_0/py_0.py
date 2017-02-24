from PIL import Image, ImageDraw, ImageFont
ex1 = Image.open("wife.jpg")
ex1_draw = ImageDraw.Draw(ex1)  # 创建文字
font = ImageFont.truetype("SIMLI.TTF", int(ex1.size[0] / 9))  # 选择字体颜色 和大小
ex1_draw.text((int(ex1.size[0] - 820), 0), " I love you", fill='red', font=font)  # 确定位置颜色，字体内容
# del ex1_draw  # 删除list
ex1.show()
ex1.save("new_tu.jpg")