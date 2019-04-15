参考自：
GitHub：https://github.com/qqwweee/keras-yolo3
博客：https://blog.csdn.net/sinat_26917383/article/details/85614247
https://blog.csdn.net/akenseren/article/details/83069190
https://blog.csdn.net/yuhq3/article/details/80281929
https://blog.csdn.net/qq_40013071/article/details/88395413

训练步骤：

1、利用xml文件或者其他方式生成所用到的txt文件，文件格式为：图像地址，xmin,ymin,xmax,ymax，类别ID+空格下一个box信息
eg: 
E:\test_idea\raccoon_dataset-master\images//raccoon-117.jpg 100,124,266,324,0 342,101,570,297,0
E:\test_idea\raccoon_dataset-master\images//raccoon-118.jpg 109,31,307,297,0

2、更改train.py文件中的信息，替换为所训练需要的数据（不使用预训练好的模型）
annotation_path 就是上述生成的txt文件，log_dir 一会生成模型存放的地址，classes_path 类别的名称（eg:person），一个一行，
anchors_path 存放通过聚类得到的anchors
def _main():
    annotation_path = 'redcell_anno_wyk.txt'
    log_dir = 'logs_redcell/'
    classes_path = 'model_data/redcell_classes.txt'
    anchors_path = 'model_data/yolo_anchors.txt'

这里load_pretrained改为False就可以了，表示不使用预训练好的模型进行训练
model = create_model(input_shape, anchors, num_classes,load_pretrained=True,
            freeze_body=2, weights_path='model_data\\darknet53_weights.h5')

3、使用预训练好的权重进行训练（适合样本比较少的场合）
为了加快训练速度，
下载darknet网络的预训练权重
	
https://pjreddie.com/media/files/darknet53.conv.74

	
将darknet53.conv.74改名为darknet53.weights,并转化为keras能够接受的权重形式

	
python convert.py -w darknet53.cfg darknet53.weights model_data/darknet53_weights.h5

这里load_pretrained改为True，freeze_body=2表示一开始训练的时候冻结前249层的权重信息（一共252层），训练一定的epoch后
，epoch的大小可以自己设定，然后再训练所有的层。
weights_path='model_data\\darknet53_weights.h5表示使用这个权重进行训练
model = create_model(input_shape, anchors, num_classes,load_pretrained=True,
            freeze_body=2, weights_path='model_data\\darknet53_weights.h5')

4、利用训练好的模型进行预测
修改yolo文件，如下（当最终的预测结果没有框的时候，可以通过修改"score"  "iou" 来解决），然后运行
python yolo_video.py --image 文件进行预测，进去以后再输入图片的地址
python yolo_video.py --input 视频地址 进行视频的预测

class YOLO(object):
    _defaults = {
        "model_path": 'E:\\test_idea\\wyk_yolo_redcell\\logs_redcell\\trained_weights_final_pre.h5',
        "anchors_path": 'model_data/yolo_anchors.txt',
        "classes_path": 'model_data/redcell_classes.txt',
        "score" : 0.3,
        "iou" : 0.45,
        "model_image_size" : (416, 416),
        "gpu_num" : 1,
    }



wyk_parase_anno.py 文件是进行文件的转换，将xml文件中的有用信息进行提取并转换为txt文件，在训练的时候会用到

batchsize别设置的太大，否则使用GPU进行训练的时候可能显示显存不够，oom error，需要调小batchsize。

font 文件夹需要存在，否则向图像中写入类别名称会有错误，在yolo文件的第129行


