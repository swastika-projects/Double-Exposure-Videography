# Double-Exposure-Videography

![samsung PRISM worklet](https://user-images.githubusercontent.com/83866176/120084996-4eb47500-c0f2-11eb-8d46-8a3959c0e499.png)

This was a project assigned by Samsung PRISM which aimed at creating a double exposure video using Machine Learning/Deep Learning model for human segmentation followed by video processing to generate the required double exposure effect using Python Image Processing libraries. 
Additional Requirement : Playback FPS >=30

Model used for Human Segmentation : YOLACT (refer : https://github.com/dbolya/yolact.git)
FPS achieved : 18

*Output ScreenShot of YOLACT model :*

![original frame](https://user-images.githubusercontent.com/83866176/120083785-cbdaec80-c0e8-11eb-95d7-cb2fdd776747.png)




Next, used OPENCV Python library to get masked region from the previous output video. This was done in two steps : 
a) Extract each frame from the video
b) Change the BGR values of the surrounding to [0,0,0] (to convert it to black)

*Output ScreenShot after extracting the Masked Region :*

![masked frame](https://user-images.githubusercontent.com/83866176/120083943-ea8db300-c0e9-11eb-9c1d-5d3deb9a9b08.png)




Finally, merged an image with each frame of the output of previous video wherever BGR values equaled [0,0,0]

*Final Output ScreenShot :*

![double exposure](https://user-images.githubusercontent.com/83866176/120084022-9505d600-c0ea-11eb-9d4a-24faaf970e9a.png)






