import cv2
import numpy as np
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "image.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Не знайдено зображення: {image_path}")

# Вибираємо прямокутник навколо об'єкта для виділення переднього плану.
#space or
rect = cv2.selectROI("Select object", image, False)

cv2.destroyWindow("Select object")

# Створюємо маску
mask = np.zeros(image.shape[:2], np.uint8)

# Моделі фону та переднього плану
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Запускаємо GrabCut
cv2.grabCut(
    image,
    mask,
    rect,
    bgdModel,
    fgdModel,
    5,
    cv2.GC_INIT_WITH_RECT
)

# Відокремлюємо передній план
mask2 = np.where(
    (mask == cv2.GC_FGD) |
    (mask == cv2.GC_PR_FGD),
    255,
    0
).astype("uint8")

# Застосовуємо маску до оригінального зображення
result = cv2.bitwise_and(image, image, mask=mask2)

# Знаходимо контури виділеного кота
contours, _ = cv2.findContours(
    mask2,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Малюємо контури
contour_image = image.copy()

cv2.drawContours(
    contour_image,
    contours,
    -1,
    (0, 255, 0),
    2
)

cv2.imshow("Original", image)
cv2.imshow("Cat mask", mask2)
cv2.imshow("Isolated cat", result)
cv2.imshow("Cat contours", contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()