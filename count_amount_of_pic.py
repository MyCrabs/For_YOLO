import os

def count_images_in_directory(directory):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.txt']
    if not os.path.exists(directory):
        print(f"Thư mục '{directory}' không tồn tại.")
        return
    count = 0
    for filename in os.listdir(directory):
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            count += 1
    return count

directory_path = "C:/Users/ADMIN/Desktop/labels"

image_count = count_images_in_directory(directory_path)
if image_count is not None:
    print(f"Số lượng ảnh trong thư mục '{directory_path}' là: {image_count}")
