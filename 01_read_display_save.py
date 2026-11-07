"""
01. Читання, показ і збереження зображення в OpenCV.

Запуск:
    python 01_read_display_save.py шлях/до/фото.jpg

Якщо шлях не вказано, скрипт шукає image.jpg поруч із файлом.
"""
import cv2
import sys

# Отримуємо шлях до зображення з аргументів командного рядка.
image_path = sys.argv[1] if len(sys.argv) > 1 else "image.jpg"

# IMREAD_COLOR завантажує зображення у кольорі (3 канали BGR).
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Якщо шлях неправильний або файл не знайдено, imread поверне None.
if image is None:
    raise FileNotFoundError(
        f"Не вдалося відкрити файл: {image_path}\n"
        "Передайте правильний шлях до JPG/PNG-файлу."
    )

# Форма масиву: (висота, ширина, кількість каналів).
height, width, channels = image.shape
print(f"Ширина: {width}px")
print(f"Висота: {height}px")
print(f"Кількість каналів: {channels}")

# OpenCV показує зображення у власному вікні.
cv2.imshow("Original image", image)

# Зберігаємо копію зображення. imwrite повертає True, якщо запис успішний.
saved = cv2.imwrite("copy_image.jpg", image)
print("Файл збережено:", saved)

# Чекаємо натискання будь-якої клавіші, інакше вікно одразу закриється.
cv2.waitKey(0)
cv2.destroyAllWindows()
