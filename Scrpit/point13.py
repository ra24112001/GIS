import os
from PIL import Image, ExifTags

# Specify the directory where your images are located
img_folder = r"E:\FinalProjectGis\Image"
img_contents = os.listdir(img_folder)

for image in img_contents:

    full_path = os.path.join(img_folder, image)
    pillow_img = Image.open(full_path)
    exif = {ExifTags.TAGS[k]: v for k, v in pillow_img._getexif().items() if k in ExifTags.TAGS}
    print (exif)

