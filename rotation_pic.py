import cv2

image = cv2.imread("./picture/a5.jpg")
angle = int(input("Nhập góc xoay (tính bằng độ): "))
rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
cv2.imwrite(f"./picture/rotated{angle}_image.jpg", rotated_image)



