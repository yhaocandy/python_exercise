from PIL import Image
for num in range(1, 11):
   picture1 = "{}.jpg".format(num)
   picture_1 = Image.open(picture1)
   print(picture_1.size) # 打印原图的分辨率
   a = picture_1.resize((3264, 2448))
   b = "new_{}.jpg".format(num)
   a.save(b)