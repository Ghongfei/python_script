
import os
from os.path import join
import shutil
import random
from lxml.etree import parse, Element, SubElement, tostring
from copy import copy


# classes = ['face', 'person', 'fire', 'smoke', 'fall', 'fall,person','person,fall', 'danger', 'head', 'hat', 'reflective']
classes = ['face', 'person', 'fire', 'smoke', 'fall,person', 'danger', 'head', 'hat', 'reflective']




total = [0, 0, 0, 0, 0, 0, 0, 0, 0]
others = set()
others_count = 0
all_img = []



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
 
def convert_annotation(path, xml_file):
    global total, all_img, others_count
    # img = path + 'JPEGImages/' + xml_file.replace('.xml', '.jpg')
    # if not os.path.exists(img):
    #     print(img)
    #     return
    # all_img.append(img)
    # in_file = open(path + 'Annotations/' + xml_file, 'r', encoding='UTF-8')
    # tree=ET.parse(in_file)
    tree = parse(path + 'Annotations_combine/' + xml_file)
    root = tree.getroot()
    folder = root.find('folder')
    filename = root.find('filename')
    size = root.find('size')

    roots = []
    for i in classes:
        r = Element('annotation')
        r.append(copy(folder))
        r.append(copy(filename))
        r.append(copy(size))
        roots.append(r)

    # size = root.find('size')
    # w = int(size.find('width').text)
    # h = int(size.find('height').text)
 
    
    for obj in root.findall('object'):
        # difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # if cls not in classes or int(difficult)==1:
        if cls == 'fall' or cls == 'person,fall':
            cls = 'fall,person'
            obj.find('name').text = cls

        if cls not in classes:
            others.add(cls)
            others_count += 1
            # print(img)
            continue

        cls_id = classes.index(cls)
        total[cls_id] += 1
        roots[cls_id].append(obj)


    for i, r in zip(classes, roots):
        xml = tostring(r, pretty_print=True)
        xml_name = path + 'Annotations_' + i + '/' + xml_file
        # print(xml_name)
        with open(xml_name, "wb") as f:
            f.write(xml)
            f.close()


def process(path):
    for i in classes:
        ann_dir = path + 'Annotations_' + i
        if not os.path.exists(ann_dir):
            os.mkdir(ann_dir)
    for xml_file in os.listdir(path + 'Annotations_combine'):
        # print(xml_file)
        convert_annotation(path, xml_file)




#path1 = 'folder2/'
path2 = 'folder18/'
process(path2)




print(classes)
print('total', total)
print('others', others)
print('others_count', others_count)

