# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:46:40 2019

@author: hit

2019.4.9 
该文件用来将xml文件中的有用信息提取出来，然后再转换为txt文件，然后该txt文件后续会被
用在神经网络的训练中


"""

import os
import xml.etree.ElementTree as ET

def trans_annototxt_wyk(anno_dir,img_dir):
    f=open("redcell_anno_wyk.txt",'w')
    
    for items in sorted(os.listdir(anno_dir)):
        tree=ET.parse(anno_dir+items)
        
        str=img_dir+items[:-4]+".jpg"
        if os.path.isfile(str):
            f.write(str)
            temp=0
            for elem in tree.iter():
                if "object" in elem.tag:
                    for attr in list(elem):
                        if "bndbox" in attr.tag:
                            obj={}
                            for dim in list(attr):
                                if "xmin" in dim.tag:
                                    obj["xmin"]=dim.text
                                if "ymin" in dim.tag:
                                    obj["ymin"]=dim.text
                                if "xmax" in dim.tag:
                                    obj["xmax"]=dim.text
                                if "ymax" in dim.tag:
                                    obj["ymax"]=dim.text
                            str2=obj["xmin"]+','+obj["ymin"]+','+obj["xmax"]+','+obj["ymax"]+','+'0'
                            if len(obj)>3:
                                temp=temp+1
                            if temp>1:
                                print('{} boxs exits'.format(temp))     # 17 images have two boxs
                                print(str)
                                f.write(' ')
                                f.write(str2)
                            else:
                                f.write(' ')
                                f.write(str2)
            f.write('\n')
            
    f.close()


anno_dir=r"E:\test_idea\redcell-yolo2-keras-master\RBC_datasets\Annotations//"
img_dir=r"E:\test_idea\redcell-yolo2-keras-master\RBC_datasets\JPEGImages//"

trans_annototxt_wyk(anno_dir,img_dir)