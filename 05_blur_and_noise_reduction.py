"""
05. Розмиття та зменшення шуму.

Фільтри згладжують дрібні коливання кольору. Це часто допомагає
перед пошуком контурів, але надмірне розмиття стирає дрібні деталі.
"""
import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "image.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Не знайдено зображення: {image_path}")

# Звичайне усереднювальне розмиття: усереднює значення пікселів у вікні 5x5.
average_blur = cv2.blur(image, (5, 5))

# Гаусове розмиття: центральні пікселі мають більшу вагу.
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Медіанний фільтр: добре прибирає імпульсний шум (окремі чорні/білі точки).
median_blur = cv2.medianBlur(image, 5)

cv2.imshow("Original", image)
cv2.imshow("Average blur", average_blur)
cv2.imshow("Gaussian blur", gaussian_blur)
cv2.imshow("Median blur", median_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
