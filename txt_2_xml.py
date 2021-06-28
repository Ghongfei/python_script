# import copy
# from lxml.etree import Element, SubElement, tostring, ElementTree
# import cv2
#
# # 修改为你自己的路径
# template_file = 'G:\\dataset\\WJ-data\\anno.xml'
# target_dir = 'G:\\dataset\\WJ-data\\Annotations\\'
# image_dir = 'G:\\dataset\\train\\'  # 图片文件夹
# train_file = 'G:\\dataset\\train.txt'  # 存储了图片信息的txt文件
#
# with open(train_file) as f:
#     trainfiles = f.readlines()  # 标注数据 格式(filename label x_min y_min x_max y_max)
#
# file_names = []
# tree = ElementTree()
#
# for line in trainfiles:
#     trainFile = line.split()
#     file_name = trainFile[0]
#     print(file_name)
#
#     # 如果没有重复，则顺利进行。这给的数据集一张图片的多个框没有写在一起。
#     if file_name not in file_names:
#         file_names.append(file_name)
#         lable = trainFile[1]
#         xmin = trainFile[2]
#         ymin = trainFile[3]
#         xmax = trainFile[4]
#         ymax = trainFile[5]
#
#         tree.parse(template_file)
#         root = tree.getroot()
#         root.find('filename').text = file_name
#
#         # size
#         sz = root.find('size')
#         im = cv2.imread(image_dir + file_name)  # 读取图片信息
#
#         sz.find('height').text = str(im.shape[0])
#         sz.find('width').text = str(im.shape[1])
#         sz.find('depth').text = str(im.shape[2])
#
#         # object 因为我的数据集都只有一个框
#         obj = root.find('object')
#
#         obj.find('name').text = lable
#         bb = obj.find('bndbox')
#         bb.find('xmin').text = xmin
#         bb.find('ymin').text = ymin
#         bb.find('xmax').text = xmax
#         bb.find('ymax').text = ymax
#         # 如果重复，则需要添加object框
#     else:
#         lable = trainFile[1]
#         xmin = trainFile[2]
#         ymin = trainFile[3]
#         xmax = trainFile[4]
#         ymax = trainFile[5]
#
#         xml_file = file_name.replace('jpg', 'xml')
#         tree.parse(target_dir + xml_file)  # 如果已经重复
#         root = tree.getroot()
#
#         obj_ori = root.find('object')
#
#         obj = copy.deepcopy(obj_ori)  # 注意这里深拷贝
#
#         obj.find('name').text = lable
#         bb = obj.find('bndbox')
#         bb.find('xmin').text = xmin
#         bb.find('ymin').text = ymin
#         bb.find('xmax').text = xmax
#         bb.find('ymax').text = ymax
#         root.append(obj)
#
#     xml_file = file_name.replace('jpg', 'xml')
#     tree.write(target_dir + xml_file, encoding='utf-8')


from xml.dom.minidom import Document
import os
import cv2


def makexml(txtPath, xmlPath, picPath):  # 读取txt路径，xml保存路径，数据集图片所在路径
    dict = {'0': "belt",  # 字典对类型进行转换
            }
    files = os.listdir(txtPath)

    count = 0
    for i, name in enumerate(files):
        xmlBuilder = Document()
        annotation = xmlBuilder.createElement("annotation")  # 创建annotation标签
        xmlBuilder.appendChild(annotation)

        txtFile = open(txtPath + '\\' + name)
        txtList = txtFile.readlines()
        img = cv2.imread(picPath + '\\' + name[0:-4] + ".jpg")
        Pheight, Pwidth, Pdepth = img.shape

        folder = xmlBuilder.createElement("folder")  # folder标签
        folderContent = xmlBuilder.createTextNode("JPEGImages")
        folder.appendChild(folderContent)
        annotation.appendChild(folder)

        filename = xmlBuilder.createElement("filename")  # filename标签
        filenameContent = xmlBuilder.createTextNode(name[0:-4] + ".jpg")
        filename.appendChild(filenameContent)
        annotation.appendChild(filename)

        size = xmlBuilder.createElement("size")  # size标签
        width = xmlBuilder.createElement("width")  # size子标签width
        widthContent = xmlBuilder.createTextNode(str(Pwidth))
        width.appendChild(widthContent)
        size.appendChild(width)

        height = xmlBuilder.createElement("height")  # size子标签height
        heightContent = xmlBuilder.createTextNode(str(Pheight))
        height.appendChild(heightContent)
        size.appendChild(height)

        depth = xmlBuilder.createElement("depth")  # size子标签depth
        depthContent = xmlBuilder.createTextNode(str(Pdepth))
        depth.appendChild(depthContent)
        size.appendChild(depth)

        annotation.appendChild(size)


        for i in txtList:
            oneline = i.strip().split(" ")

            object = xmlBuilder.createElement("object")
            picname = xmlBuilder.createElement("name")
            nameContent = xmlBuilder.createTextNode(dict[oneline[0]])
            picname.appendChild(nameContent)
            object.appendChild(picname)

            pose = xmlBuilder.createElement("pose")
            poseContent = xmlBuilder.createTextNode("Unspecified")
            pose.appendChild(poseContent)
            object.appendChild(pose)

            truncated = xmlBuilder.createElement("truncated")
            truncatedContent = xmlBuilder.createTextNode("0")
            truncated.appendChild(truncatedContent)
            object.appendChild(truncated)

            difficult = xmlBuilder.createElement("difficult")
            difficultContent = xmlBuilder.createTextNode("0")
            difficult.appendChild(difficultContent)
            object.appendChild(difficult)

            bndbox = xmlBuilder.createElement("bndbox")
            xmin = xmlBuilder.createElement("xmin")
            mathData = int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)
            xminContent = xmlBuilder.createTextNode(str(mathData))
            xmin.appendChild(xminContent)
            bndbox.appendChild(xmin)

            ymin = xmlBuilder.createElement("ymin")
            mathData = int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)
            yminContent = xmlBuilder.createTextNode(str(mathData))
            ymin.appendChild(yminContent)
            bndbox.appendChild(ymin)

            xmax = xmlBuilder.createElement("xmax")
            mathData = int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)
            xmaxContent = xmlBuilder.createTextNode(str(mathData))
            xmax.appendChild(xmaxContent)
            bndbox.appendChild(xmax)

            ymax = xmlBuilder.createElement("ymax")
            mathData = int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)
            ymaxContent = xmlBuilder.createTextNode(str(mathData))
            ymax.appendChild(ymaxContent)
            bndbox.appendChild(ymax)

            object.appendChild(bndbox)

            annotation.appendChild(object)

        f = open(xmlPath + '\\' + name[0:-4] + ".xml", 'w')
        xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t')
        f.close()
        count += 1
        print('文件数量为：{}'.format(count))

paths_1 = 'E:\\HONGFEI\\arms\\knife_fire_fall_face_smoke_person_pic\\folder25'

labels_path1 = paths_1 + '\\' + 'labels'
xml_path1 = paths_1 + '\\' + 'Annotations_belt'
jpg_path1 = paths_1 + '\\' + 'JPEGImages'
makexml(labels_path1, xml_path1, jpg_path1)
print('编写xml文件完毕！')
