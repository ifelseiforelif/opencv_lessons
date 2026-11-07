"""
08. Морфологічні операції: erosion, dilation, opening, closing.

Вони змінюють форму білих областей у бінарному зображенні.
Зручно прибирати дрібний шум, з'єднувати розірвані частини та змінювати товщину.
"""
import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "image.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Не знайдено зображення: {image_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Спочатку отримуємо чорно-біле зображення.
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Ядро (kernel) — невелика матриця, якою обробляється зображення.
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Erosion (ерозія): звужує білі області.
erosion = cv2.erode(binary, kernel, iterations=1)

# Dilation (дилатація): розширює білі області.
dilation = cv2.dilate(binary, kernel, iterations=1)

# Opening = erosion, потім dilation. Допомагає прибрати дрібні білі точки.
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# Closing = dilation, потім erosion. Допомагає закрити маленькі чорні отвори.
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Binary", binary)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
