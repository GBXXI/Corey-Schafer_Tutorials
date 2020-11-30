
import concurrent.futures
import os
import sys
import time
from itertools import repeat

from PIL import Image, ImageFilter

img_names = [
    '1028225.jpg',
    '277253.jpg',
    '3445219.jpg',
    '358457.jpg',
    '373912.jpg',
    '3942711.jpg',
    '5250367.jpg',
    '544268.jpg',
    '5454846.jpg',
    '5696925.jpg',
    '931018.jpg'
]

size = (1200, 1200)

directory = os.getcwd()

os.chdir(directory+"\\Modules\\Threading_module")

start = time.perf_counter()

for img_name in img_names:
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(17))

    img.thumbnail(size)
    img.save(directory+f"\\Modules\\Multiprocessing_Module\\{img_name}")
    print(f"{img_name} was processed..")

finish = time.perf_counter()

print(f"Finished in {finish-start} second('s)")

# -------------------------------Using Multiprocess-----------------------------
print()

def image_alteration(img_name, directory):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(17))

    img.thumbnail(size)
    img.save(directory+f"\\Modules\\Multiprocessing_Module\\{img_name}")
    print(f"{img_name} was processed..")


def goodbye():
    print('Solution?')


if __name__ == "__main__":
    
    try:
        dir_ = os.getcwd()

        os.chdir(dir_+"\\Modules\\Threading_module")
        
        print('Dir', dir_)
        start = time.perf_counter()

        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(image_alteration, img_names, repeat(dir_))
        
        finish = time.perf_counter()
        
        print(f"Finished in {finish-start} second('s)")
    except Exception:
        pass
