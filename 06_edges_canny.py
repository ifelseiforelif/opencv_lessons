"""
06. Пошук меж/контурних ліній за допомогою алгоритму Canny.

Canny знаходить різкі зміни яскравості. Результат — не заповнені
об'єкти, а тонкі лінії їхніх меж.
"""
import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "image.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Не знайдено зображення: {image_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Перед Canny трохи згладжуємо шум, щоб він не створював зайвих меж.
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 50 і 150 — нижній та верхній пороги алгоритму.
# Їх можна змінювати залежно від контрасту зображення.
edges = cv2.Canny(blurred, 50, 150)

cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("Canny edges", edges)
cv2.imwrite("canny_edges.png", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
