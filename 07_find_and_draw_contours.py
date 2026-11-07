"""
07. Знаходження контурів та малювання рамок навколо об'єктів.

Для findContours потрібне бінарне зображення: зазвичай білий об'єкт
на чорному фоні. Тут використаємо Canny як один зі способів отримати межі.
"""
import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "image.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Не знайдено зображення: {image_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

# RETR_EXTERNAL — шукаємо тільки зовнішні контури.
# CHAIN_APPROX_SIMPLE — стискаємо послідовності точок контуру.
contours, hierarchy = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

# Працюємо з копією, щоб не змінювати оригінал.
output = image.copy()

# Малюємо всі знайдені контури зеленим кольором, товщина 2 пікселі.
cv2.drawContours(output, contours, -1, (0, 255, 0), 2)

# Для кожного контуру знаходимо прямокутну рамку.
for index, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)

    # Відкидаємо дуже маленькі контури (часто це шум).
    if w * h < 100:
        continue

    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(
        output, f"Object {index}", (x, max(y - 8, 15)),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1
    )

print("Знайдено контурів:", len(contours))
cv2.imshow("Edges", edges)
cv2.imshow("Contours and bounding boxes", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
