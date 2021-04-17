
from PIL import Image
import os

os.chdir(r'D:\GBXXI\DOWNLOADS')
directory = os.getcwd()

filename = f"{directory}\\download.png"
image = Image.open(filename)

image.save('download_logo.ico', format='ICO', size=[(32, 32)])
