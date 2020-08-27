import os
import shutil

path_xml = "D://pig"
filelist = os.listdir(path_xml)
path1 = "D:\\pig"
path2 = "D:\\pig_d1\\"


for files1 in filelist:
    xmlname1 = os.path.splitext(files1)[1]  
    xmlname0 = os.path.splitext(files1)[0]  
    if xmlname1 == '.xml':
        for files2 in filelist:
            imgname1 = os.path.splitext(files2)[1]
            imgname0 = os.path.splitext(files2)[0]
            if imgname1 == '.jpg' and imgname0 == xmlname0:  
                full_path1 = os.path.join(path1, files1)
                full_path2 = os.path.join(path1, files2)
                despath1 = path2 + xmlname0+'.xml'
                despath2 = path2 + imgname0+'.jpg'
                shutil.move(full_path1, despath1)
                shutil.move(full_path2, despath2)


