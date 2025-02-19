import cv2

image_path = '_ls11-cat.jpeg'
image = cv2.imread(image_path)

cat_face_cascade = cv2.CascadeClassifier('_ls11-haarcascade_frontalcatface_extended.xml')
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)

for (x, y, w, h) in cat_face:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)

cv2.imshow("Cat", image)
cv2.waitKey()
