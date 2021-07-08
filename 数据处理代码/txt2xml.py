import cv2
import os
from lxml.etree import Element, SubElement, tostring


mask_landmarks_label = "text.txt"

img = None

with open(mask_landmarks_label, "r") as f:
    line_list = list(f.readlines())
    for line_i, line in enumerate(line_list):
        if line.startswith("#"):
            _line = line.replace("\n", "")
            path = _line[2:]
            filename = _line[2:].split('/')[1]
            folder = _line[2:].split('/')[0]
            img = cv2.imread(path)
            w, h, c = img.shape

            node_root = Element('annotation')
            node_folder = SubElement(node_root, 'folder')
            node_folder.text = folder
            node_filename = SubElement(node_root, 'filename')
            node_filename.text = filename
            node_filename = SubElement(node_root, 'path')
            node_filename.text = path

            node_size = SubElement(node_root, 'size')
            node_width = SubElement(node_size, 'width')

            node_width.text = str(w)

            node_height = SubElement(node_size, 'height')
            node_height.text = str(h)

            node_depth = SubElement(node_size, 'depth')
            node_depth.text = str(c)



            line_j = line_i + 1
            while True:
                if (len(line_list)) == line_j:
                    break
                line = line_list[line_j]
                if line.startswith("#"):
                    break
                _line = line.replace("\n", "")
                label = _line.split(" ")[0]
                xmin = _line.split(" ")[1]
                ymin = _line.split(" ")[2]
                xmax = _line.split(" ")[3]
                ymax = _line.split(" ")[4]
                line_j = line_j + 1


                node_object = SubElement(node_root, 'object')
                node_name = SubElement(node_object, 'name')
                node_name.text = label
                node_difficult = SubElement(node_object, 'difficult')
                node_difficult.text = '0'
                node_bndbox = SubElement(node_object, 'bndbox')
                node_xmin = SubElement(node_bndbox, 'xmin')
                node_xmin.text = xmin
                node_ymin = SubElement(node_bndbox, 'ymin')
                node_ymin.text = ymin
                node_xmax = SubElement(node_bndbox, 'xmax')
                node_xmax.text = xmax
                node_ymax = SubElement(node_bndbox, 'ymax')
                node_ymax.text = ymax

            xml = tostring(node_root, pretty_print=True)
            xml_name = os.path.basename(path).split('.')[0] + ".xml"
            output_path = folder

            with open(os.path.join(folder, filename.replace(filename.split(".")[1], "xml")), "wb") as f:
                f.write(xml)
                f.close()
