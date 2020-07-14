
from PIL import Image, ImageFilter
import os

# Setup.
os.chdir(r"Modules\PIL_module\Images")
folder_pngs = 'pngs'
folder_Resize_300 = 'Resize_300'
folder_Resize_700 = 'Resize_700'
folder_Rotations = 'Rotations'
folder_BlackAndWhite = 'BlackAndWhite'
folder_Blurred = 'Blurred'

os.makedirs(f'{folder_pngs}')
os.makedirs(f'{folder_Resize_300}')
os.makedirs(f'{folder_Resize_700}')
os.makedirs(f'{folder_Rotations}')
os.makedirs(f'{folder_BlackAndWhite}')
os.makedirs(f'{folder_Blurred}')

image_size_300 = (300, 300)
image_size_700 = (700, 700)
degrees = 90

# Main().
for element in os.listdir('.'):
    # Accessing only the .jpg files in our folder
    if element.endswith('.jpg'):
        image = Image.open(element)
        # Taking the name and extension of our folders files.
        filename, fileExtension = os.path.splitext(element)

        # Modify and save our images to the 'pngs' folder.
        image.save(f"{os.getcwd()}\\{folder_pngs}\\{filename}.png")

        # Create our thumbnails with size 300 and save them.
        image.thumbnail(image_size_300)

        image.save(f"{os.getcwd()}\\{folder_Resize_300}\\{filename}_300.{fileExtension}")

        # Create our thumbnails with size 700 and save them.
        image.thumbnail(image_size_700)

        image.save(f"{os.getcwd()}\\{folder_Resize_700}\\{filename}_700.{fileExtension}")       
        
        # Rotate our images 90 degrees and save them.
        image.rotate(angle=degrees)

        image.save(f"{os.getcwd()}\\{folder_Rotations}\\{filename}_{str(degrees)}dg.{fileExtension}")        
        
        # Making our images black 'n' white and save them.
        image.convert(mode='L')

        image.save(f"{os.getcwd()}\\{folder_BlackAndWhite}\\{filename}_bnw.{fileExtension}")
 
        # Blurring our images  and save them.
        image.filter(ImageFilter.GaussianBlur(21))

        image.save(f"{os.getcwd()}\\{folder_Blurred}\\{filename}_blurr.{fileExtension}")
