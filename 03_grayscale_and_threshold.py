"""
03. Перетворення кольорового зображення у відтінки сірого
та створення чорно-білого зображення (бінаризація).
"""
import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "image.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Не знайдено зображення: {image_path}")

# Перетворюємо BGR у Grayscale. Тепер кожен піксель має одне значення 0..255.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Порогове перетворення:
# значення > 127 стає білим (255), решта — чорним (0).
# THRESH_BINARY повертає також використаний поріг та нове зображення.
threshold_value, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

print("Застосований поріг:", threshold_value)
cv2.imshow("Original - color", image)
cv2.imshow("Grayscale - shades of gray", gray)
cv2.imshow("Binary - black and white", binary)

cv2.imwrite("gray.jpg", gray)
cv2.imwrite("black_white.png", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
