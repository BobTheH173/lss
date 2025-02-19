import cv2
from PIL import Image

image_path = '_ls11-man.jpg'
image = cv2.imread(image_path)

cat_face_cascade = cv2.CascadeClassifier('_ls11-haarcascade_lowerbody.xml')
cat_face = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_path)
glasses = Image.open('_ls11-pants.png')
cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w-50, int(h/1.5)))
    cat.paste(glasses, (x+25, int(y + h/5)), glasses)
    cat.save("_ls11_3-man_with_pants.png")
    cat_with_glasses = cv2.imread("_ls11_3-man_with_pants.png")
    cv2.imshow("Man_with_pants", cat_with_glasses)
    cv2.waitKey()

# cv2.imshow("Cat", image)
# cv2.waitKey()
