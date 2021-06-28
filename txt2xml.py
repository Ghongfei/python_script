# import cv2
# import os
# from lxml.etree import Element, SubElement, tostring
#
#
# mask_landmarks_label = r"E:\HONGFEI\arms\knife_fire_fall_face_smoke_person_pic\folder2_pass\VID_20201103_124025_armed_002050.txt"
#
# img = None
#
# with open(mask_landmarks_label, "r") as f:
#     line_list = list(f.readlines())
#     for line_i, line in enumerate(line_list):
#         if line.startswith("#"):
#             _line = line.replace("\n", "")
#             path = _line[2:]
#             filename = _line[2:].split('/')[1]
#             folder = _line[2:].split('/')[0]
#             img = cv2.imread(path)
#             w, h, c = img.shape
#
#             node_root = Element('annotation')
#             node_folder = SubElement(node_root, 'folder')
#             node_folder.text = folder
#             node_filename = SubElement(node_root, 'filename')
#             node_filename.text = filename
#             node_filename = SubElement(node_root, 'path')
#             node_filename.text = path
#
#             node_size = SubElement(node_root, 'size')
#             node_width = SubElement(node_size, 'width')
#
#             node_width.text = str(w)
#
#             node_height = SubElement(node_size, 'height')
#             node_height.text = str(h)
#
#             node_depth = SubElement(node_size, 'depth')
#             node_depth.text = str(c)
#
#
#
#             line_j = line_i + 1
#             while True:
#                 if (len(line_list)) == line_j:
#                     break
#                 line = line_list[line_j]
#                 if line.startswith("#"):
#                     break
#                 _line = line.replace("\n", "")
#                 label = _line.split(" ")[0]
#                 xmin = _line.split(" ")[1]
#                 ymin = _line.split(" ")[2]
#                 xmax = _line.split(" ")[3]
#                 ymax = _line.split(" ")[4]
#                 line_j = line_j + 1
#
#
#                 node_object = SubElement(node_root, 'object')
#                 node_name = SubElement(node_object, 'name')
#                 node_name.text = label
#                 node_difficult = SubElement(node_object, 'difficult')
#                 node_difficult.text = '0'
#                 node_bndbox = SubElement(node_object, 'bndbox')
#                 node_xmin = SubElement(node_bndbox, 'xmin')
#                 node_xmin.text = xmin
#                 node_ymin = SubElement(node_bndbox, 'ymin')
#                 node_ymin.text = ymin
#                 node_xmax = SubElement(node_bndbox, 'xmax')
#                 node_xmax.text = xmax
#                 node_ymax = SubElement(node_bndbox, 'ymax')
#                 node_ymax.text = ymax
#
#             xml = tostring(node_root, pretty_print=True)
#             xml_name = os.path.basename(path).split('.')[0] + ".xml"
#             output_path = folder
#
#             with open(os.path.join(folder, filename.replace(filename.split(".")[1], "xml")), "wb") as f:
#                 f.write(xml)
#                 f.close()



import os
import xml.etree.ElementTree as ET
from PIL import Image
import numpy as np

img_path = r'E:\test\JPEGImages'                   #原图.jpg文件的路径
labels_path = r'E:\test\Annotations_bodys'                    #labels中.txt文件的路径
annotations_path = r'E:\test\xml'          #生成的xml文件需要保存的路径
labels = os.listdir(labels_path)
clsnames_path = r'E:\test\name.names'     #names文件的路径
with open(clsnames_path,'r') as f:
    classes = f.readlines()
    classes = [cls.strip('\n') for cls in classes]
def write_xml(imgname,filepath,labeldicts):                     #参数imagename是图片名（无后缀）
    root = ET.Element('Annotation')                             #创建Annotation根节点
    ET.SubElement(root, 'filename').text = str(imgname)         #创建filename子节点（无后缀）
    sizes = ET.SubElement(root,'size')                          #创建size子节点
    ET.SubElement(sizes, 'width').text = '1280'                 #没带脑子直接写了原图片的尺寸......
    ET.SubElement(sizes, 'height').text = '720'
    ET.SubElement(sizes, 'depth').text = '3'                    #图片的通道数：img.shape[2]
    for labeldict in labeldicts:
        objects = ET.SubElement(root, 'object')                 #创建object子节点
        ET.SubElement(objects, 'name').text = labeldict['name']        #BDD100K_10.names文件中
                                                                       #的类别名
        ET.SubElement(objects, 'pose').text = 'Unspecified'
        ET.SubElement(objects, 'truncated').text = '0'
        ET.SubElement(objects, 'difficult').text = '0'
        bndbox = ET.SubElement(objects,'bndbox')
        ET.SubElement(bndbox, 'xmin').text = str(int(labeldict['xmin']))
        ET.SubElement(bndbox, 'ymin').text = str(int(labeldict['ymin']))
        ET.SubElement(bndbox, 'xmax').text = str(int(labeldict['xmax']))
        ET.SubElement(bndbox, 'ymax').text = str(int(labeldict['ymax']))
    tree = ET.ElementTree(root)
    tree.write(filepath, encoding='utf-8')


for label in labels:                                           #批量读.txt文件
    with open(labels_path + label, 'r') as f:
        img_id = os.path.splitext(label)[0]
        contents = f.readlines()
        labeldicts = []
        for content in contents:
            img = np.array(Image.open(img_path+label.strip('.txt') + '.jpg'))
            sh,sw = img.shape[0],img.shape[1]                  #img.shape[0]是图片的高度720
                                                               #img.shape[1]是图片的宽度720
            content = content.strip('\n').split()
            x=float(content[1])*sw
            y=float(content[2])*sh
            w=float(content[3])*sw
            h=float(content[4])*sh
            new_dict = {'name': classes[int(content[0])],
                        'difficult': '0',
                        'xmin': x+1-w/2,                      #坐标转换公式看另一篇文章....
                        'ymin': y+1-h/2,
                        'xmax': x+1+w/2,
                        'ymax': y+1+h/2
                        }
            labeldicts.append(new_dict)
        write_xml(img_id, annotations_path + label.strip('.txt') + '.xml', labeldicts)
