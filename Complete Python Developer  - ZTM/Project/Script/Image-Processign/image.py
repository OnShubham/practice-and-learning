# this is simple images processing scr
from PIL import Image, ImageFilter

img = Image.open('./img/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blur.png", 'png')


