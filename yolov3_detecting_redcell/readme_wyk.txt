�ο��ԣ�
GitHub��https://github.com/qqwweee/keras-yolo3
���ͣ�https://blog.csdn.net/sinat_26917383/article/details/85614247
https://blog.csdn.net/akenseren/article/details/83069190
https://blog.csdn.net/yuhq3/article/details/80281929
https://blog.csdn.net/qq_40013071/article/details/88395413

ѵ�����裺

1������xml�ļ�����������ʽ�������õ���txt�ļ����ļ���ʽΪ��ͼ���ַ��xmin,ymin,xmax,ymax�����ID+�ո���һ��box��Ϣ
eg: 
E:\test_idea\raccoon_dataset-master\images//raccoon-117.jpg 100,124,266,324,0 342,101,570,297,0
E:\test_idea\raccoon_dataset-master\images//raccoon-118.jpg 109,31,307,297,0

2������train.py�ļ��е���Ϣ���滻Ϊ��ѵ����Ҫ�����ݣ���ʹ��Ԥѵ���õ�ģ�ͣ�
annotation_path �����������ɵ�txt�ļ���log_dir һ������ģ�ʹ�ŵĵ�ַ��classes_path �������ƣ�eg:person����һ��һ�У�
anchors_path ���ͨ������õ���anchors
def _main():
    annotation_path = 'redcell_anno_wyk.txt'
    log_dir = 'logs_redcell/'
    classes_path = 'model_data/redcell_classes.txt'
    anchors_path = 'model_data/yolo_anchors.txt'

����load_pretrained��ΪFalse�Ϳ����ˣ���ʾ��ʹ��Ԥѵ���õ�ģ�ͽ���ѵ��
model = create_model(input_shape, anchors, num_classes,load_pretrained=True,
            freeze_body=2, weights_path='model_data\\darknet53_weights.h5')

3��ʹ��Ԥѵ���õ�Ȩ�ؽ���ѵ�����ʺ������Ƚ��ٵĳ��ϣ�
Ϊ�˼ӿ�ѵ���ٶȣ�
����darknet�����Ԥѵ��Ȩ��
	
https://pjreddie.com/media/files/darknet53.conv.74

	
��darknet53.conv.74����Ϊdarknet53.weights,��ת��Ϊkeras�ܹ����ܵ�Ȩ����ʽ

	
python convert.py -w darknet53.cfg darknet53.weights model_data/darknet53_weights.h5

����load_pretrained��ΪTrue��freeze_body=2��ʾһ��ʼѵ����ʱ�򶳽�ǰ249���Ȩ����Ϣ��һ��252�㣩��ѵ��һ����epoch��
��epoch�Ĵ�С�����Լ��趨��Ȼ����ѵ�����еĲ㡣
weights_path='model_data\\darknet53_weights.h5��ʾʹ�����Ȩ�ؽ���ѵ��
model = create_model(input_shape, anchors, num_classes,load_pretrained=True,
            freeze_body=2, weights_path='model_data\\darknet53_weights.h5')

4������ѵ���õ�ģ�ͽ���Ԥ��
�޸�yolo�ļ������£������յ�Ԥ����û�п��ʱ�򣬿���ͨ���޸�"score"  "iou" ���������Ȼ������
python yolo_video.py --image �ļ�����Ԥ�⣬��ȥ�Ժ�������ͼƬ�ĵ�ַ
python yolo_video.py --input ��Ƶ��ַ ������Ƶ��Ԥ��

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



wyk_parase_anno.py �ļ��ǽ����ļ���ת������xml�ļ��е�������Ϣ������ȡ��ת��Ϊtxt�ļ�����ѵ����ʱ����õ�

batchsize�����õ�̫�󣬷���ʹ��GPU����ѵ����ʱ�������ʾ�Դ治����oom error����Ҫ��Сbatchsize��

font �ļ�����Ҫ���ڣ�������ͼ����д��������ƻ��д�����yolo�ļ��ĵ�129��


