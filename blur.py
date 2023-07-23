from PIL import Image, ImageFilter

before = Image.open("img.png")
after = before.filter(ImageFilter.BLUR)
after.save("out.png")

before1 = Image.open("img.png")
after1 = before1.filter(ImageFilter.BLUR)
after1.save("out1.png")
