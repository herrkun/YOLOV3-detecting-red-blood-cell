# YOLOV3-detecting-red-blood-cell
this is a yolov3 model that can detecting red-blood-cell

# Introduction
A Keras implementation of YOLOv3 (Tensorflow backend) inspired by https://github.com/qqwweee/keras-yolo3
## final results


# how to start  
## (1) just test model using pretrained weight  
    1、Download YOLOv3 weights from YOLO website.
    2、wget https://pjreddie.com/media/files/yolov3.weights or directly open this link on windows to download  
    3、Convert the Darknet YOLO model to a Keras model: python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
    4、Run YOLO detection.  
    5、modify yolo.py as         
        "model_path": 'model_data/yolo.h5',  
        "anchors_path": 'model_data/yolo_anchors.txt',  
        "classes_path": 'model_data/coco_classes.txt',  
    6、python yolo_video.py [OPTIONS...] --image, for image detection mode(you will input image_path later on the console)
    7、python yolo_video.py [video_path] [output_path (optional)], for video detection
 ## (2) train on your own data  
    1、download red-blood-cell dataset: https://github.com/cosmicad/dataset
    2、Convert the Darknet YOLO model to a Keras model: 
        python convert.py -w darknet53.cfg darknet53.weights model_data/darknet53_weights.h5
    3、transfer annotation files into a txt file
        just modify wyk_parase_anno.py--change "anno_dir" and "img_dir" to your dataset dir
        results format just like:
            One row for one image;
            Row format: image_file_path box1 box2 ... boxN;
            Box format: x_min,y_min,x_max,y_max,class_id (no space).
            (For VOC dataset, try python voc_annotation.py)
            Here is an example:
            path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
            path/to/img2.jpg 120,300,250,600,2
            ...
    4、if you wana use the pretrained weights , download here : https://pjreddie.com/media/files/darknet53.conv.74
       use the pretrained weights and you will get a better performance in a little dataset.  
       \if U do not wana use the pretrained weights, just modify wyk_train_redcell.py - load_pretrained=False.
    5、change to your own path, modify wyk_train_redcell.py-
        annotation_path = 'redcell_anno_wyk.txt'
        log_dir = 'logs_redcell/'
        classes_path = 'model_data/redcell_classes.txt'
        anchors_path = 'model_data/yolo_anchors.txt'
     6、run pyhton wyk_train_redcell.py and later you will see the weights in loggig dir
 ## (3)for more dataset to enjoy
    Hand detection : http://cvrr.ucsd.edu/vivachallenge/index.php/hands/hand-detection/
    Self-driving Car detection : http://cocodataset.org/#detections-challenge2017
    Kangaroo detection : https://github.com/experiencor/kangaroo
    Raccon detection : https://github.com/experiencor/raccoon_dataset
    
# tips
   these datasets are less images, so using pretrained will get a better performance than you train the model from the beginning.
# platform
   Keras 2.2.4  
   Tensorflow-gpu 1.12  
   windows 10  
