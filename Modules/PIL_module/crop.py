
from PIL import Image

img_dir = 'D:\GBXXI\GB\'s PHOTOS\ΣΚΑΤΟΦΑΤΣΑ\IMG_20210307_103627.jpg'
image_size = [309,309]

image = Image.open(img_dir)

image.thumbnail(image_size)
image.save('D:\GBXXI\GB\'s PHOTOS\gbitsonis1.jpg', optimaze=True, quality=25)
print("Saved")
