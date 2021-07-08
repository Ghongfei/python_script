import os
import shutil

# 文件路径
path1 = "E:\\抽烟\\0022\\"
# 目标路径
path2 = "C:\\Users\\Administrator\\Desktop\\aa\\"

filelist = os.listdir(path1)

if not os.path.exists(path2):
    os.makedirs(path2)

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
                shutil.copy(full_path1, despath1)
                shutil.copy(full_path2, despath2)


