"""
02. Колірні канали BGR та перетворення у RGB.

OpenCV за замовчуванням зберігає колір у порядку BGR:
синій, зелений, червоний. Багато інших бібліотек використовують RGB.
"""
import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "image.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Не знайдено зображення: {image_path}")

# Розділяємо три канали на окремі одноканальні зображення.
blue, green, red = cv2.split(image)

# Показуємо канали окремо. Яскравість пікселя показує силу відповідного каналу.
cv2.imshow("Blue channel", blue)
cv2.imshow("Green channel", green)
cv2.imshow("Red channel", red)

# Збираємо канали назад у початковому порядку BGR.
merged = cv2.merge((blue, green, red))
cv2.imshow("Merged BGR", merged)

# Перетворюємо BGR у RGB. Це важливо, наприклад, перед передачею в Matplotlib.
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print("Піксель у BGR:", image[0, 0])
print("Той самий піксель у RGB:", rgb[0, 0])

cv2.waitKey(0)
cv2.destroyAllWindows()
