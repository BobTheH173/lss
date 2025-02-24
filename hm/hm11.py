import cv2
from PIL import Image

image_path = "../_ls11-man.jpg"
image = cv2.imread(image_path)

man_lower_cascade = cv2.CascadeClassifier("../_ls11-haarcascade_lowerbody.xml")
man_face_cascade = cv2.CascadeClassifier("_hm11-haarcascade_frontalface_default.xml")

man_pants = man_lower_cascade.detectMultiScale(image, scaleFactor=1.2, minNeighbors=5)
man_face = man_face_cascade.detectMultiScale(image, scaleFactor=1.2, minNeighbors=5)

man = Image.open(image_path).convert("RGBA")
pants = Image.open("../_ls11-pants.png").convert("RGBA")
hat = Image.open("_hm11-hat.png").convert("RGBA")

for (x, y, w, h) in man_pants:
    resized_pants = pants.resize((w - 90, int(h / 1.5)))
    man.paste(resized_pants, (x + 50, int(y + h / 5)), resized_pants)

for (x, y, w, h) in man_face:
    resized_hat = hat.resize((w + 65, h + 30))  # Resize hat based on face size
    man.paste(resized_hat, (x - 32, y - 50), resized_hat)  # Place above the face

# Save and show result
output_path = "_hm11-man_with_armor.png"
man.save(output_path)
man_with_armor = cv2.imread(output_path)

cv2.imshow("Man_with_armor", man_with_armor)
cv2.waitKey(0)
cv2.destroyAllWindows()
