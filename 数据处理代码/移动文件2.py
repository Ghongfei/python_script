import os
import shutil
# 文件路径
imgpath = 'C:/Users/Administrator/Desktop/aa'
labelpath = 'C:/Users/Administrator/Desktop/output2'
# 目标路径
imgdes = 'C:/Users/Administrator/Desktop/a/'
labeldes = 'C:/Users/Administrator/Desktop/b/'



for files1 in os.listdir(imgpath):
    imgname1 = os.path.splitext(files1)[1]
    imgname0 = os.path.splitext(files1)[0]

    for files2 in os.listdir(labelpath):
        txtname1 = os.path.splitext(files2)[1]
        txtname0 = os.path.splitext(files2)[0]
        if imgname0 == txtname0:
            full_path1 = os.path.join(imgpath, files1)
            full_path2 = os.path.join(labelpath, files2)
            despath1 = imgdes + files1
            despath2 = labeldes + files2
            shutil.move(full_path1, despath1)
            shutil.move(full_path2, despath2)



