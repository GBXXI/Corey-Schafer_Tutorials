
import concurrent.futures
import os
import time

import requests

imgs_url = [

    "https://images.pexels.com/photos/373912/pexels-photo-373912.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260",

    "https://images.pexels.com/photos/358457/pexels-photo-358457.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",

    "https://images.pexels.com/photos/277253/pexels-photo-277253.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",

    "https://images.pexels.com/photos/3445219/pexels-photo-3445219.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",

    "https://images.pexels.com/photos/544268/pexels-photo-544268.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",

    "https://images.pexels.com/photos/3942711/pexels-photo-3942711.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",

    "https://images.pexels.com/photos/931018/pexels-photo-931018.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",

    "https://images.pexels.com/photos/5454846/pexels-photo-5454846.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",

    "https://images.pexels.com/photos/5250367/pexels-photo-5250367.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",

    "https://images.pexels.com/photos/1028225/pexels-photo-1028225.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",

    "https://images.pexels.com/photos/5696925/pexels-photo-5696925.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
]

os.chdir(os.getcwd() + "\\Modules\\Threading_module")

start = time.perf_counter()

for img_url in imgs_url:
    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[4]
    img_name = f"{img_name}.jpg"

    with open(img_name, "wb") as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded..")

finish = time.perf_counter()        

print(f"Finished in {finish - start} second('s)")

# --------------------------------Using Threads---------------------------------
print()
start =  time.perf_counter()

def image_download(img_url):

    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[4]
    img_name = f"{img_name}.jpg"

    with open(img_name, "wb") as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded..")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(image_download, imgs_url)        

finish = time.perf_counter()        

print(f"Finished in {finish - start} second('s)")
