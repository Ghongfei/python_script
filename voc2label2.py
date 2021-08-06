import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random
import glob
import cv2


# classes = ['face', 'person', 'fire', 'smoke', 'fall', 'danger']
classes = ['belt']
path1 = 'folder19/Annotations/'


# total = [0, 0, 0, 0, 0, 0]
total = [0]
a = set()
all_img = []
others = 0

def clip(a, b, c):
    if a < b:
        a = b
    if a > c:
        a = c
    return a


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
    x = clip(x, 0, 1)
    y = clip(y, 0, 1)
    w = clip(w, 0, 1)
    h = clip(h, 0, 1)
    return (x,y,w,h)


def cal_iou(a, b):
    inter = (min(a[2], b[2]) - max(a[0], b[0])) * (min(a[3], b[3]) - max(a[1], b[1]))
    inter = inter if inter > 0 else 0
    union = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter
    return inter / union



def convert_annotation(xml_file):
    global total, others
    if os.path.exists(xml_file.replace('Annotations/', 'JPEGImages/').replace('.xml', '.jpg')):
        img = xml_file.replace('Annotations/', 'JPEGImages/').replace('.xml', '.jpg')
    elif os.path.exists(xml_file.replace('Annotations/', 'JPEGImages/').replace('.xml', '.png')):
        img = xml_file.replace('Annotations/', 'JPEGImages/').replace('.xml', '.png')
    else:
        return

    all_img.append(img)
    in_file = open(xml_file)
    # txt_file = os.path.join('labels', os.path.basename(xml_file).split('.')[0] + '.txt')
    txt_file = xml_file.replace('Annotations', 'labels').replace('.xml', '.txt')

    out_file = open(txt_file, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    img = cv2.imread(img)
    w = img.shape[1]
    h = img.shape[0]
    #size = root.find('size')
    #w = int(size.find('width').text)
    #h = int(size.find('height').text)

    count = 0

    person = []
    fall = []

    for obj in root.findall('object'):
        # difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # if cls not in classes or int(difficult)==1:
        # if cls == 'yanwu':
        #     cls = 'smoke'
        # if cls == 'fire、':
        #     cls = 'fire'
        # if cls == 'knife' or cls == 'gun' or cls == 'scissors' or cls == 'axe' or cls == 'hammer' or cls == 'stick' or cls == 'axew':
        #     cls = 'danger'
        # if cls == 'fallw' or cls == 'falld':
        #     cls = 'fall'
        if cls not in classes:
            others += 1
            a.add(cls)
            continue
        cls_id = classes.index(cls)
        total[cls_id] += 1
        xmlbox = obj.find('bndbox')
        xmin = float(xmlbox.find('xmin').text)
        xmax = float(xmlbox.find('xmax').text)
        ymin = float(xmlbox.find('ymin').text)
        ymax = float(xmlbox.find('ymax').text)
        xmin = clip(xmin, 0, w-1)
        xmax = clip(xmax, 0, w-1)
        ymin = clip(ymin, 0, h-1)
        ymax = clip(ymax, 0, h-1)

        b = (xmin, xmax, ymin, ymax)
        bb = convert((w,h), b)
        line = str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n'

        # if cls == 'person':
        #     person.append([line, [xmin, ymin, xmax, ymax]])
        #     continue
        # elif cls == 'fall':
        #     fall.append([line, [xmin, ymin, xmax, ymax]])
        #     continue

        out_file.write(line)
        count += 1

    # for i in fall:
    #     for j in person:
    #         iou = cal_iou(i[1], j[1])
    #         if iou > 0.9:
    #             person.remove(j)
    #             break
    #
    # for i in fall:
    #     out_file.write(i[0])
    # for i in person:
    #     out_file.write(i[0])

    out_file.close()
    # if count == 0:
    #     os.remove(txt_file)
    #     all_img.pop(-1)



def dir_xml_to_txt(path):
    for xml_file in glob.glob(path + '*.xml'):
        convert_annotation(xml_file)
dir_xml_to_txt(path1)



trainval_percent = 0.1   #可自行进行调节

 
num = len(all_img)
list_ = range(num)
tv = int(num * trainval_percent)
val = random.sample(list_, tv)
 
# ftest = open('test.txt', 'w')
# ftrain = open('train.txt', 'w')
#
# for i in list_:
#     name = os.getcwd() + '/' + all_img[i] + '\n'
#     if i in val:
#         ftest.write(name)
#     else:
#         ftrain.write(name)
 
# ftrain.close()
# ftest.close()

print('all classes:', classes)
print('total count:', total)
print('others:', a)
print('others total', others)
