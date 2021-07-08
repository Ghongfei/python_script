import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random

# classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', \
#      'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', \
#      'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', \
#      'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', \
#      'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', \
#      'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', \
#      'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', \
#      'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', \
#      'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

# classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", \
#       "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", \
#       "train", "tvmonitor"]

classes = ["person"]

idx = set()
# total_bd = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
# total_bd = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
total_bd = [0]
total_img = 0
name_set = set()

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(xml_file):
    global total_img
    in_file = open("Annotations/" + xml_file)
    txt_file = 'labels/' + xml_file[:-4] + '.txt'
    out_file = open(txt_file, 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    count = 0
    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        cls = obj.find('name').text
        name_set.add(cls)
        # if cls not in classes or int(difficult)==1:
        # if cls == 'motorbike' or cls == 'motorcycle':
        #     cls = 'motorcycle'
        # if cls == 'airplane' or cls == 'aeroplane':
        #     cls = 'airplane'
        # if cls == 'diningtable' or cls == 'dining table':
        #     cls = 'dining table'
        # if cls == 'couch' or cls == 'sofa':
        #     cls = 'couch'
        # if cls == 'pottedplant' or cls == 'potted plant':
        #     cls = 'potted plant'
        # if cls == 'tv' or cls == 'tvmonitor':
        #     cls = 'tv'
        if cls == 'car' or cls == 'bus':
            cls = 'car'

        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        idx.add(cls)
        total_bd[cls_id] += 1
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


        count += 1
    if count == 0:
        out_file.close()
        os.remove(txt_file)
    else:
        total_img += 1


if not os.path.exists('./labels/'):
    os.makedirs('./labels/')

all_xml = os.listdir('Annotations')
for xml_file in all_xml:
    convert_annotation(xml_file)




total_txt = os.listdir('labels')
trainval_percent = 0.2
num = len(total_txt)
indexes = range(num)
tv = int(num * trainval_percent)
trainval = random.sample(indexes, tv)
# ftrain = open('train.txt', 'w')
# ftest = open('test.txt', 'w')
list_train = open('train_car.txt', 'w')
list_test = open('test_car.txt', 'w')

for i in indexes:   
    if os.path.exists('/home/ai/kh/voc/VOCdevkit/VOC2012/JPEGImages/' + total_txt[i][:-4] + '.jpg'):
        # name1 = total_txt[i][:-4]  + '\n'
        name2 = "/home/ai/kh/voc/VOCdevkit/VOC2012/JPEGImages/" + total_txt[i][:-4]  + '.jpg' + '\n'
    elif os.path.exists('/home/ai/kh/voc/VOCdevkit/VOC2012/JPEGImages/' + total_txt[i][:-4] + '.jpeg'):
        # name1 = total_txt[i][:-4]  + '\n'
        name2 = "/home/ai/kh/voc/VOCdevkit/VOC2012/JPEGImages/" + total_txt[i][:-4]  + '.jpeg' + '\n'
    elif os.path.exists('/home/ai/kh/voc/VOCdevkit/VOC2012/JPEGImages/' + total_txt[i][:-4] + '.png'):
        # name1 = total_txt[i][:-4]  + '\n'
        name2 = "/home/ai/kh/voc/VOCdevkit/VOC2012/JPEGImages/" + total_txt[i][:-4]  + '.png' + '\n'
    else:
        continue
    if i in trainval:
        # ftest.write(name1)
        list_test.write(name2)
    else:
        # ftrain.write(name1)
        list_train.write(name2)


# ftrain.close()
# ftest.close()
list_train.close()
list_test.close()


print('idx:', idx)
print('total_bd:', total_bd)
print('total_img:', total_img)
print(name_set)
