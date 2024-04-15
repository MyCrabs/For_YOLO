from PIL import Image
import os

src_folder = "C:/Users/ADMIN/Pictures/edit/"
dest_folder = "C:/Users/ADMIN/Pictures/edit/"
directory = os.listdir(src_folder)   # Listdir(): Dùng để lấy tên của file ảnh ra
print(directory)

for item in directory:
    img = Image.open(src_folder + item)
    width, height = img.size
    ratio = width / height
    new_width = 640
    new_height = int(new_width/ratio)
    imgResize = img.resize((new_width, new_height),Image.LANCZOS)
    imgResize.save(dest_folder + item[:-4] + ".jpg", quality = 100)    