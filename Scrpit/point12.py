import os
from  PIL import Image,ExifTags

# Specify the directory where your images are located
img_folder = r"E:\FinalProjectGis\Image"
img_contents = os.listdir(img_folder)


for image in img_contents:
    print (image)

    full_path=os.path.join(img_folder,image)
    print (full_path)

   
