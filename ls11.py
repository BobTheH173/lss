import cv2

image_path = '_ls11-cat.jpeg'
image = cv2.imread(image_path)
cv2.imshow("Cat", image)
cv2.waitKey()
