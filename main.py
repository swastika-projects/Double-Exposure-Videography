import cv2
import numpy as np

cap = cv2.VideoCapture('yolact-man-walking-output.mp4')
image = cv2.imread('space.jpg')


offset = 50
b = 80
g = 80
r = 150

while(cap.isOpened()):

    ret, frame = cap.read()
    rgb_frame = frame[:, :, ::-1] # converts frame[BGR] to rgb_frame[RGB]
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    cv2.imshow('Original Frame', frame)
    b_ch, g_ch, r_ch = cv2.split(frame)

    # mask the different channels seperately
    frame[np.where((b_ch < b - offset) | (b_ch > b + offset))] = 0
    frame[np.where((g_ch < g - offset) | (g_ch > g + offset))] = 0
    frame[np.where((r_ch < r - offset) | (r_ch > r + offset))] = 0

    upper_red = np.array([10, 10, 10])
    lower_red = np.array([0, 0, 0])

    mask = cv2.inRange(frame, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    f = frame - res
    f = np.where(f == 0, image, f)

    cv2.imshow('Masked Frame', frame)
    cv2.imshow('Double exposure', f)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()

