# YOLOV3-detecting-redcell
this is a yolov3 model that can detecting redcell

# Introduction
A Keras implementation of YOLOv3 (Tensorflow backend) inspired by https://github.com/qqwweee/keras-yolo3

# how to start  
## (1) just test model using pretrained weight  
    1、Download YOLOv3 weights from YOLO website.
    2、wget https://pjreddie.com/media/files/yolov3.weights or directly open this link on windows to download  
    3、Convert the Darknet YOLO model to a Keras model: python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
    4、Run YOLO detection.
    6、python yolo_video.py [OPTIONS...] --image, for image detection mode, OR
    7、python yolo_video.py [video_path] [output_path (optional)]
