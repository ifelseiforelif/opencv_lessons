
"""
10. Виявлення руху через вебкамеру за допомогою OpenCV.

Порівнюємо поточний кадр із попереднім.
Зміни підсвічуємо зеленими прямокутниками.

Натисніть Q або ESC для завершення.
"""

import cv2
import numpy as np
import sys

# =====================================
# 1. ВІДКРИВАЄМО ВЕБКАМЕРУ
# =====================================

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError(
        "Не вдалося відкрити камеру. "
        "Перевірте підключення та дозвіл Windows."
    )

# Налаштування роздільної здатності
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

previous_gray = None

# =====================================
# 2. ГОЛОВНИЙ ЦИКЛ
# =====================================

try:
    while True:

        success, frame = camera.read()

        if not success:
            print("Помилка отримання кадру")
            break

        # Дзеркальне відображення
        frame = cv2.flip(frame, 1)

        # =====================================
        # 3. ПІДГОТОВКА ЗОБРАЖЕННЯ
        # =====================================

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        # Зменшуємо шум
        gray = cv2.GaussianBlur(
            gray,
            (21, 21),
            0
        )

        # =====================================
        # 4. ВИЯВЛЕННЯ РУХУ
        # =====================================

        if previous_gray is not None:

            # Обчислюємо різницю між кадрами
            difference = cv2.absdiff(
                previous_gray,
                gray
            )

            # Бінаризація
            motion_mask: np.ndarray
            _, motion_mask = cv2.threshold(
                difference,
                25,
                255,
                cv2.THRESH_BINARY
            )

            # Прибираємо дрібні прогалини
            motion_mask = cv2.dilate(
                motion_mask,
                None,
                iterations=2
            )

            # =====================================
            # 5. ПОШУК КОНТУРІВ
            # =====================================

            contours, _ = cv2.findContours(
                motion_mask,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )

            motion_detected = False

            for contour in contours:

                area = cv2.contourArea(contour)

                # Ігноруємо маленькі зміни
                if area < 700:
                    continue

                motion_detected = True

                # Отримуємо прямокутник навколо руху
                x, y, w, h = cv2.boundingRect(contour)

                # Малюємо прямокутник
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                # Підпис
                cv2.putText(
                    frame,
                    "MOTION",
                    (x, max(y - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

            # =====================================
            # 6. СТАТУС РУХУ
            # =====================================

            if motion_detected:
                status = "MOVEMENT DETECTED"
                color = (0, 0, 255)
            else:
                status = "NO MOVEMENT"
                color = (0, 255, 0)

            cv2.putText(
                frame,
                status,
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2
            )

            # Показуємо маску руху
            cv2.imshow(
                "Motion Mask",
                motion_mask
            )

        # =====================================
        # 7. ЗБЕРІГАЄМО ПОПЕРЕДНІЙ КАДР
        # =====================================

        previous_gray = gray.copy()

        # Показуємо камеру
        cv2.imshow(
            "Motion Detection - Q to quit",
            frame
        )

        # Перевіряємо натискання клавіші
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q") or key == 27:
            break

finally:

    # =====================================
    # 8. ЗАКРИВАЄМО РЕСУРСИ
    # =====================================

    camera.release()
    cv2.destroyAllWindows()

    print("Програму завершено.")
