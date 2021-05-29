import cv2
import numpy as np

#capture each frame of video
cap = cv2.VideoCapture('yolact-man-walking-output.mp4')
#get image to be blended with the video
image = cv2.imread('space.jpg')


offset = 50
#assign BGR values such that it refers to the masked region color
b = 70
g = 70
r = 150

#create writer object to save the output video files
original_video = cv2.VideoWriter('originalVideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (640, 480))
masked_video = cv2.VideoWriter('maskedVideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (640, 480))
final_video = cv2.VideoWriter('finalVideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (640, 480))

while(cap.isOpened()): #runs until video is opened

    ret, frame = cap.read()
    rgb_frame = frame[:, :, ::-1] # converts frame[BGR] to rgb_frame[RGB]

    #resize both frame and image
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    #display the original video before any processing
    cv2.imshow('Original Frame', frame)

    #save original video file in current working directory
    original_video.write(frame)

    #split each frame to extract BGR values
    b_ch, g_ch, r_ch = cv2.split(frame)

    # mask the different channels separately and assign BGR vlues [0,0,0] to convert it to black
    frame[np.where((b_ch < b - offset) | (b_ch > b + offset))] = 0
    frame[np.where((g_ch < g - offset) | (g_ch > g + offset))] = 0
    frame[np.where((r_ch < r - offset) | (r_ch > r + offset))] = 0

    #assign lower and upper boundaries to get regions in black
    upper_red = np.array([10, 10, 10])
    lower_red = np.array([0, 0, 0])

    #create a mask on the black region
    mask = cv2.inRange(frame, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #delete the black region from the original frame to get f
    f = frame - res
    #insert image at all places except the region 'f'
    f = np.where(f == 0, image, f)

    #display masked frame
    cv2.imshow('Masked Frame', frame)

    #save masked video file in current working directory
    masked_video.write(frame)

    #display final double exposure videography frame
    cv2.imshow('Double exposure', f)

    #save final video file in current working directory
    final_video.write(f)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
original_video.release()
masked_video.release()
final_video.release()
cv2.destroyAllWindows()



