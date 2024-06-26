# -*- coding: utf-8 -*-
"""capture.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q0cp6I6dM2srN1x1Pli1z9lsS6QuWl7Y
"""

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

ret, frame = cap.read()

if not ret:
    print("캡처 실패 - 카메라 프레임을 읽을 수 없습니다.")
    exit()

cv2.imshow("Captured Image", frame)
cv2.waitKey(0)

cv2.imwrite('captured_image.jpg', frame)

cap.release()
cv2.destroyAllWindows()